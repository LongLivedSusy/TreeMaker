import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/5A65897F-52BE-E811-BEBF-24BE05C6B701.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/E83853F9-38BF-E811-AAAF-E0071B6C9DF0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/641B3467-59BF-E811-862F-44A842B4210B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/4AF07747-8EBF-E811-87FA-0023AEEEB799.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/E46934B8-61BF-E811-B495-0425C590303A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/BC5C8E2F-5CBF-E811-8430-008CFAC94274.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/188DE530-87BE-E811-AF25-90B11C2CB121.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/288A396A-7EBE-E811-9902-40167E216787.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/8862095B-61BF-E811-AC29-1418774A2C9C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/90033CE4-60BF-E811-B560-001E675051BD.root',
] )


