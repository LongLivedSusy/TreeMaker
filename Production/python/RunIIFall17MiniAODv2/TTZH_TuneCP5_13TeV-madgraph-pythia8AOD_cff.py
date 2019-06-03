import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/B46B50F8-CF0A-E811-BB8F-A4BF0112BC90.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/268DC157-9F09-E811-AE58-002590E2DDC8.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/30871365-A509-E811-82C4-0CC47AD98BCC.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/7256AE95-A009-E811-9591-0CC47A13CD9C.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/1C561A69-A309-E811-9547-0CC47AD98B94.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/0EF9A395-CF0A-E811-BC1C-FA163E5B2FBF.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/6EE514FA-D00A-E811-B493-0CC47A57CD00.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/C41BEC6A-CF0A-E811-8F01-0CC47AA478BE.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/F23432A4-D10A-E811-8368-00259048AC9A.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/96D9CBD9-A609-E811-8C4C-A0369F83635A.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/467CC0D8-A609-E811-BFBB-A0369F83641E.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/F2A40DC5-C509-E811-A16D-0025905C5430.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/226FA6FF-970A-E811-A27B-0025905C42F4.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/B8D0C52E-8F09-E811-BDEA-1866DAEA6CC4.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/1296DDDD-7A0A-E811-8EFC-801844E56C20.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/98B34376-D30A-E811-B4F5-44A842CFD5B1.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/5CC0B372-EB0A-E811-A9AF-3417EBE6453D.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/BEE3A879-D30A-E811-9EE5-3417EBE643DE.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/20000/3292404C-CE0A-E811-8045-E0071B7AC700.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/7419CA94-D40E-E811-85AC-00266CFEFC38.root',
'/store/mc/RunIIFall17DRPremix/TTZH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/6ED01A8E-D40E-E811-9376-008CFAEEABF8.root',
] )
