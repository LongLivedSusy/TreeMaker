import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/BC98842C-7DBF-E811-92AA-34E6D7BEAF28.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/4A7BE48B-99BE-E811-804A-EC0D9A8222DE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/681EE699-A0BE-E811-A4D5-24BE05C3CBD1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/4E5AD18C-7CBF-E811-9AD0-E0071B6C9DD0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/12567B2C-7DBF-E811-829A-1866DA890879.root',
] )






