import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/CCEDCDC0-CAA2-E811-B610-3CFDFE63D380.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A060C95A-CBA2-E811-82CC-3CFDFE639B40.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/202267F7-0CA4-E811-9E15-7CD30AD08E7E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1E6052F9-99A7-E811-ACAC-0025905B855A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/98D429A1-80A8-E811-8930-FA163E3593E9.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/14705496-76A8-E811-97EE-FA163EE8C7E8.root',
] )


























