import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D6023223-C595-E811-B30D-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/74DEAE35-0A98-E811-9731-002481DE4BF0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6E947735-0A98-E811-AF12-001F29087EFC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6A704DEC-1997-E811-A520-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E28E96B4-4497-E811-976A-A0369F8363BE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/26B08DA2-E196-E811-A9F3-1866DAEA6D0C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A07CA1AB-0998-E811-9750-0025905C3DCE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A42650E9-3897-E811-B44C-A4BF0112BD5E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/9A76BF75-0A98-E811-B70B-002590DBDFF4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3E7CFC87-C697-E811-9879-A4BF011254F0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/9EBAEDD0-3898-E811-BE1D-A4BF0112BE48.root',
] )



































