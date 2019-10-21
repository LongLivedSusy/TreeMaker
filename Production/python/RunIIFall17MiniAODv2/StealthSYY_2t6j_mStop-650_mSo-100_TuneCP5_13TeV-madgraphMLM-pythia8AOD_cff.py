import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B26CFC2D-53AB-E811-8EB2-0090FAA57B10.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/88681184-27A9-E811-98B9-A4BF01158CF8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D66C6041-1CAB-E811-B05F-0CC47A57D136.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/0417BBAE-53AB-E811-AC22-002590D8C7E2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/1C163056-4CA7-E811-923C-001E677925A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/6E2F2616-99A7-E811-98BE-A4BF0112BC5C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/AC9C51D1-9DA7-E811-8EE0-A4BF011258D8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CAA27232-53AB-E811-A9FC-0025905C53F2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/5EE96E00-54AB-E811-A9CD-5065F381F202.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/2CD93819-54AB-E811-97F4-842B2B689031.root',
] )




























