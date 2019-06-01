import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D0609EA8-38A6-E811-8009-E0071B7AE500.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/745CA910-3AA6-E811-B51C-EC0D9A822606.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/ECA6085C-9FAB-E811-B448-AC1F6B0DE362.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/466E5E29-3CAC-E811-B4FF-0CC47A412A7A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/6A3D230D-3CAC-E811-9A27-B499BAAC064E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/2AEE6B08-3CAC-E811-91C3-0CC47A57D1F8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/20E42E38-B8AB-E811-91AF-001E67E33ECC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B841C488-D7AB-E811-9C98-001E6757F1D4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D4B21E77-A2AB-E811-BE79-0025905C975E.root',
] )

