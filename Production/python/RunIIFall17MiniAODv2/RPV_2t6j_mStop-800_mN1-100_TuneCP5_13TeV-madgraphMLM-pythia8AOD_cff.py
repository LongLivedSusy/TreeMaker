import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/16067103-E49B-E811-B2E5-0CC47A5FA3BD.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2EFC8DE2-E39B-E811-A9A3-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/22A1C519-6E9B-E811-832C-00266CFFBEB4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/80A763BF-259B-E811-AF03-5065F38182E1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E43F5639-E49B-E811-A195-24BE05BD4F61.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AA0570CB-E39B-E811-B7A9-0CC47A4D767E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4AF74626-38C0-E811-8B14-0242AC1C0500.root',
] )



















