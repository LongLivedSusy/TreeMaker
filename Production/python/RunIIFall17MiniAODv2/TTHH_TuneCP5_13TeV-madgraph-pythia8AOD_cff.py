import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/929A7BB3-B720-E811-8C40-001E67E6F805.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/600D2A60-B720-E811-9E52-002590E3A0EE.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/E859ABF5-F91F-E811-A24D-FA163EF568AC.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/AC2B3FFE-F91F-E811-A708-FA163EA56006.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/2E901E76-B620-E811-86FB-0025905C42F4.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/B4CBFCEE-B620-E811-B68A-0025905A6110.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/560FDDA9-F920-E811-9775-C4346BBF3E78.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/A01F0B58-481E-E811-93F8-001E675825D4.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/DCCACE33-A31E-E811-A13A-001E675825D4.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/8A78AD92-AF1E-E811-AD0D-001E67504445.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/18B24E9E-4A1E-E811-98F9-00215AAFFBE8.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/2ED4F920-F91D-E811-A88A-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/7E65B8C8-FC1D-E811-A4A5-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/7A5833A7-B620-E811-AD3E-E4115BCEE072.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/ACB6736C-4B1E-E811-A36F-FA163E42C814.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/2A3EC01A-4B1E-E811-8136-02163E019F63.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/60000/A6066F5F-7822-E811-B290-0CC47A4C8E86.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/60000/94DE3389-7822-E811-A993-FA163E802A8D.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/60000/7EB7F33E-7722-E811-BB15-FA163E344602.root',
'/store/mc/RunIIFall17DRPremix/TTHH_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/50000/DE2BDE91-021C-E811-B0AB-901B0E6459CA.root',
] )

