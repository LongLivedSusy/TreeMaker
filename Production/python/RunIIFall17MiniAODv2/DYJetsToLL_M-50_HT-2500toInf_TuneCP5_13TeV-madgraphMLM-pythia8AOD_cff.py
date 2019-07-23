import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/14484F99-60EE-E711-95E6-FA163EA9DF9D.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9265F235-CAEF-E711-A9C2-FA163E846A8C.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1AF080E5-C9EF-E711-80B8-FA163EFC03C4.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/EC65D548-FFEC-E711-948C-FA163EC31E4B.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/06CAEB40-4FED-E711-9FA0-FA163E23DFA5.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/329D9EEE-FEEC-E711-BC62-FA163E53B320.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1E51843B-4FED-E711-BCF6-FA163E6F1BDB.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7C560E9D-50ED-E711-BE72-FA163E36AD00.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3ECF7A4F-65ED-E711-AA24-FA163E8FF367.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/789E0A2F-65ED-E711-8FCC-FA163EA010B6.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AE977612-EBED-E711-A9E1-FA163E43E730.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7E843AD2-91ED-E711-9E06-FA163E1EB77F.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FCD9EAD5-91ED-E711-8E0B-FA163EEE5935.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/525D00CE-91ED-E711-8467-FA163E86F545.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/80F408EC-FAED-E711-9938-FA163E2087CD.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AEA06B18-FBED-E711-8354-FA163E528057.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FCD57D5C-F9ED-E711-BCAD-FA163E6E88E3.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E0FC1C57-27EE-E711-8981-FA163E2EA817.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/28F9EB1C-F9ED-E711-8659-FA163E29BD8D.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1076EF9B-A2EE-E711-A32C-FA163E354557.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/4CE24797-60EE-E711-ACD7-FA163E6C9315.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3C012389-A2EE-E711-A76E-FA163EA4BE23.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E85C665C-A2EE-E711-94E1-FA163E434C8E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A899D17D-F0EE-E711-8ED4-FA163E875D55.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9699618A-A2EE-E711-A3AF-FA163E433120.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/26FEBD89-A2EE-E711-9039-FA163E5CAD01.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/CA261498-C9F5-E711-AB98-FA163E6151E6.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C8886B0E-96F6-E711-9053-0CC47A2B04A6.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/DAC54A0D-96F6-E711-87FF-0026B9277A3F.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E68DC191-CBF6-E711-88D3-A4BF010F0E26.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/4625DA9B-93F6-E711-81DD-7845C4F91633.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/CCC26E6D-E8EF-E711-B4CA-FA163EF16BA8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/52356DA6-CBF5-E711-93DF-E0071B7A08F0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D6524B07-CDF5-E711-BC68-E0071B7A6850.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/40CA92E7-DFF7-E711-8031-0025905A6110.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/109531DC-99F6-E711-8F0C-6CC2173C3E80.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/8AE51441-90F7-E711-8B4A-0CC47A1DF7F2.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E42529B7-89F7-E711-883D-008CFAF754BE.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/00000/2C4F2D67-51FB-E711-A6CD-E0071B691B81.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/145A7879-AAF2-E711-A3F9-FA163E14A423.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A8C9A75E-1EF3-E711-A043-FA163EE07187.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/88E62536-96F6-E711-8C16-141877411C7F.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7CC37E52-9BF6-E711-9E5E-14187763B750.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F8360A52-C1F6-E711-BC5E-7CD30AC036FE.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/DC5E209C-CDF6-E711-9EAF-0242AC1C0500.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/B03DFD9A-4405-E811-863D-FA163EB6AB2F.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/804A5C23-2F06-E811-B9A8-FA163EBEAB66.root',
] )



















