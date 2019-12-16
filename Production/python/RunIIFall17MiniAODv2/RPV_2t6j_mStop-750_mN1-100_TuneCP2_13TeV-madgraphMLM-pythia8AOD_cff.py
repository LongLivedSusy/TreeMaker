import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C889A720-6CC1-E811-B54E-A0369FC5E9A4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/189892A5-E8C1-E811-ADC4-7CD30AD08824.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4C851C01-2FC0-E811-8FC9-24BE05C6C7F1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/601D0E7C-66C0-E811-9025-24BE05CECB81.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/223AD587-45C1-E811-80FA-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2CBA0C94-E1C0-E811-BC4C-3CFDFE6396C0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/246C71A1-5CC0-E811-AFF3-001E67A3FDF8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E8828196-F0C9-E811-9C84-D8D385FF1914.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/446307AF-C9CA-E811-81C9-008CFA111348.root',
] )


































