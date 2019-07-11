import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/180331B1-8F9C-E811-8D31-0CC47A4C8EBA.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9C45E9BB-ED9B-E811-9FC7-0CC47A7EEE1E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CACB62B1-B19B-E811-A26B-9CDC715FC770.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8436659B-AF9B-E811-88BF-5065F37D6172.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/84221FCE-119D-E811-8B65-001E6779279A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/ACA18671-B59C-E811-AAA6-0026B94DBDFD.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3899726B-B59C-E811-9917-AC1F6B1B2392.root',
] )















