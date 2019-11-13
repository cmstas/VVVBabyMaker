##!/bin/env python

from condor_submit_util import submit
from time import sleep

#______________________________________________________________________________________
def get_master_list():

    dinfos = {}

    #######################################
    ######## WWW BABY MC 2016 80x #########
    #######################################

    sample_info = {

            ###############################################################################
            # CMS4
            ###############################################################################
            # Data
            "/DoubleEG/Run2016B-03Feb2017_ver1-v1/MINIAOD"                                                                                                                                  : "data_Run2016B_03feb2017rereco_unmerged_ee_v1",
            "/DoubleEG/Run2016B-03Feb2017_ver2-v2/MINIAOD"                                                                                                                                  : "data_Run2016B_03feb2017rereco_unmerged_ee_v2",
            "/DoubleEG/Run2016C-03Feb2017-v1/MINIAOD"                                                                                                                                       : "data_Run2016C_03feb2017rereco_unmerged_ee_v1",
            "/DoubleEG/Run2016D-03Feb2017-v1/MINIAOD"                                                                                                                                       : "data_Run2016D_03feb2017rereco_unmerged_ee_v1",
            "/DoubleEG/Run2016E-03Feb2017-v1/MINIAOD"                                                                                                                                       : "data_Run2016E_03feb2017rereco_unmerged_ee_v1",
            "/DoubleEG/Run2016F-03Feb2017-v1/MINIAOD"                                                                                                                                       : "data_Run2016F_03feb2017rereco_unmerged_ee_v1",
            "/DoubleEG/Run2016G-03Feb2017-v1/MINIAOD"                                                                                                                                       : "data_Run2016G_03feb2017rereco_unmerged_ee_v1",
            "/DoubleEG/Run2016H-03Feb2017_ver2-v1/MINIAOD"                                                                                                                                  : "data_Run2016H_03feb2017rereco_unmerged_ee_v2",
            "/DoubleEG/Run2016H-03Feb2017_ver3-v1/MINIAOD"                                                                                                                                  : "data_Run2016H_03feb2017rereco_unmerged_ee_v3",
            "/DoubleMuon/Run2016B-03Feb2017_ver1-v1/MINIAOD"                                                                                                                                : "data_Run2016B_03feb2017rereco_unmerged_mm_v1",
            "/DoubleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD"                                                                                                                                : "data_Run2016B_03feb2017rereco_unmerged_mm_v2",
            "/DoubleMuon/Run2016C-03Feb2017-v1/MINIAOD"                                                                                                                                     : "data_Run2016C_03feb2017rereco_unmerged_mm_v1",
            "/DoubleMuon/Run2016D-03Feb2017-v1/MINIAOD"                                                                                                                                     : "data_Run2016D_03feb2017rereco_unmerged_mm_v1",
            "/DoubleMuon/Run2016E-03Feb2017-v1/MINIAOD"                                                                                                                                     : "data_Run2016E_03feb2017rereco_unmerged_mm_v1",
            "/DoubleMuon/Run2016F-03Feb2017-v1/MINIAOD"                                                                                                                                     : "data_Run2016F_03feb2017rereco_unmerged_mm_v1",
            "/DoubleMuon/Run2016G-03Feb2017-v1/MINIAOD"                                                                                                                                     : "data_Run2016G_03feb2017rereco_unmerged_mm_v1",
            "/DoubleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD"                                                                                                                                : "data_Run2016H_03feb2017rereco_unmerged_mm_v2",
            "/DoubleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD"                                                                                                                                : "data_Run2016H_03feb2017rereco_unmerged_mm_v3",
            "/MuonEG/Run2016B-03Feb2017_ver1-v1/MINIAOD"                                                                                                                                    : "data_Run2016B_03feb2017rereco_unmerged_em_v1",
            "/MuonEG/Run2016B-03Feb2017_ver2-v2/MINIAOD"                                                                                                                                    : "data_Run2016B_03feb2017rereco_unmerged_em_v2",
            "/MuonEG/Run2016C-03Feb2017-v1/MINIAOD"                                                                                                                                         : "data_Run2016C_03feb2017rereco_unmerged_em_v1",
            "/MuonEG/Run2016D-03Feb2017-v1/MINIAOD"                                                                                                                                         : "data_Run2016D_03feb2017rereco_unmerged_em_v1",
            "/MuonEG/Run2016E-03Feb2017-v1/MINIAOD"                                                                                                                                         : "data_Run2016E_03feb2017rereco_unmerged_em_v1",
            "/MuonEG/Run2016F-03Feb2017-v1/MINIAOD"                                                                                                                                         : "data_Run2016F_03feb2017rereco_unmerged_em_v1",
            "/MuonEG/Run2016G-03Feb2017-v1/MINIAOD"                                                                                                                                         : "data_Run2016G_03feb2017rereco_unmerged_em_v1",
            "/MuonEG/Run2016H-03Feb2017_ver2-v1/MINIAOD"                                                                                                                                    : "data_Run2016H_03feb2017rereco_unmerged_em_v2",
            "/MuonEG/Run2016H-03Feb2017_ver3-v1/MINIAOD"                                                                                                                                    : "data_Run2016H_03feb2017rereco_unmerged_em_v3",

            # Private from Mia
            "/PrivateWWW/www-cms4-Private80X-v1/MINIAODSIM"                                                                                                                                 : "www_2l_mia",
            "/PrivateWWW/wwwext-cms4-Private80X-v1/MINIAODSIM"                                                                                                                              : "www_2l_ext1_mia",

            # ttbar
            "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                  : "ttbar_1ltop_mgmlm_ext1",
            "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"               : "ttbar_1ltbr_mgmlm_ext1",
            "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                           : "ttbar_dilep_mgmlm_ext1",

            # single top
            "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM" : "stt_antitop_incdec_powheg",
            "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"     : "stt_top_incdec_powheg",
            "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                    : "sts_4f_leptonic_amcnlo",
            "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "sttw_top_nofullhaddecay_powheg",
            "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                    : "sttw_antitop_nofullhaddecay_powheg",
            "/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                                               : "tzq_ll_amcnlo",
            "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                : "sttwll_madgraph",

            # diboson
            "/WZTo3LNu_0Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu0jetmll50_madgraph",
            "/WZTo3LNu_1Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu1jetmll50_madgraph",
            "/WZTo3LNu_2Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu2jetmll50_madgraph",
            "/WZTo3LNu_3Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu3jetmll50_madgraph",
            "/WZTo3LNu_0Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"                     : "wz_3lnu0jetmll4_madgraph",
            "/WZTo3LNu_1Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"                     : "wz_3lnu1jetmll4_madgraph",
            "/WZTo3LNu_2Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"                     : "wz_3lnu2jetmll4_madgraph",
            "/WZTo3LNu_3Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                     : "wz_3lnu3jetmll4_madgraph",
            "/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                              : "ww_2l2nu_powheg",
            "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                              : "ww_lnuqq_powheg",
            "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM"                                      : "wz_lnqq_amcnlo",
            "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                        : "wz_1l3n_amcnlo",
            "/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                  : "wpwpjj_ewk-qcd_madgraph",
            "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                            : "ww_2l2nu_dbl_scat",
            "/EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                    : "Wpjj_lnu_madgraph",
            "/EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                         : "Zjj_m50_madgraph",
            "/EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                   : "Wmjj_lnu_madgraph",
            "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                          : "wz_3lnu_powheg",
            "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                      : "zz_2l2n_powheg",
            "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                         : "zz_2l2q_powheg",
            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                        : "zz_2q2n_amcnlo",
            "/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                         : "zz_4l_powheg",
            # ttV
            "/ttZJets_13TeV_madgraphMLM/RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                                       : "ttz_incl_mgmlm",
            "/ttWJets_13TeV_madgraphMLM/RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                                       : "ttw_incl_mgmlm",
            "/ttHTobb_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                   : "tth_bb_powheg",
            "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                       : "tth_nonbb_powheg",
            # ewk gamma contamination
            "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                     : "wgjets_incl_mgmlm",
            "/WGstarToLNuMuMu_012Jets_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                              : "wgstar_lnmm_012jets_madgraph",
            "/WGstarToLNuEE_012Jets_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                : "wgstar_lnee_012jets_madgraph",
            "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                                : "zgamma_2lG_amc",
            "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                             : "ttg_incl_amcnlo",
            # triboson
            "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                             : "wwz_incl_amcnlo",
            "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                             : "wzz_incl_amcnlo",
            "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                             : "zzz_incl_amcnlo",
            "/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                             : "wzg_incl_amcnlo",
            "/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                                        : "wwg_incl_amcnlo",
            # Higgs
            "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                   : "vh_nonbb_amcnlo",

            # Wjets
            "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                   : "wjets_incl_mgmlm",
            "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                  : "wjets_ht100_mgmlm_ext1",
            "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                  : "wjets_ht200_mgmlm_ext1",
            "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                  : "wjets_ht400_mgmlm_ext1",
            "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                  : "wjets_ht600_mgmlm_ext1",
            "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                 : "wjets_ht800_mgmlm_ext1",
            "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                     : "wjets_ht1200_mgmlm_nonext",
            "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"                 : "wjets_ht2500_mgmlm_ext1",
            # DYToLL
            "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                          : "dy_m1050_mgmlm",
            "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM"                         : "dy_m50_mgmlm_ext1",
            "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"             : "dy_m50_mgmlm_ht100_ext1",
            "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"             : "dy_m50_mgmlm_ht200_ext1",
            "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"             : "dy_m50_mgmlm_ht400_ext1",
            "/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"                  : "dy_m50_mgmlm_ht600_nonext",
            "/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                 : "dy_m50_mgmlm_ht800_nonext",
            "/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                : "dy_m50_mgmlm_ht1200_nonext",
            "/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                 : "dy_m50_mgmlm_ht2500_nonext",

            }

    dinfos["www_2016_80x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "WWW"
            }

    dinfos["pog_2016_80x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "POG"
            }

    dinfos["loose_2016_80x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "Loose"
            }

    dinfos["os_2016_80x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "OS"
            }


    ##########################################
    ######## WWW BABY MC 2017 94x v2 #########
    ##########################################


    sample_info = {

            "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                                          : "www_amcatnlo",
            "/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                           : "www_2l_amcatnlo",
            # "/VBF_WpmWpmJJh-aHTC/PRIVATE_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                                     : "vbf_wpmwpmjjh-aHTC", 
            "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                              : "vh_nonbb_amcatnlo",
            "/VHToNonbb_M125_DiLeptonFilter_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"       : "vh_nonbb_2l_amcatnlo",
            "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                          : "dy_m1050_mgmlm",
            # "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"                        : "dy_m50_amcatnlo",
            "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"              : "dy_m50_madgraph",
            "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM"                              : "wjets_incl_mgmlm",
            "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                       : "wjets_ht100_madgraph",
            "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                       : "wjets_ht200_madgraph",
            "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                       : "wjets_ht400_madgraph",
            "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                       : "wjets_ht600_madgraph",
            "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                      : "wjets_ht800_madgraph",
            "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                     : "wjets_ht1200_madgraph",
            "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"                      : "wjets_ht2500_madgraph",
            "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"  : "singletop_schanlep_amcatnlo",
            "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"    : "tw_antitopnofullhad_powheg",
            "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"        : "tw_topnofullhad_powheg",
            "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"                    : "twz_incl_madgraph",
            "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"                    : "ggh_hzz4l_powheg",
            "/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                  : "vbsww_madgraph",
            "/WW_DoubleScattering_13TeV-pythia8_TuneCP5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                      : "ww_dblsct_pythia",
            "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                                       : "ww_incl_pythia",
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
            "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                     : "wg_lvg_madgraph",
            "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"                             : "wg_lvg_amcatnlo",
            "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"                              : "zg_llg_amcatnlo",
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
            "/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                        : "ttg_dilep_madgraph",
            "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                        : "ttw_lv_amcatnlo",
            "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                         : "ttw_qq_amcatnlo",
            "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                 : "ttz_m1to10ll_amcatnlo",
            "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                : "ttz_llvvm10_amcatnlo",
            "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                         : "ttz_qq_amcatnlo",
            "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"                           : "tth_nonbb_powheg",
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
            # "/VHToWW_M125_13TeV_amcatnloFXFX_madspin_pythia8/PRIVATE_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-ext1-v2/MINIAODSIM"                    : "vh_ww_amcatnlo_private", # Private sample generated by Phil. Restricted to VH->WW but no dilep filter
            # "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/PRIVATE_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                  : "www_amcatnlo_private",   # Private sample generated by Phil. W width not fixed and no dilep filter

            # Not needed
            # "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : "singletop_tbrtchanincl_powheg", # Not sure of the status. Too tiny to care.
            # "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     : "singletop_toptchanincl_powheg", # Not sure of the status. Too tiny to care.
            # "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"                            : "wz_3lv_amcatnlo",
            # "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"                                                       : "wz_incl_pythia",
            # "/WZTo3LNu_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"                                                  : "wz_3lv_powheg",

            }

    dinfos["www_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "WWW"
            }

    dinfos["www3l_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "WWW3L"
            }

    dinfos["loose_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "Loose"
            }

    dinfos["os_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "OS"
            }

    dinfos["vvv_2017_94x_v2"] = {
            "samples" : sample_info,
            "year" : 2017,
            "baby_type" : "VVV"
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
            "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"            : "qcd_pt20_bctoe",
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

    ########################################
    ######## WWW BABY MC 2018 102x #########
    ########################################

    sample_info = {

        # "/EGamma/Run2018A-PromptReco-v1/MINIAOD": "data_Run2018Av1_ee",
        # "/EGamma/Run2018A-PromptReco-v2/MINIAOD": "data_Run2018Av2_ee",
        # "/EGamma/Run2018A-PromptReco-v3/MINIAOD": "data_Run2018Av3_ee",
        # "/EGamma/Run2018B-PromptReco-v1/MINIAOD": "data_Run2018Bv1_ee",
        # "/EGamma/Run2018B-PromptReco-v2/MINIAOD": "data_Run2018Bv2_ee",
        # "/EGamma/Run2018C-PromptReco-v1/MINIAOD": "data_Run2018Cv1_ee",
        # "/EGamma/Run2018C-PromptReco-v2/MINIAOD": "data_Run2018Cv2_ee",
        # "/EGamma/Run2018C-PromptReco-v3/MINIAOD": "data_Run2018Cv3_ee",
        # "/EGamma/Run2018D-PromptReco-v2/MINIAOD": "data_Run2018Dv2_ee",
        "/EGamma/Run2018D-22Jan2019-v2/MINIAOD": "data_Run2018Dv2_ee_reproc",
        # "/DoubleMuon/Run2018A-PromptReco-v1/MINIAOD": "data_Run2018Av1_mm",
        # "/DoubleMuon/Run2018A-PromptReco-v2/MINIAOD": "data_Run2018Av2_mm",
        # "/DoubleMuon/Run2018A-PromptReco-v3/MINIAOD": "data_Run2018Av3_mm",
        # "/DoubleMuon/Run2018B-PromptReco-v1/MINIAOD": "data_Run2018Bv1_mm",
        # "/DoubleMuon/Run2018B-PromptReco-v2/MINIAOD": "data_Run2018Bv2_mm",
        # "/DoubleMuon/Run2018C-PromptReco-v1/MINIAOD": "data_Run2018Cv1_mm",
        # "/DoubleMuon/Run2018C-PromptReco-v2/MINIAOD": "data_Run2018Cv2_mm",
        # "/DoubleMuon/Run2018C-PromptReco-v3/MINIAOD": "data_Run2018Cv3_mm",
        "/DoubleMuon/Run2018D-PromptReco-v2/MINIAOD": "data_Run2018Dv2_mm",
        # "/MuonEG/Run2018A-PromptReco-v1/MINIAOD": "data_Run2018Av1_em",
        # "/MuonEG/Run2018A-PromptReco-v2/MINIAOD": "data_Run2018Av2_em",
        # "/MuonEG/Run2018A-PromptReco-v3/MINIAOD": "data_Run2018Av3_em",
        # "/MuonEG/Run2018B-PromptReco-v1/MINIAOD": "data_Run2018Bv1_em",
        # "/MuonEG/Run2018B-PromptReco-v2/MINIAOD": "data_Run2018Bv2_em",
        # "/MuonEG/Run2018C-PromptReco-v1/MINIAOD": "data_Run2018Cv1_em",
        # "/MuonEG/Run2018C-PromptReco-v2/MINIAOD": "data_Run2018Cv2_em",
        # "/MuonEG/Run2018C-PromptReco-v3/MINIAOD": "data_Run2018Cv3_em",
        "/MuonEG/Run2018D-PromptReco-v2/MINIAOD": "data_Run2018Dv2_em",

        # Rereco
        "/EGamma/Run2018A-17Sep2018-v2/MINIAOD": "data_Run2018Av2_ee",
        "/EGamma/Run2018B-17Sep2018-v1/MINIAOD": "data_Run2018Bv1_ee",
        "/EGamma/Run2018C-17Sep2018-v1/MINIAOD": "data_Run2018Cv1_ee",
        "/DoubleMuon/Run2018A-17Sep2018-v2/MINIAOD": "data_Run2018Av2_mm",
        "/DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD": "data_Run2018Bv1_mm",
        "/DoubleMuon/Run2018C-17Sep2018-v1/MINIAOD": "data_Run2018Cv1_mm",
        "/MuonEG/Run2018A-17Sep2018-v1/MINIAOD": "data_Run2018Av1_em",
        "/MuonEG/Run2018B-17Sep2018-v1/MINIAOD": "data_Run2018Bv1_em",
        "/MuonEG/Run2018C-17Sep2018-v1/MINIAOD": "data_Run2018Cv1_em",
        "/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                     : "www_amcatnlo_dilepfilter",
        "/VHToNonbb_M125_DiLeptonFilter_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" : "vh_nonbb_amcatnlo_dilepfilter",
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                               : "www_amcatnlo"               ,
        "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                        : "vh_nonbb_amcatnlo"          ,
        "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                    : "dy_m1050_madgraph"          ,
        "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                        : "dy_m50_madgraph"            ,
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                             : "wjets_incl_madgraph"        ,
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                 : "wjets_ht100_madgraph"       ,
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                 : "wjets_ht200_madgraph"       ,
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                 : "wjets_ht400_madgraph"       ,
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                 : "wjets_ht600_madgraph"       ,
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                : "wjets_ht800_madgraph"       ,
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"               : "wjets_ht1200_madgraph"      ,
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                : "wjets_ht2500_madgraph"      ,
        "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4/MINIAODSIM"         : "sts_4f_leptonic_madgraph"   ,
        # ST t-channel top
        # ST t-channel anti-top
        "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"              : "twz_ll_madgraph"            ,
        "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM" : "tw_antitopnofullhad_powheg" ,
        "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM"     : "tw_topnofullhad_powheg"     ,
        "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                   : "ggh_hzz4l_powheg"           ,
        "/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                            : "vbsww_madgraph"             ,
        "/WW_DoubleScattering_13TeV-pythia8_TuneCP5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"                           : "ww_dblsct_pythia"           ,
        "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                                                 : "ww_incl_pythia"             ,
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                         : "wz_3lv_amcatnlo"            ,
        "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"                                                 : "wz_incl_pythia"             ,
        # WZ 1L1Nu2Q
        # WZ 1L3Nu
        # WZ 2L2Q
        # WZ 3LNu 0
        # WZ 3LNu 0
        # WZ 3LNu 1
        # WZ 3LNu 1
        # WZ 3LNu 2
        # WZ 3LNu 2
        # WZ 3LNu 3
        # WZ 3LNu 3
        # WZ 3LNu powheg
        # "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v2/MINIAODSIM"                                 : "zz_4l_powheg"               ,
        "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                                                 : "zz_incl_pythia"             ,
        "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                  : "wwz_amcatnlo"               ,
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                  : "wzz_amcatnlo"               ,
        "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                                       : "wzg_amcatnlo"               ,
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                  : "zzz_amcatnlo"               ,
        "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                 : "ttbar_1ltop_madgraph"       ,
        "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"              : "ttbar_1ltbr_madgraph"       ,
        "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                                   : "ttbar_dilep_powheg"         ,
        "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                          : "ttbar_dilep_madgraph"       ,
        "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                            : "ttbar_semilep_powheg"       ,
        "/TTGamma_SingleLeptFromT_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"              : "ttgam_1ltop_madgraph"       ,
        "/TTGamma_SingleLeptFromTbar_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"           : "ttgam_1ltbr_madgraph"       ,
        "/TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                       : "ttgam_dilep_madgraph"       ,
        "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"             : "ttw_lnu_amcatnlo"           ,
        #/TTWJetsToQQ
        "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                           : "ttz_ll_mll1_amcatnlo"       ,
        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                     : "ttz_llvv_mll10_amcatnlo"    ,
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                             : "tth_nonbb_powheg"           ,
        #/TTZToQQ
        "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                    : "tZq_ll_madgraph"            ,
        "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                  : "wwg_amcatnlo"               ,

        "/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                  : "tgjets_lepdecay_madgraph"   ,
        "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"                  : "wg_lnug_amcatnlo"           ,
        "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"                               : "wg_lnug_madgraph"           ,
        "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                   : "zg_llg_amcatnlo"            ,

        # "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                                                 : "ZZincl"                   ,
        # "/TTPlus1Jet_DiLept_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                : "TTdilep1jet"              ,
        # "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                            : "TTdilep0jet"              ,
        # "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"          : "TTHtoNonBB"               ,
        # "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTTTnew"                  ,
        # "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTHH"                     ,
        # "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTWZ"                     ,
        # "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTZZ"                     ,
        # "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTTW"                     ,
        # "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTTJ"                     ,
        # "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTWH"                     ,
        # "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTZH"                     ,
        # "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"                                 : "TTWW"                     ,


        }

    dinfos["www_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "WWW"
            }

    dinfos["www3l_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "WWW3L"
            }

    dinfos["loose_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "Loose"
            }

    dinfos["os_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "OS"
            }

    dinfos["vvv_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "VVV"
            }


    ##########################################
    ######## FR BABY MC 2018 102x v2 #########
    ##########################################

    sample_info = {

            "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"            : "dy_m50_madgraph",
            "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"               : "ttbar_incl_amcatnlo",
            "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                 : "wjets_incl_madgraph",
            "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"                                     : "ww_incl_pythia",
            "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"                                     : "wz_incl_pythia",
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
            "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "ttbar_1ltop_madgraph",
            "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"  : "ttbar_1ltbr_madgraph",
            "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"              : "ttbar_dilep_madgraph",
            "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht100_madgraph",
            "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht200_madgraph",
            "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht400_madgraph",
            "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"     : "wjets_ht600_madgraph",
            "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"    : "wjets_ht800_madgraph",
            "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"   : "wjets_ht1200_madgraph",
            "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"    : "wjets_ht2500_madgraph",
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

    dinfos["fr_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "FR"
            }


    ###########################################
    ######## TnP BABY MC 2018 102x v2 #########
    ###########################################

    sample_info = {

            "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"            : "dy_m50_madgraph",
            "/EGamma/Run2018A-17Sep2018-v2/MINIAOD": "data_Run2018Av2_se",
            "/EGamma/Run2018B-17Sep2018-v1/MINIAOD": "data_Run2018Bv1_se",
            "/EGamma/Run2018C-17Sep2018-v1/MINIAOD": "data_Run2018Cv1_se",
            # "/EGamma/Run2018D-PromptReco-v2/MINIAOD": "data_Run2018Dv2_se",
            "/EGamma/Run2018D-22Jan2019-v2/MINIAOD": "data_Run2018Dv2_ee_reproc",
            "/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD": "data_Run2018Av2_sm",
            "/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD": "data_Run2018Bv1_sm",
            "/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD": "data_Run2018Cv1_sm",
            "/SingleMuon/Run2018D-PromptReco-v2/MINIAOD": "data_Run2018Dv2_sm",
            "/MET/Run2018A-17Sep2018-v1/MINIAOD": "data_Run2018Av1_xe",
            "/MET/Run2018B-17Sep2018-v1/MINIAOD": "data_Run2018Bv1_xe",
            "/MET/Run2018C-17Sep2018-v1/MINIAOD": "data_Run2018Cv1_xe",
            "/MET/Run2018D-PromptReco-v1/MINIAOD": "data_Run2018Dv1_xe",
            "/MET/Run2018D-PromptReco-v2/MINIAOD": "data_Run2018Dv2_xe",

            }

    dinfos["tnp_2018_102x"] = {
            "samples" : sample_info,
            "year" : 2018,
            "baby_type" : "TnP"
            }

    sample_info = {

            ###############################################################################
            # CMS4
            ###############################################################################
            # Data
            #"/DoubleEG/Run2016B-17Jul2018_ver1-v1/MINIAOD"   : "data_Run2016Bv1_ee" , 
            "/DoubleEG/Run2016B-17Jul2018_ver2-v1/MINIAOD"   : "data_Run2016Bv2_ee" , 
            "/DoubleEG/Run2016C-17Jul2018-v1/MINIAOD"        : "data_Run2016C_ee"   , 
            "/DoubleEG/Run2016D-17Jul2018-v1/MINIAOD"        : "data_Run2016D_ee"   , 
            "/DoubleEG/Run2016E-17Jul2018-v1/MINIAOD"        : "data_Run2016E_ee"   , 
            "/DoubleEG/Run2016F-17Jul2018-v1/MINIAOD"        : "data_Run2016F_ee"   , 
            "/DoubleEG/Run2016G-17Jul2018-v1/MINIAOD"        : "data_Run2016G_ee"   , 
            "/DoubleEG/Run2016H-17Jul2018-v1/MINIAOD"        : "data_Run2016H_ee"   , 
            #"/DoubleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD" : "data_Run2016Bv1_mm" , 
            "/DoubleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD" : "data_Run2016Bv2_mm" , 
            "/DoubleMuon/Run2016C-17Jul2018-v1/MINIAOD"      : "data_Run2016C_mm"   , 
            "/DoubleMuon/Run2016D-17Jul2018-v1/MINIAOD"      : "data_Run2016D_mm"   , 
            "/DoubleMuon/Run2016E-17Jul2018-v1/MINIAOD"      : "data_Run2016E_mm"   , 
            "/DoubleMuon/Run2016F-17Jul2018-v1/MINIAOD"      : "data_Run2016F_mm"   , 
            "/DoubleMuon/Run2016G-17Jul2018-v1/MINIAOD"      : "data_Run2016G_mm"   , 
            "/DoubleMuon/Run2016H-17Jul2018-v1/MINIAOD"      : "data_Run2016H_mm"   , 
            #"/MuonEG/Run2016B-17Jul2018_ver1-v1/MINIAOD"     : "data_Run2016Bv1_em" , 
            "/MuonEG/Run2016B-17Jul2018_ver2-v1/MINIAOD"     : "data_Run2016Bv2_em" , 
            "/MuonEG/Run2016C-17Jul2018-v1/MINIAOD"          : "data_Run2016C_em"   , 
            "/MuonEG/Run2016D-17Jul2018-v1/MINIAOD"          : "data_Run2016D_em"   , 
            "/MuonEG/Run2016E-17Jul2018-v2/MINIAOD"          : "data_Run2016E_em"   , # note , v2 due to email titled [ops] Reprocessing 2017 94X with MET Recipe"
            "/MuonEG/Run2016F-17Jul2018-v1/MINIAOD"          : "data_Run2016F_em"   , 
            "/MuonEG/Run2016G-17Jul2018-v1/MINIAOD"          : "data_Run2016G_em"   , 
            "/MuonEG/Run2016H-17Jul2018-v1/MINIAOD"          : "data_Run2016H_em"   , 

            # Signal
            "/WWW_4F_DiLeptonFilter_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM"                                          : "www_2l_amcatnlo",
            "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                         : "www_incl_amcatnlo",

            # ttbar
            "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                 : "ttbar_1ltop_mgmlm_ext1",
            "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                              : "ttbar_1ltbr_mgmlm_ext1",
            "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                               : "ttbar_dilep_mgmlm_ext1",

            # single top
            "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                : "stt_antitop_incdec_powheg",
            "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                    : "stt_top_incdec_powheg",
            "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                   : "sts_4f_leptonic_amcnlo",
            "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                  : "sttw_top_nofullhaddecay_powheg",
            "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                              : "sttw_antitop_nofullhaddecay_powheg",
            "/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"                                                              : "tzq_ll_amcnlo",
            "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                                               : "sttwll_madgraph",

            # diboson
            # "/WZTo3LNu_0Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu0jetmll50_madgraph",
            # "/WZTo3LNu_1Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu1jetmll50_madgraph",
            # "/WZTo3LNu_2Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu2jetmll50_madgraph",
            # "/WZTo3LNu_3Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                        : "wz_3lnu3jetmll50_madgraph",
            # "/WZTo3LNu_0Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"                     : "wz_3lnu0jetmll4_madgraph",
            # "/WZTo3LNu_1Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"                     : "wz_3lnu1jetmll4_madgraph",
            # "/WZTo3LNu_2Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"                     : "wz_3lnu2jetmll4_madgraph",
            # "/WZTo3LNu_3Jets_MLL-4To50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                     : "wz_3lnu3jetmll4_madgraph",
            "/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                                             : "ww_2l2nu_powheg",
            "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                                             : "ww_lnuqq_powheg",
            "/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                                 : "wpwpjj_ewk-qcd_madgraph",
            "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                           : "ww_2l2nu_dbl_scat",
            # "/EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                    : "Wpjj_lnu_madgraph",
            # "/EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                         : "Zjj_m50_madgraph",
            # "/EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                   : "Wmjj_lnu_madgraph",
            "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                     : "wz_lnqq_amcatnlo",
            "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                       : "wz_1l3n_amcatnlo",
            "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                        : "wz_2l2q_amcatnlo",
            "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                   : "wz_3lnu_amcatnlo",
            "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                                     : "zz_2l2n_powheg",
            "/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                                      : "zz_2l2q_powheg",
            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                       : "zz_2q2n_amcnlo",
            "/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                                                        : "zz_4l_powheg",
            # ttV
            "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM"                                          : "ttz_llvv_mll10_amcatnlo",
            "/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                                         : "ttz_ll_mll1_madgraph",
            "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM"                                  : "ttw_incl_mgmlm",
            # "/ttHTobb_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                   : "tth_bb_powheg",
            "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                      : "tth_nonbb_powheg",
            # ewk gamma contamination
            "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"                                              : "wgjets_incl_amcnlo",
            # "/WGstarToLNuMuMu_012Jets_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                              : "wgstar_lnmm_012jets_madgraph",
            # "/WGstarToLNuEE_012Jets_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"                                                : "wgstar_lnee_012jets_madgraph",
            "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"                                               : "zgamma_2lG_amc",
            "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                       : "ttg_incl_amcnlo",
            # triboson
            "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                            : "wwz_incl_amcnlo",
            "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                            : "wzz_incl_amcnlo",
            "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                            : "zzz_incl_amcnlo",
            "/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                                            : "wzg_incl_amcnlo",
            "/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"                                                       : "wwg_incl_amcnlo",
            # Higgs
            "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                  : "vh_nonbb_amcnlo",

            # Wjets
            "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM"                                             : "wjets_incl_mgmlm",
            # "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                      : "wjets_ht100_mgmlm_ext1",
            # "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM"                                 : "wjets_ht200_mgmlm_ext1",
            # "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                 : "wjets_ht400_mgmlm_ext1",
            # "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                 : "wjets_ht600_mgmlm_ext1",
            # "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                : "wjets_ht800_mgmlm_ext1",
            # "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                               : "wjets_ht1200_mgmlm_nonext",
            # "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                     : "wjets_ht2500_mgmlm_ext1",
            # DYToLL
            "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                                   : "dy_m1050_amcatnlo",
            "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM"                                       : "dy_m50_amcatnlo",
            # "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                            : "dy_m50_mgmlm_ht100_ext1",
            # "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                 : "dy_m50_mgmlm_ht200_ext1",
            # "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"                            : "dy_m50_mgmlm_ht400_ext1",
            # "/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                 : "dy_m50_mgmlm_ht600_nonext",
            # "/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                : "dy_m50_mgmlm_ht800_nonext",
            # "/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                               : "dy_m50_mgmlm_ht1200_nonext",
            # "/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                                : "dy_m50_mgmlm_ht2500_nonext",

            }

    dinfos["www_2016_94x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "WWW"
            }

    dinfos["www3l_2016_94x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "WWW3L"
            }

    dinfos["loose_2016_94x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "Loose"
            }

    dinfos["vvv_2016_94x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "VVV"
            }

    sample_info = {
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

            "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM"          : "dy_m50_amcatnlo",
            "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"                         : "ttbar_incl_madgraph",
            "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM"                : "wjets_incl_mgmlm",

            "/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                : "ww_2l2nu_powheg",
            "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                                                : "ww_lnuqq_powheg",
            "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                        : "wz_lnqq_amcatnlo",
            "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                          : "wz_1l3n_amcatnlo",
            "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                           : "wz_2l2q_amcatnlo",
            "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                      : "wz_3lnu_amcatnlo",
            "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    : "ttbar_1ltop_mgmlm_ext1",
            "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM" : "ttbar_1ltbr_mgmlm_ext1",
            "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"                  : "ttbar_dilep_mgmlm_ext1",
            "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"         : "wjets_ht100_mgmlm_ext1",
            "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM"    : "wjets_ht200_mgmlm_ext1",
            "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    : "wjets_ht400_mgmlm_ext1",
            "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    : "wjets_ht600_mgmlm_ext1",
            "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"   : "wjets_ht800_mgmlm_ext1",
            # "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"  : "wjets_ht1200_mgmlm_nonext",
            # "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"        : "wjets_ht2500_mgmlm_ext1",

            "/DoubleEG/Run2016B-17Jul2018_ver2-v1/MINIAOD"   : "data_Run2016Bv2_ee" , 
            "/DoubleEG/Run2016C-17Jul2018-v1/MINIAOD"        : "data_Run2016C_ee"   , 
            "/DoubleEG/Run2016D-17Jul2018-v1/MINIAOD"        : "data_Run2016D_ee"   , 
            "/DoubleEG/Run2016E-17Jul2018-v1/MINIAOD"        : "data_Run2016E_ee"   , 
            "/DoubleEG/Run2016F-17Jul2018-v1/MINIAOD"        : "data_Run2016F_ee"   , 
            "/DoubleEG/Run2016G-17Jul2018-v1/MINIAOD"        : "data_Run2016G_ee"   , 
            "/DoubleEG/Run2016H-17Jul2018-v1/MINIAOD"        : "data_Run2016H_ee"   , 
            "/DoubleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD" : "data_Run2016Bv2_mm" , 
            "/DoubleMuon/Run2016C-17Jul2018-v1/MINIAOD"      : "data_Run2016C_mm"   , 
            "/DoubleMuon/Run2016D-17Jul2018-v1/MINIAOD"      : "data_Run2016D_mm"   , 
            "/DoubleMuon/Run2016E-17Jul2018-v1/MINIAOD"      : "data_Run2016E_mm"   , 
            "/DoubleMuon/Run2016F-17Jul2018-v1/MINIAOD"      : "data_Run2016F_mm"   , 
            "/DoubleMuon/Run2016G-17Jul2018-v1/MINIAOD"      : "data_Run2016G_mm"   , 
            "/DoubleMuon/Run2016H-17Jul2018-v1/MINIAOD"      : "data_Run2016H_mm"   , 

            }

    dinfos["fr_2016_94x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "FR"
            }

    sample_info = {
            "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM"          : "dy_m50_amcatnlo",
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
            "/MET/Run2016B-17Jul2018_ver2-v1/MINIAOD"            : "data_Run2016B_xe",
            "/MET/Run2016C-17Jul2018-v1/MINIAOD"                 : "data_Run2016C_xe",
            "/MET/Run2016D-17Jul2018-v1/MINIAOD"                 : "data_Run2016D_xe",
            "/MET/Run2016E-17Jul2018-v1/MINIAOD"                 : "data_Run2016E_xe",
            "/MET/Run2016F-17Jul2018-v1/MINIAOD"                 : "data_Run2016F_xe",
            "/MET/Run2016G-17Jul2018-v1/MINIAOD"                 : "data_Run2016G_xe",
            "/MET/Run2016H-17Jul2018-v2/MINIAOD"                 : "data_Run2016H_xe",
            }

    dinfos["tnp_2016_94x"] = {
            "samples" : sample_info,
            "year" : 2016,
            "baby_type" : "TnP"
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
    if "WWW2016" in args.sample_sets:
        master_list["www_2016_94x"] = grand_master_list["www_2016_94x"]
    if "WWW2017" in args.sample_sets:
        master_list["www_2017_94x_v2"] = grand_master_list["www_2017_94x_v2"]
    if "WWW2018" in args.sample_sets:
        master_list["www_2018_102x"] = grand_master_list["www_2018_102x"]

    if "WWW3L2016" in args.sample_sets:
        master_list["www3l_2016_94x"] = grand_master_list["www3l_2016_94x"]
    if "WWW3L2017" in args.sample_sets:
        master_list["www3l_2017_94x_v2"] = grand_master_list["www3l_2017_94x_v2"]
    if "WWW3L2018" in args.sample_sets:
        master_list["www3l_2018_102x"] = grand_master_list["www3l_2018_102x"]

    if "VVV2016" in args.sample_sets:
        master_list["vvv_2016_94x"] = grand_master_list["vvv_2016_94x"]
    if "VVV2017" in args.sample_sets:
        master_list["vvv_2017_94x_v2"] = grand_master_list["vvv_2017_94x_v2"]
    if "VVV2018" in args.sample_sets:
        master_list["vvv_2018_102x"] = grand_master_list["vvv_2018_102x"]

    if "Loose2016" in args.sample_sets:
        master_list["loose_2016_94x"] = grand_master_list["loose_2016_94x"]
    if "Loose2017" in args.sample_sets:
        master_list["loose_2017_94x_v2"] = grand_master_list["loose_2017_94x_v2"]
    if "Loose2018" in args.sample_sets:
        master_list["loose_2018_102x"] = grand_master_list["loose_2018_102x"]

    if "OS2016" in args.sample_sets:
        master_list["os_2016_80x"] = grand_master_list["os_2016_80x"]
    if "OS2017" in args.sample_sets:
        master_list["os_2017_94x_v2"] = grand_master_list["os_2017_94x_v2"]
    if "OS2018" in args.sample_sets:
        master_list["os_2018_102x"] = grand_master_list["os_2018_102x"]

    # FIXME: TODO: ADD 2016 FAKERATE SAMPLES
    # if "FR2016" in args.sample_sets:
    #     master_list["os_2016_80x"] = grand_master_list["os_2016_80x"]
    if "FR2016" in args.sample_sets:
        master_list["fr_2016_94x"] = grand_master_list["fr_2016_94x"]
    if "FR2017" in args.sample_sets:
        master_list["fr_2017_94x_v2"] = grand_master_list["fr_2017_94x_v2"]
    if "FR2018" in args.sample_sets:
        master_list["fr_2018_102x"] = grand_master_list["fr_2018_102x"]

    if "TnP2016" in args.sample_sets:
        master_list["tnp_2016_94x"] = grand_master_list["tnp_2016_94x"]
    if "TnP2017" in args.sample_sets:
        master_list["tnp_2017_94x_v2"] = grand_master_list["tnp_2017_94x_v2"]
    if "TnP2018" in args.sample_sets:
        master_list["tnp_2018_102x"] = grand_master_list["tnp_2018_102x"]

    # If submitting a single sample
    if "SingleSample" in args.sample_sets:
        master_list["single_sample"] = {
            "samples" : {args.single_sample_sample_name:args.single_sample_sample_nicename},
            "year" : int(args.single_sample_sample_year),
            "baby_type" : args.single_sample_sample_babytype
            }

    submit(master_list, args.tag, dotestrun=args.test)

#eof
