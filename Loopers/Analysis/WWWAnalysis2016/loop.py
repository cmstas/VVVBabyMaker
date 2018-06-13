#!/bin/env python

import os
import sys
import ROOT
from QFramework import TQSampleFolder, TQXSecParser, TQCut, TQAnalysisSampleVisitor, TQSampleInitializer, TQCutflowAnalysisJob, TQCutflowPrinter, TQHistoMakerAnalysisJob, TQHWWPlotter, TQEventlistAnalysisJob
from rooutil.qutils import *
sys.path.append("..")
from cuts import *

def main(index):

    #
    #
    # Create the master TQSampleFolder
    #
    #
    samples = TQSampleFolder("samples")

    #
    #
    # Connect input baby ntuple
    #
    #
    connectNtuples(samples, "../samples.cfg", "/nfs-7/userdata/phchang/WWW_babies/WWW_v1.0.28/skim/", "<-1")

    #
    #
    # Define cuts
    #
    #
    if index ==-1: cuts = getWWWAnalysisCuts()
    if index == 0: cuts = getWWWAnalysisCuts()
    if index == 1: cuts = getWWWAnalysisCuts(jecvar_suffix="_up")
    if index == 2: cuts = getWWWAnalysisCuts(jecvar_suffix="_dn")

    #
    #
    # Define histograms
    #
    #
    histojob_filename = ".histo.cfg"
    f = open(histojob_filename, "w")
    f.write("""
    TH1F('MllSS' , '' , 180 , 0. , 300.) << (MllSS : '\#it{m}_{ll} [GeV]');
    #@*/*: MllSS;

    TH1F('MllZ' , '' , 180 , 60. , 120.) << (MllSS : '\#it{m}_{ll} [GeV]');
    #@*/*: MllZ;

    TH1F('MllZZoom' , '' , 180 , 80. , 100.) << (MllSS : '\#it{m}_{ll} [GeV]');
    #@*/*: MllZZoom;

    TH1F('M3l' , '' , 180 , 0. , 150.) << (M3l : '\#it{m}_{lll} [GeV]');
    #@*/*: M3l;

    TH1F('Pt3lGCR' , '' , 180 , 0. , 100.) << (Pt3l : '\#it{p}_{T,lll} [GeV]');
    #@*/*: Pt3lGCR;

    TH1F('Pt3l' , '' , 180 , 0. , 300.) << (Pt3l : '\#it{p}_{T,lll} [GeV]');
    #@*/*: Pt3l;

    TH1F('Ptll' , '' , 180 , 0. , 300.) << (Pt3l : '\#it{p}_{T,lll} [GeV]');
    #@*/*: Ptll;

    TH1F('nvtx' , '' , 60 , 0. , 60. ) << (nVert : 'Nvtx');
    #@*/*: nvtx;

    TH1F('Mjj' , '' , 180 , 0. , 300.) << (Mjj : '\#it{m}_{jj} [GeV]');
    #@*/*: Mjj;

    TH1F('MjjL' , '' , 180 , 0. , 750.) << (MjjL : '\#it{m}_{jj,central,leading} [GeV]');
    #@*/*: MjjL;

    TH1F('DetajjL' , '' , 180 , 0. , 5.) << (DetajjL : '\#it{m}_{jj,central,leading} [GeV]');
    #@*/*: DetajjL;

    TH1F('MjjVBF' , '' , 180 , 0. , 750.) << (MjjVBF : '\#it{m}_{jj,central,leading} [GeV]');
    #@*/*: MjjVBF;

    TH1F('DetajjVBF' , '' , 180 , 0. , 8.) << (DetajjVBF : '\#it{m}_{jj,central,leading} [GeV]');
    #@*/*: DetajjVBF;

    TH1F('MET' , '' , 180 , 0. , 180.) << (met_pt : 'MET [GeV]');
    #@*/*: MET;

    TH2F('lep0_pt_vs_eta' , '' , {0, 0.9, 1.6, 1.9, 2.4}, {20, 30, 40, 50, 60, 70, 150, 2000} ) << (lep_eta[0] : '\#eta_{lead-lep}', lep_pt[0] : '\#it{p}_{T, lead-lep} [GeV]');
    #@*/*: lep0_pt_vs_eta;

    TH2F('lep1_pt_vs_eta' , '' , {0, 0.9, 1.6, 1.9, 2.4}, {20, 30, 40, 50, 60, 70, 150, 2000} ) << (lep_eta[1] : '\#eta_{trail-lep}', lep_pt[1] : '\#it{p}_{T, trail-lep} [GeV]');
    #@*/*: lep1_pt_vs_eta;

    TH1F('lep_pt0' , '' , 180 , 0. , 250 ) << (lep_pt[0] : '\#it{p}_{T, lead-lep} [GeV]');
    #@*/*: lep_pt0;

    TH1F('lep_pt1' , '' , 180 , 0. , 150 ) << (lep_pt[1] : '\#it{p}_{T, trail-lep} [GeV]');
    #@*/*: lep_pt1;

    #TH1F('lep_pt2' , '' , 180 , 0. , 150 ) << (lep_pt[2] : '\#it{p}_{T, trail-lep} [GeV]');
    ##@*/*: lep_pt1;

    TH1F('lep_eta0' , '' , 180 , -2.5 , 2.5 ) << (lep_eta[0] : '\#eta_{lead-lep}');
    #@*/*: lep_eta0;

    TH1F('lep_eta1' , '' , 180 , -2.5 , 2.5 ) << (lep_eta[1] : '\#eta_{trail-lep}');
    #@*/*: lep_eta1;

    TH1F('lep_phi0' , '' , 180 , -3.1416 , 3.1416 ) << (lep_phi[0] : '\#phi_{lead-lep}');
    #@*/*: lep_phi0;

    TH1F('lep_phi1' , '' , 180 , -3.1416, 3.1416 ) << (lep_phi[1] : '\#phi_{trail-lep}');
    #@*/*: lep_phi1;

    TH1F('lep_relIso03EAv2Lep0' , '' , 180 , 0.0 , 0.2 ) << (lep_relIso03EAv2Lep[0] : 'I_{R=0.3,EA,Lep, lead-lep}');
    #@*/*: lep_relIso03EAv2Lep0;

    TH1F('lep_relIso03EAv2Lep1' , '' , 180 , 0.0 , 0.2 ) << (lep_relIso03EAv2Lep[1] : 'I_{R=0.3,EA,Lep, trail-lep}');
    #@*/*: lep_relIso03EAv2Lep1;

    TH1F('lep_relIso03EAv2Lep2' , '' , 180 , 0.0 , 0.2 ) << (lep_relIso03EAv2Lep[2] : 'I_{R=0.3,EA,Lep, trail-lep}');
    #@*/*: lep_relIso03EAv2Lep2;

    TH1F('nj' , '' , 7 , 0. , 7. ) << (nj : 'N_{jet}');
    #@*/*: nj;

    TH1F('nj30' , '' , 7 , 0. , 7. ) << (nj30 : 'N_{jet}');
    #@*/*: nj30;

    TH1F('nb' , '' , 5 , 0. , 5. ) << (nb : 'N_{b-jet}');
    #@*/*: nb;

    TH1F('jets_pt0' , '' , 180 , 0. , 250 ) << (jets_p4[0].pt() : '\#it{p}_{T, lead-jet} [GeV]');
    #@*/*: jets_pt0;

    TH1F('jets_pt1' , '' , 180 , 0. , 150 ) << (jets_p4[1].pt() : '\#it{p}_{T, trail-jet} [GeV]');
    #@*/*: jets_pt1;

    TH1F('jets_eta0' , '' , 180 , -5.0 , 5.0 ) << (jets_p4[0].eta() : '\#eta_{lead-jet}');
    #@*/*: jets_eta0;

    TH1F('jets_eta1' , '' , 180 , -5.0 , 5.0 ) << (jets_p4[1].eta() : '\#eta_{trail-jet}');
    #@*/*: jets_eta1;

    TH1F('jets_phi0' , '' , 180 , -3.1416, 3.1416 ) << (jets_p4[0].phi() : '\#phi_{lead-jet}');
    #@*/*: jets_phi0;

    TH1F('jets_phi1' , '' , 180 , -3.1416, 3.1416 ) << (jets_p4[1].phi() : '\#phi_{trail-jet}');
    #@*/*: jets_phi1;

    TH1F('MTmax3L' , '' , 180 , 0. , 300.) << ([MTMax3L] : '\#it{m}_{T,max} [GeV]');
    #@*/*: MTmax3L;

    TH1F('MT3rd' , '' , 180 , 0. , 300.) << (MT3rd : '\#it{m}_{T,3rd} [GeV]');
    #@*/*: MT3rd;

    @SRSSeePre: Mjj;
    @SRSSemPre: Mjj;
    @SRSSmmPre: Mjj;

    @SR0SFOSMET: MTmax3L;
    @SR0SFOSZVt: MTmax3L;
    @SR1SFOSZVt: MT3rd;

    @SideSSeeMjj: MjjVBF, DetajjVBF;
    @SideSSemMjj: MjjVBF, DetajjVBF;
    @SideSSmmMjj: MjjVBF, DetajjVBF;

    """)
    f.close()

    #
    #
    # Book Analysis Jobs (Histogramming, Cutflow, Event lists, etc.)
    #
    #
    histojob = TQHistoMakerAnalysisJob()
    histojob.importJobsFromTextFiles(histojob_filename, cuts, "*", True)

    # Analysis jobs
    cutflowjob = TQCutflowAnalysisJob("cutflow")
    cuts.addAnalysisJob(cutflowjob, "*")

    # Eventlist jobs (use this if we want to print out some event information in a text format e.g. run, lumi, evt or other variables.)
    #eventlistjob = TQEventlistAnalysisJob("eventlist")
    #eventlistjob.importJobsFromTextFiles("eventlist.cfg", cuts, "*", True)

    # Print cuts and numebr of booked analysis jobs for debugging purpose
    if index < 0:
        samples.printContents("t[*status]dr")
        cuts.printCut("trd")
        return

    #
    #
    # Add custom tqobservable that can do more than just string based draw statements
    #
    #
    from QFramework import TQObservable, TQWWWMTMax3L, TQWWWClosureEvtType
    customobservables = {}
    customobservables["MTMax3L"] = TQWWWMTMax3L("")
    customobservables["MTMax3L_up"] = TQWWWMTMax3L("_up")
    customobservables["MTMax3L_dn"] = TQWWWMTMax3L("_dn")
    TQObservable.addObservable(customobservables["MTMax3L"], "MTMax3L")
    TQObservable.addObservable(customobservables["MTMax3L_up"], "MTMax3L_up")
    TQObservable.addObservable(customobservables["MTMax3L_dn"], "MTMax3L_dn")

    # Print cuts and numebr of booked analysis jobs for debugging purpose
    cuts.printCut("trd")

    #
    #
    # Loop over the samples
    #
    #

    # setup a visitor to actually loop over ROOT files
    vis = TQAnalysisSampleVisitor(cuts, True)

    # Run the job!
    samples.visitSampleFolders(vis)

    # Write the output histograms and cutflow cut values and etc.
    if index == 0: samples.writeToFile("output.root", True)
    if index == 1: samples.writeToFile("output_jec_up.root", True)
    if index == 2: samples.writeToFile("output_jec_dn.root", True)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage:"
        print "  python {} INDEX".format(sys.argv[0])
        print ""
        print "  INDEX determines which variation to run"
        print " -1 : print cuts and samples and exit"
        print "  0 : nominal"
        print "  1 : jec_up"
        print "  2 : jec_dn"
        print ""
        sys.exit()

    main(int(sys.argv[1]))