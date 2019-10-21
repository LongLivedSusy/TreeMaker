import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/62CE5157-2E95-E811-BE4C-24BE05C38CA1.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BCB543E5-6D94-E811-9150-0CC47A2B0700.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4075E543-C995-E811-8BB1-001E67A3ED40.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F0F3C36F-6D95-E811-AF49-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3AAC5CA5-4899-E811-80DC-0CC47A01035C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E01252FA-D898-E811-AC28-00266CFFC13C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F8A3A5C6-4699-E811-BE00-00266CFFBC74.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B81632A1-4899-E811-BD87-00269E95AF28.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/DCA998A6-4899-E811-B5BC-14DDA9243247.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/48B5FD57-6B98-E811-9E5B-001E677928AE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0C757821-7198-E811-B234-0CC47A2B0700.root',
] )




























