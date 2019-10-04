import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4CDC8532-8BA4-E811-80E7-0CC47AD99112.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/00643907-8BA4-E811-BF84-24BE05CE1E01.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/F2074559-CBA2-E811-B157-3CFDFE634F80.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/0ADED26B-13A4-E811-A221-509A4C74D09C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1C930C11-13A4-E811-AEF8-509A4C74D077.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/560556A4-77A2-E811-9D85-24BE05C668E1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/FCD7D14F-B0AB-E811-9C1E-509A4C74D0CD.root',
] )

























