import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9EC4C7D7-809C-E811-B318-0CC47A4D767C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/046E2AD1-929C-E811-9436-0CC47A4D7614.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BC980948-959D-E811-A233-0CC47A7C345E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8017F093-D99D-E811-955B-00259048AC76.root',
] )














