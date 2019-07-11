import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/B0DE2B69-4AFD-E711-9190-0CC47A7FC746.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/16D33BA0-53FD-E711-96F9-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/385ECBCA-4BFD-E711-98E3-0025904CF102.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/942C3EDB-4DFD-E711-936A-0025901D08F0.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/4081A2D9-4EFD-E711-BCD1-0025904C7B26.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/4A8AD2C6-4BFD-E711-94F2-D8D385AE8B24.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/DAB20B70-18FA-E711-92CF-1866DA85D893.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/D4E87522-3AFA-E711-A350-1866DA85DAB8.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/9A7CDF5E-3AFA-E711-99B9-1866DA7F9160.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/0A3604D7-BEFF-E711-9B35-E0071B73C600.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/4E3EE86D-9200-E811-8036-24BE05C6C7E1.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/7069241B-5601-E811-97EC-002590E7D7C2.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/029EF613-B501-E811-A00D-141877410512.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/4E15B3B2-54FD-E711-B951-FA163E0683BD.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/3ACA01B9-4AFD-E711-9A1F-549F35AF4517.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/4017D899-54FD-E711-B99D-0CC47A5FBE35.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/6ADDC1C9-54FD-E711-9C86-0CC47A5FBE25.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/DA46CCEC-7200-E811-996E-008CFAC91D68.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/2E776E0F-6B00-E811-92A1-008CFAC93E84.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/182E56EE-5201-E811-A392-00259075D702.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/104F8110-B501-E811-8F65-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/B26CEDD3-E112-E811-9F75-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/TTWH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/40000/7424BB38-E512-E811-AAC7-0242AC1C0501.root',
] )















