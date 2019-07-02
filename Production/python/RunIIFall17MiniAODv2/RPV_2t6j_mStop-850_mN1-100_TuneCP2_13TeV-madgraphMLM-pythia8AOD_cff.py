import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/44F0D9BC-48C0-E811-86D3-90E2BAD1BDF0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2E0D0F47-9BC0-E811-8E89-44A842BE7718.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E2D8871C-41C0-E811-8895-008CFAC8DA30.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/38EEB64F-9BC0-E811-B861-0CC47A2B0744.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8C04CE1B-3FC0-E811-B4E5-5065F381E1A1.root',
] )












