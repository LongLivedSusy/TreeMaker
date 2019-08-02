import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C82046A8-9CBA-E811-9FC1-246E96D10E64.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F0B62AD8-9CBA-E811-909B-246E96D74858.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6224B9A2-50BA-E811-91F0-24BE05CEFDF1.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7E17AF3D-88BA-E811-BF49-24BE05CECB51.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/009A2284-6FBA-E811-B772-24BE05CECB71.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F20AAD41-B4BB-E811-88C5-001E67DDBFF7.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/44E1DB28-84BC-E811-8193-A4BF01026229.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CE8A840A-91BF-E811-9CA1-6C3BE5B580C8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/662A5685-7BBF-E811-BCEA-44A84223FF3C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/74017667-A3BF-E811-AF23-BC305B390A8D.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/9E01BD93-7ABE-E811-9E73-0090FAA578F0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FED787AE-99BF-E811-8AC7-002590908236.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/DC1565C6-5BBF-E811-86FA-002481CFE834.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/689EE6BC-EEBD-E811-942C-008CFAC9429C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BE4EED02-81BF-E811-9D5A-B496910A8AC0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1AC27B60-C1BE-E811-8CCE-44A842BFA958.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5AABEF8B-DABE-E811-BF3D-0CC47A2B0214.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E04A5863-7ABE-E811-AFC6-0CC47AD98A92.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3C4EE3D4-22BF-E811-8030-001E67E71BAA.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/80C2EA17-98BF-E811-BF63-008CFAF2224C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/84C3E3F1-97BF-E811-9901-0025905C9724.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4A5DCEAA-CCBE-E811-819D-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6241A0EC-EFBD-E811-A737-001E67580724.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A458C9E8-48BE-E811-9D90-901B0E6459DE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/02CFFC87-97BE-E811-9856-AC1F6B0DE2EC.root',
] )





















