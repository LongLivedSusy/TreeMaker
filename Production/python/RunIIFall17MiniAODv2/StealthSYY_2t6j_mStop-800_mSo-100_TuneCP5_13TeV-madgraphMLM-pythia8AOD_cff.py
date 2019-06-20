import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/EC9C1A3D-0396-E811-9FCD-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B208375E-D496-E811-AFA0-02163E00BF91.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/767140DB-C795-E811-856D-0CC47A13D3B2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B26CC443-9996-E811-AE4E-549F3525D084.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/488355BF-9897-E811-88D3-047D7B10618E.root',
] )







