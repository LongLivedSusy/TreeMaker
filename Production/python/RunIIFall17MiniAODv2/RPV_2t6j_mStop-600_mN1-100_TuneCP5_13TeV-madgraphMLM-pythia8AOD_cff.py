import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/10ECFDD0-C999-E811-91D6-782BCB1612C0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/4A702472-B69A-E811-9B29-0CC47A7EEE0E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/04187CF7-279A-E811-A989-008CFA1112BC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/58725528-979A-E811-9AAC-24BE05C63721.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/620000/F07FBA7F-D4AA-E811-AB0D-0242AC1C0507.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1230000/CAE4404A-EEBF-E811-84D5-0242AC1C0504.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1230000/B69E79C3-F5BF-E811-A701-0242AC1C0504.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1230000/1881C87D-F3BF-E811-A2CE-0242AC1C0504.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1230000/36B546B1-03C0-E811-8F13-0242AC1C0503.root',
] )




