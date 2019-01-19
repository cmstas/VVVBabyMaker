##!/bin/env python

from submit_condor_jobs import submit_condor_jobs



def get_master_list():

    dinfos = {}


    ##########################################
    ######## WWW BABY MC 2017 94x v2 #########
    ##########################################


    sample_info = {

            "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                                          : "www_amcatnlo",
            "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                              : "vh_nonbb_amcatnlo",
            "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                          : "dy_m1050_mgmlm",
            "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"                        : "dy_m50_amcatnlo",
            "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM"                              : "wjets_incl_mgmlm",
            "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                       : "wjets_ht100_madgraph",
            "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                       : "wjets_ht200_madgraph",
            "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                       : "wjets_ht400_madgraph",
            "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                       : "wjets_ht600_madgraph",
            "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                      : "wjets_ht800_madgraph",
            "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                     : "wjets_ht1200_madgraph",
            "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"                      : "wjets_ht2500_madgraph",
            "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"  : "singletop_schanlep_amcatnlo",
            #"/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : "singletop_tbrtchanincl_powheg", # Not sure of the status. Too tiny to care.
            #"/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "singletop_toptchanincl_powheg", # Not sure of the status. Too tiny to care.
            "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"    : "tw_antitopnofullhad_powheg",
            "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"        : "tw_topnofullhad_powheg",
            "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"                    : "ggh_hzz4l_powheg",
            "/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                  : "vbsww_madgraph",
            "/WW_DoubleScattering_13TeV-pythia8_TuneCP5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                      : "ww_dblsct_pythia",
            "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                                       : "ww_incl_pythia",
            "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"                            : "wz_3lv_amcatnlo",
            "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                                       : "wz_incl_pythia",
            "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                                 : "wz_lnqq_amcatnlo",
            "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                : "wz_1l3n_amcatnlo",
            "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                    : "wz_2l2q_amcatnlo",
            "/WZTo3LNu_0Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                     : "wz_3lv_0jmll4_madgraph",
            "/WZTo3LNu_0Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"                        : "wz_3lv_0jmll50_madgraph",
            "/WZTo3LNu_1Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                     : "wz_3lv_1jmll4_madgraph",
            "/WZTo3LNu_1Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                        : "wz_3lv_1jmll50_madgraph",
            "/WZTo3LNu_2Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                     : "wz_3lv_2jmll4_madgraph",
            "/WZTo3LNu_2Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                        : "wz_3lv_2jmll50_madgraph",
            "/WZTo3LNu_3Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                     : "wz_3lv_3jmll4_madgraph",
            "/WZTo3LNu_3Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                        : "wz_3lv_3jmll50_madgraph",
            "/WZTo3LNu_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                                                  : "wz_3lv_powheg",
            "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                                    : "zz_4l_powheg",
            "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                          : "wwz_amcatnlo",
            "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                             : "wzz_amcatnlo",
            "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                             : "wzg_amcatnlo",
            "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                             : "zzz_amcatnlo",
            "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                       : "ttbar_1ltop_mgmlm",
            "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                    : "ttbar_1ltbr_mgmlm",
            "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                : "ttbar_dilep_mgmlm",
            "/TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"               : "ttg_1ltop_madgraph",
            "/TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM"                        : "ttg_1ltbr_madgraph",
            "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                        : "ttw_lv_amcatnlo",
            "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                         : "ttw_qq_amcatnlo",
            "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                 : "ttz_m1to10ll_amcatnlo",
            "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                : "ttz_llvvm10_amcatnlo",
            "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                         : "ttz_qq_amcatnlo",
            "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                     : "tzq_ll_amcatnlo",
            "/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD"                                                                                                                      : "data_Run2017B_ee",
            "/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD"                                                                                                                      : "data_Run2017C_ee",
            "/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD"                                                                                                                      : "data_Run2017D_ee",
            "/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD"                                                                                                                      : "data_Run2017E_ee",
            "/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD"                                                                                                                      : "data_Run2017F_ee",
            "/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD"                                                                                                                    : "data_Run2017B_mm",
            "/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD"                                                                                                                    : "data_Run2017C_mm",
            "/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD"                                                                                                                    : "data_Run2017D_mm",
            "/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD"                                                                                                                    : "data_Run2017E_mm",
            "/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD"                                                                                                                    : "data_Run2017F_mm",
            "/MuonEG/Run2017B-31Mar2018-v1/MINIAOD"                                                                                                                        : "data_Run2017B_em",
            "/MuonEG/Run2017C-31Mar2018-v1/MINIAOD"                                                                                                                        : "data_Run2017C_em",
            "/MuonEG/Run2017D-31Mar2018-v1/MINIAOD"                                                                                                                        : "data_Run2017D_em",
            "/MuonEG/Run2017E-31Mar2018-v1/MINIAOD"                                                                                                                        : "data_Run2017E_em",
            "/MuonEG/Run2017F-31Mar2018-v1/MINIAOD"                                                                                                                        : "data_Run2017F_em",
            "/VHToWW_M125_13TeV_amcatnloFXFX_madspin_pythia8/PRIVATE_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-ext1-v2/MINIAODSIM"                    : "vh_ww_amcatnlo_private", # Private sample generated by Phil. Restricted to VH->WW but no dilep filter
            "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/PRIVATE_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                  : "www_amcatnlo_private",   # Private sample generated by Phil. W width not fixed and no dilep filter

            }

    dinfos["www_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "WWW"
            }


    #########################################
    ######## FR BABY MC 2017 94x v2 #########
    #########################################

    sample_info = {

            "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : "dy_m50_madgraph",
            "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                    : "ttbar_incl_amcatnlo",
            "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM"            : "wjets_incl_madgraph",
            "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                     : "ww_incl_pythia",
            "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                     : "wz_incl_pythia",
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
            "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                    : "qcd_pt20_bctoe",
            "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                    : "qcd_pt30_bctoe",
            "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                   : "qcd_pt80_bctoe",
            "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                  : "qcd_pt170_bctoe",
            "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                  : "qcd_pt250_bctoe",
            "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "ttbar_1ltop_madgraph",
            "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"  : "ttbar_1ltbr_madgraph",
            "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"              : "ttbar_dilep_madgraph",
            "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"     : "wjets_ht100_madgraph",
            "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "wjets_ht200_madgraph",
            "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "wjets_ht400_madgraph",
            "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "wjets_ht600_madgraph",
            "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"    : "wjets_ht800_madgraph",
            "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"   : "wjets_ht1200_madgraph",
            "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"    : "wjets_ht2500_madgraph",

            }

    dinfos["fr_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "FR"
            }

    ##########################################
    ######## TnP BABY MC 2017 94x v2 #########
    ##########################################

    sample_info = {

            "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : "dy_m50_madgraph",
            "/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017B_se",
            "/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017C_se",
            "/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017D_se",
            "/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017E_se",
            "/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD"                                                                                              : "data_Run2017F_se",
            "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017B_sm",
            "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017C_sm",
            "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017D_sm",
            "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017E_sm",
            "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD"                                                                                                  : "data_Run2017F_sm",
            "/MET/Run2017B-31Mar2018-v1/MINIAOD"                                                                                                         : "data_Run2017B_xe",
            "/MET/Run2017C-31Mar2018-v1/MINIAOD"                                                                                                         : "data_Run2017C_xe",
            "/MET/Run2017D-31Mar2018-v1/MINIAOD"                                                                                                         : "data_Run2017D_xe",
            "/MET/Run2017E-31Mar2018-v1/MINIAOD"                                                                                                         : "data_Run2017E_xe",
            "/MET/Run2017F-31Mar2018-v1/MINIAOD"                                                                                                         : "data_Run2017F_xe",

            }

    dinfos["tnp_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "TnP"
            }


    return dinfos

#################################################################################################################################################################################################
# SUBMIT JOBS
#################################################################################################################################################################################################

def submit_condor_jobs(tag):

    dinfos = get_master_list()

    for campaign in dinfos:

        submit_condor_jobs(
                samples_dictionary = dinfos[campaign]["samples"],
                year               = dinfos[campaign]["year"],
                baby_type          = dinfos[campaign]["baby_type"],
                baby_version_tag   = tag
                )

if __name__ == "__main__":

    submit_condor_jobs("v5.0.1") # Submitting 94x v2 2017 samples

#eof
