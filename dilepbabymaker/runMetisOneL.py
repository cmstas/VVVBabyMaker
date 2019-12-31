##!/bin/env python

from condor_submit_util import submit
from time import sleep

#______________________________________________________________________________________
def get_master_list():

    dinfos = {}


    # not including ttV 
    # also not sure what the filtering is on vh_nonbb

    #########################################
    ######## One L Ntup MC 2017 94x v2 ######
    #########################################

    sample_info = {
	
	
	    # Signal
            "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                                          : "www_amcatnlo",
            "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                              : "vh_nonbb_amcatnlo",
            "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                          : "wwz_amcatnlo",
            "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                             : "wzz_amcatnlo",
            "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                             : "wzg_amcatnlo",
            "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                             : "zzz_amcatnlo",

	    # Diboson
            "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                     : "ww_incl_pythia",
            "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                     : "wz_incl_pythia",
	
	    # QCD 
            "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"            : "qcd_pt15_muenriched",
            "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"            : "qcd_pt20_muenriched",
            "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"            : "qcd_pt30_muenriched",
            "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"            : "qcd_pt50_muenriched",
            "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"           : "qcd_pt80_muenriched",
            "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"          : "qcd_pt120_muenriched",
            "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"          : "qcd_pt170_muenriched",
            "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"          : "qcd_pt300_muenriched",
            "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"          : "qcd_pt470_muenriched",
            "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"                             : "qcd_pt600_muenriched",
            #"/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"                            : "qcd_pt800_muenriched",
            #"/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"         : "qcd_pt1000_muenriched",
            "/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"               : "qcd_pt15_emenriched",
            "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"               : "qcd_pt20_emenriched",
            "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"               : "qcd_pt30_emenriched",
            "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"               : "qcd_pt50_emenriched",
            "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"              : "qcd_pt80_emenriched",
            "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"             : "qcd_pt120_emenriched",
            "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"                                : "qcd_pt170_emenriched",
            "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"             : "qcd_pt300_emenriched",
            "/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM"                                       : "qcd_pt15_bctoe",
            "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"            : "qcd_pt20_bctoe",
            "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                    : "qcd_pt30_bctoe",
            "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                   : "qcd_pt80_bctoe",
            "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                  : "qcd_pt170_bctoe",
            "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                  : "qcd_pt250_bctoe",
	
            # inclusive tt-bar and w+jets
            "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                    : "ttbar_incl_amcatnlo",
            "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM"            : "wjets_incl_madgraph",

	    # tt-bar
            "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "ttbar_1ltop_madgraph",
            "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"  : "ttbar_1ltbr_madgraph",
            "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"              : "ttbar_dilep_madgraph",

	    # single top
            "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"  : "singletop_schanlep_amcatnlo",
            "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"    : "tw_antitopnofullhad_powheg",
            "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"        : "tw_topnofullhad_powheg",
            "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"                    : "twz_incl_madgraph",
	
 	    # W +jets 
            "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"     : "wjets_ht100_madgraph",
            "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "wjets_ht200_madgraph",
            "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "wjets_ht400_madgraph",
            "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "wjets_ht600_madgraph",
            "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"    : "wjets_ht800_madgraph",
            "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"   : "wjets_ht1200_madgraph",
            "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"    : "wjets_ht2500_madgraph",

	    # Drell Yan
            "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                          : "dy_m1050_mgmlm",
            "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : "dy_m50_madgraph",
	
	    # Data
            "/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017B_se",
            "/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017C_se",
            "/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017D_se",
            "/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017E_se",
            "/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017F_se",
            "/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017B_mm",
            "/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017C_mm",
            "/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017D_mm",
            "/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017E_mm",
            "/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017F_mm",

            }

    dinfos["onel_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "OneL"
            }




    ##########################################
    ######## One L BABY MC 2018 102x v2 ######
    ##########################################

    sample_info = {

	    # signal
            "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                               : "www_amcatnlo"               ,
            "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                        : "vh_nonbb_amcatnlo"          ,
            "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                  : "wwz_amcatnlo"               ,
            "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                  : "wzz_amcatnlo"               ,
            "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                                       : "wzg_amcatnlo"               ,
            "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                  : "zzz_amcatnlo"               ,

	    # Drell Yan
            "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                    : "dy_m1050_madgraph"          ,
            "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"            : "dy_m50_madgraph",

	    # Diboson
            "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                                     : "ww_incl_pythia",
            "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"                                     : "wz_incl_pythia",
	    # QCD 
            "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"            : "qcd_pt15_muenriched",
            "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v4/MINIAODSIM"            : "qcd_pt20_muenriched",
            "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"            : "qcd_pt30_muenriched",
            "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"            : "qcd_pt50_muenriched",
            "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"           : "qcd_pt80_muenriched",
            "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"          : "qcd_pt120_muenriched",
            "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"          : "qcd_pt170_muenriched",
            "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"          : "qcd_pt300_muenriched",
            "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"          : "qcd_pt470_muenriched",
            "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"          : "qcd_pt600_muenriched",
            "/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"          : "qcd_pt15_emenriched",
            "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"               : "qcd_pt20_emenriched",
            "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"          : "qcd_pt30_emenriched",
            "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"               : "qcd_pt50_emenriched",
            "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"              : "qcd_pt80_emenriched",
            "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"             : "qcd_pt120_emenriched",
            "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"             : "qcd_pt170_emenriched",
            "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"             : "qcd_pt300_emenriched",
            "/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM"                            : "qcd_pt15_bctoe",
            "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM" : "qcd_pt20_bctoe",
            "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"         : "qcd_pt30_bctoe",
            "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"        : "qcd_pt80_bctoe",
            "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"       : "qcd_pt170_bctoe",
            "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"       : "qcd_pt250_bctoe",
	
	    # tt-bar and w+jets inclusive 
            "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"               : "ttbar_incl_amcatnlo",
            "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                 : "wjets_incl_madgraph",
	
 	    # tt-bar
            "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "ttbar_1ltop_madgraph",
            "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"  : "ttbar_1ltbr_madgraph",
            "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"              : "ttbar_dilep_madgraph",

	    # w+jets
            "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht100_madgraph",
            "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht200_madgraph",
            "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht400_madgraph",
            "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht600_madgraph",
            "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"    : "wjets_ht800_madgraph",
            "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"   : "wjets_ht1200_madgraph",
            "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"    : "wjets_ht2500_madgraph",

	    # single top
            "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4/MINIAODSIM"         : "sts_4f_leptonic_madgraph"   ,
            "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"              : "twz_ll_madgraph"            ,
            "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM" : "tw_antitopnofullhad_powheg" ,
            "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM"     : "tw_topnofullhad_powheg"     ,

	    # data 
            "/EGamma/Run2018A-17Sep2018-v2/MINIAOD"                                                                                           : "data_Run2018A_eg",
            "/EGamma/Run2018B-17Sep2018-v1/MINIAOD"                                                                                           : "data_Run2018B_eg",
            "/EGamma/Run2018C-17Sep2018-v1/MINIAOD"                                                                                           : "data_Run2018C_eg",
            # "/EGamma/Run2018D-PromptReco-v2/MINIAOD"                                                                                          : "data_Run2018D_eg",
            "/EGamma/Run2018D-22Jan2019-v2/MINIAOD"                                                                                           : "data_Run2018Dv2_ee_reproc",
            "/DoubleMuon/Run2018A-17Sep2018-v2/MINIAOD"                                                                                       : "data_Run2018A_mm",
            "/DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD"                                                                                       : "data_Run2018B_mm",
            "/DoubleMuon/Run2018C-17Sep2018-v1/MINIAOD"                                                                                       : "data_Run2018C_mm",
            "/DoubleMuon/Run2018D-PromptReco-v2/MINIAOD"                                                                                      : "data_Run2018D_mm",

            }

    dinfos["onel_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "OneL"
            }


    #########################################
    ######## One L Ntup MC 2017 94x v2 ######
    #########################################

    sample_info = {
	    # signal
            "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                         : "www_incl_amcatnlo",
            "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                  : "vh_nonbb_amcnlo",
            "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                            : "wwz_incl_amcnlo",
            "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                            : "wzz_incl_amcnlo",
            "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                            : "zzz_incl_amcnlo",
            "/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                                            : "wzg_incl_amcnlo",
            "/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"                                                       : "wwg_incl_amcnlo",

	    # qcd
            "/QCD_Pt_15to20_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                        : "qcd_pt15_bctoe",
            "/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                        : "qcd_pt20_bctoe",
            "/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                        : "qcd_pt30_bctoe",
            "/QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                : "qcd_pt80_bctoe",
            "/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                      : "qcd_pt170_bctoe",
            "/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                      : "qcd_pt250_bctoe",
            "/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                   : "qcd_pt20_emenriched",
            "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"              : "qcd_pt30_emenriched",
            "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"              : "qcd_pt50_emenriched",
            "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"             : "qcd_pt80_emenriched",
            "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"            : "qcd_pt120_emenriched",
            "/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                 : "qcd_pt170_emenriched",
            "/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                 : "qcd_pt300_emenriched",
            "/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                : "qcd_pt20_muenriched",
            "/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                : "qcd_pt30_muenriched",
            "/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                : "qcd_pt50_muenriched",
            "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"          : "qcd_pt80_muenriched",
            "/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"              : "qcd_pt120_muenriched",
            "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"         : "qcd_pt170_muenriched",
            "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"         : "qcd_pt300_muenriched",
            "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"         : "qcd_pt470_muenriched",
            "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"         : "qcd_pt600_muenriched",
            "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"             : "qcd_pt1000_muenriched",

	    # drell yan
            "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                   : "dy_m1050_amcatnlo",
            "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM"          : "dy_m50_amcatnlo",

	    # tt-bar and w+jets inclusive
            "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                         : "ttbar_incl_madgraph",
            "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM"                : "wjets_incl_mgmlm",


	    # diboson
            "/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                : "ww_2l2nu_powheg",
            "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                : "ww_lnuqq_powheg",
            "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                        : "wz_lnqq_amcatnlo",
            "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                          : "wz_1l3n_amcatnlo",
            "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                           : "wz_2l2q_amcatnlo",
            "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                      : "wz_3lnu_amcatnlo",

	    # ttbar
            "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    : "ttbar_1ltop_mgmlm_ext1",
            "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM" : "ttbar_1ltbr_mgmlm_ext1",
            "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                  : "ttbar_dilep_mgmlm_ext1",
	  
 	    # w+jets
            "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"         : "wjets_ht100_mgmlm_ext1",
            "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM"    : "wjets_ht200_mgmlm_ext1",
            "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    : "wjets_ht400_mgmlm_ext1",
            "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    : "wjets_ht600_mgmlm_ext1",
            "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"   : "wjets_ht800_mgmlm_ext1",
            "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"  : "wjets_ht1200_mgmlm_ext1",
            "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"        : "wjets_ht2500_mgmlm_ext1",

	    # data
            "/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD"     : "data_Run2016B_sm",
            "/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD"          : "data_Run2016C_sm",
            "/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD"          : "data_Run2016D_sm",
            "/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD"          : "data_Run2016E_sm",
            "/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD"          : "data_Run2016F_sm",
            "/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD"          : "data_Run2016G_sm",
            "/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD"          : "data_Run2016H_sm",
            "/SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD" : "data_Run2016B_se",
            "/SingleElectron/Run2016C-17Jul2018-v1/MINIAOD"      : "data_Run2016C_se",
            "/SingleElectron/Run2016D-17Jul2018-v1/MINIAOD"      : "data_Run2016D_se",
            "/SingleElectron/Run2016E-17Jul2018-v1/MINIAOD"      : "data_Run2016E_se",
            "/SingleElectron/Run2016F-17Jul2018-v1/MINIAOD"      : "data_Run2016F_se",
            "/SingleElectron/Run2016G-17Jul2018-v1/MINIAOD"      : "data_Run2016G_se",
            "/SingleElectron/Run2016H-17Jul2018-v1/MINIAOD"      : "data_Run2016H_se",
            }

    dinfos["onel_2016_94x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "OneL"
            }


    return dinfos

#################################################################################################################################################################################################
# SUBMIT JOBS
#################################################################################################################################################################################################


if __name__ == "__main__":

    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Submitting Baby Maker Jobs to Condor")
    parser.add_argument('-p' , '--production' , dest='production' , help='To submit ALL jobs for production'        , default=False         , action='store_true')
    parser.add_argument('-t' , '--test'       , dest='test'       , help='To submit test jobs (5 jobs each sample)' , default=False         , action='store_true')
    parser.add_argument(       '--tag'        , dest='tag'        , help='job tag'                                                          , required=True      )
    parser.add_argument(       '--sample_sets', dest='sample_sets', help='comma separated sample sets (e.g. WWW2018, WWW2017, FR2017, ...)' , required=True      )
    parser.add_argument(       '--single_sample_sample_name'     , dest='single_sample_sample_name'     , help='when SingleSample is included in --sample_sets option , then provide the name of the sample to be submitted here'       , required=False)
    parser.add_argument(       '--single_sample_sample_nicename' , dest='single_sample_sample_nicename' , help='when SingleSample is included in --sample_sets option , then provide the "nicename" of the sample to be submitted here' , required=False)
    parser.add_argument(       '--single_sample_sample_year'     , dest='single_sample_sample_year'     , help='when SingleSample is included in --sample_sets option , then provide the year to be submitted here'                     , required=False)
    parser.add_argument(       '--single_sample_sample_babytype' , dest='single_sample_sample_babytype' , help='when SingleSample is included in --sample_sets option , then provide the baby type of the job to be submitted here'     , required=False)

    args = parser.parse_args()

    if args.test and args.production:
        parser.print_help()
        print "ERROR: Option conflict. Can't have both -t,--test and -p,--production at the same time."
        sys.exit(1)

    if not args.test and not args.production:
        parser.print_help()
        print "ERROR: Option missing. Choose either -t,--test or -p,--production."
        sys.exit(1)

    if args.test:
        print "Submitting a test job (i.e. 5 jobs max each sample) with tag =", args.tag

    if args.production:
        print "Submitting a production job (i.e. ALL jobs per sample) with tag =", args.tag

    grand_master_list = get_master_list()

    # filter out grand master list and form a master list to be passed on to submit function
    master_list = {}
    if "OneL2016" in args.sample_sets:
	master_list["onel_2016_94x"]    = grand_master_list["onel_2016_94x"]
    if "OneL2017" in args.sample_sets:
	master_list["onel_2017_94x_v2"] = grand_master_list["onel_2017_94x_v2"]
    if "OneL2018" in args.sample_sets:
	master_list["onel_2018_102x"]   = grand_master_list["onel_2018_102x"]

    # If submitting a single sample
    if "SingleSample" in args.sample_sets:
        master_list["single_sample"] = {
            "samples" : {args.single_sample_sample_name:args.single_sample_sample_nicename},
            "year" : int(args.single_sample_sample_year),
            "baby_type" : args.single_sample_sample_babytype
            }

    submit(master_list, args.tag, dotestrun=args.test)

