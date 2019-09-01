#!/bin/env python

import time
import json
import metis

from time import sleep

from metis.Sample import DirectorySample, SNTSample
from metis.CondorTask import CondorTask

from metis.StatsParser import StatsParser

import sys
import os
import glob
import subprocess

import dataset

#______________________________________________________________________________________
def get_tasks(samples_dictionary, year, baby_type, baby_version_tag, dotestrun=False):

    job_tag = "{}{}_{}".format(baby_type, year, baby_version_tag)

    # file/dir paths
    main_dir             = os.path.dirname(os.path.abspath(__file__))
    metis_path           = os.path.dirname(os.path.dirname(metis.__file__))
    tar_path             = os.path.join(metis_path, "package.tar")
    tar_gz_path          = tar_path + ".gz"
    exec_path            = os.path.join(main_dir, "metis.sh")
    merge_exec_path      = os.path.join(main_dir, "merge.sh")
    hadoop_path          = "metis/wwwbaby/{}".format(job_tag) # The output goes to /hadoop/cms/store/user/$USER/"hadoop_path"

    # Extra arguments that will be passed on to ./processBaby to specific which baby to create from the babymaker binary executable
    if baby_type == "WWW":
        args = "0" # WWWBaby
    elif baby_type == "FR":
        args = "1" # FRBaby
    elif baby_type == "OS":
        args = "2" # OSBaby
    elif baby_type == "TnP":
        args = "3" # TnPBaby
    elif baby_type == "All":
        args = "4" # AllBaby
    elif baby_type == "POG":
        args = "5" # POGBaby
    elif baby_type == "Loose":
        args = "6" # LooseBaby
    elif baby_type == "WWW3L":
        args = "7" # WWW3LBaby

    # Change directory to metis
    os.chdir(metis_path)

    tasks = []

    # BEGIN Sample Loop -------->
    # loop over the samples
    for sample in sorted(samples_dictionary.iterkeys()):

        #
        # Job 1 : Creating baby
        #

        # define the task
        maker_task = CondorTask(
                sample               = SNTSample(dataset=sample,
                                                 exclude_tag_pattern="CMS4_V08-*", # ignore new samples by sicheng for 2016 
                                                 ),
                tag                  = job_tag,
                arguments            = args,
                executable           = exec_path,
                tarfile              = tar_gz_path,
                special_dir          = hadoop_path,
                output_name          = "output.root",
                files_per_output     = 1,
                condor_submit_params = {"sites" : "T2_US_UCSD"},
                open_dataset         = False,
                flush                = True,
                max_jobs             = 5 if dotestrun else 0
                #no_load_from_backup  = True,
                )

        print sample, job_tag

        tasks.append(maker_task)

        #
        # Job 2 : Merging baby outputs
        #

        if maker_task.complete() and not dotestrun:

            merge_sample_name = "/MERGE_"+sample[1:]

            merge_task = CondorTask(
                    sample                 = DirectorySample(dataset=merge_sample_name, location=maker_task.get_outputdir()),
                    # open_dataset         = True, flush = True,
                    executable             = merge_exec_path,
                    tarfile                = tar_gz_path,
                    files_per_output       = 1,
                    max_jobs               = 1,
                    output_dir             = maker_task.get_outputdir() + "/merged",
                    output_name            = samples_dictionary[sample] + ".root",
                    condor_submit_params   = {"sites":"T2_US_UCSD"},
                    output_is_tree         = True,
                    # check_expectedevents = True,
                    tag                    = job_tag,
                    cmssw_version          = "CMSSW_9_2_0",
                    scram_arch             = "slc6_amd64_gcc530",
                    #no_load_from_backup    = True,
                    )
            merge_task.reset_io_mapping()
            merge_task.update_mapping()

            tasks.append(merge_task)

    # <------ END Sample Loop

    return tasks

#______________________________________________________________________________________
def create_tar_ball():
    # Create tarball
    metis_path = os.path.dirname(os.path.dirname(metis.__file__))
    tar_path = os.path.join(metis_path, "package.tar")
    tar_gz_path = tar_path + ".gz"
    main_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(main_dir)
    os.system("tar -chzf {} localsetup.sh processBaby *.so *.pcm coreutil/data coreutil/lib*.so *.txt btagsf MVAinput jetCorrections leptonSFs puWeight2016.root pileup_jul21_nominalUpDown.root ../CORE/Tools/ mergeHadoopFiles.C xsec_susy_13tev.root roccor.2017.v0/*.txt rooutil/hadd.py".format(tar_gz_path))

#______________________________________________________________________________________
def submit(dinfos, version_tag, dotestrun=False):

    create_tar_ball() # Create tar ball

    # Loop
    while True:

        tasks = [] # List to hold all the Metis Tasks
        total_summary = {} # Summary for task status report to access via http

        # Boolean to aggregate all the task compelete status
        all_tasks_complete = True

        # Loop over all the campaigns
        for campaign in dinfos:

            # Get all the tasks for this campaign
            this_set_of_tasks = get_tasks(
                    samples_dictionary = dinfos[campaign]["samples"],
                    year               = dinfos[campaign]["year"],
                    baby_type          = dinfos[campaign]["baby_type"],
                    baby_version_tag   = version_tag,
                    dotestrun          = dotestrun,
                    )

            # Need separate dictionaries for each tag in order to let StatsParsers uniquely handle same dataset name jobs.
            if len(this_set_of_tasks) > 0:
                print this_set_of_tasks[0].tag
                total_summary[this_set_of_tasks[0].tag] = {}

            # Add to the master list of tasks
            tasks += this_set_of_tasks

        # Loop over all the tasks
        for task in tasks:

            # Process the task (submit or resubmit)
            task.process()

            # save some information for the dashboard
            total_summary[task.tag][task.get_sample().get_datasetname()] = task.get_task_summary()

            # Aggregate task complete booleans
            all_tasks_complete = all_tasks_complete and task.complete()

        # parse the total summary and write out the dashboard
        #metis_dashboard_path = os.path.join(os.path.dirname(os.path.dirname(metis.__file__)), "dashboard")
        metis_dashboard_path = "~/public_html/dump"

        # Go through each tag and do StatsParser
        for tag in total_summary:
            StatsParser(data=total_summary[tag], webdir=metis_dashboard_path).do()

        # Print msummary table so I don't have to load up website
        #os.system("msummary -r -p MAKER | tee summary.txt")
        os.system("msummary -r | tee summary.txt")
        os.system("chmod -R 755 {}".format(metis_dashboard_path))

        # If all done exit the loop
        if all_tasks_complete:
            print ""
            print "All job finished"
            print ""
            break

        # Neat trick to not exit the script for force updating
        print 'Press Ctrl-C to force update, otherwise will sleep for 300 seconds'
        try:
            for i in range(0,300):
                sleep(1) # could use a backward counter to be preeety :)
        except KeyboardInterrupt:
            raw_input("Press Enter to force update, or Ctrl-C to quit.")
            print "Force updating..."

