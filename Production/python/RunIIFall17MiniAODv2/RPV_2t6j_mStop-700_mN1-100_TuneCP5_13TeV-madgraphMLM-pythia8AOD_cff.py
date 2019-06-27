import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/84CB1ABA-AC99-E811-A701-EC0D9A82237E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/761EA7EB-019C-E811-B912-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C2571544-F29B-E811-95DE-3CFDFE634C80.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/1C872606-E19B-E811-8B6F-0CC47A7EEE0E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/94D36CAD-9C9C-E811-B58A-001E67E6F616.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3C00B675-109D-E811-BD5E-0CC47AFB81BC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A4370591-109D-E811-841C-A0B3CCEBAA8E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7A48D0B3-6A9B-E811-861A-001E675A6725.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/70DCC1B1-F09B-E811-B83F-008CFAC94304.root',
] )










