import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/02712146-5F09-E811-94B6-FA163E9CC154.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/C69D19C4-4D09-E811-BDC9-FA163EFA6DD9.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/8EBFE45E-BC09-E811-8712-FA163E5702B7.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/D62D276E-AF09-E811-A5D1-02163E014B8C.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/B4D3D566-8D0A-E811-A56C-FA163E421A08.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/BE70A4EE-F70B-E811-872E-008CFAC93F2C.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/6E462C52-7C0C-E811-A782-002590D60038.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/F285A6E0-9C0B-E811-96FD-02163E01A129.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/9A5649ED-9C0B-E811-B3B0-FA163E4AE4C1.root',
#'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/D88C0562-290C-E811-9EC9-7CD30AC03016.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/DA39C81F-7C0C-E811-915A-00259048AC9A.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/1E499DB4-F60B-E811-99FF-24BE05CECBD1.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/9C91967A-2A0C-E811-A7F0-0025904C637E.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/D2776C40-7C0C-E811-AA53-782BCB161F1B.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/80BA183F-7C0C-E811-9AA7-B496910A0430.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/92E33807-7C0C-E811-B810-0CC47AD98F74.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/D2978396-0613-E811-8120-D4AE527EE0E9.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/0E70589E-0613-E811-8722-C81F66B7864C.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/28C5CB81-3212-E811-83FC-FA163E6C39F7.root',
'/store/mc/RunIIFall17DRPremix/TTWZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/BC1DEA05-3A12-E811-A40C-FA163E02AFA7.root',
] )


















