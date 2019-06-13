import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/EE865088-A7CA-E811-8F1E-B083FED16468.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/E8487A52-A7CA-E811-ACE1-EC0D9A822616.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/4A378E6F-A8CA-E811-BFDF-0026B9278685.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/02D61FE1-75CB-E811-8606-0025905C53DE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/763DD1A5-A7CA-E811-8FB1-901B0E542756.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/CC3F5D24-C1D0-E811-B358-008CFA1979EC.root',
] )




