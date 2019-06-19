import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/1CF3FD1D-7D09-E811-8509-782BCB54BAAE.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/52BD2D8C-7306-E811-AC3C-008CFAF2931E.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/80392D06-6708-E811-A708-008CFA197BC4.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/1007210C-4109-E811-8154-7CD30AD09DE4.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/E67D1F29-1F09-E811-893D-0025905A6088.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/BC041309-1709-E811-AD02-02163E013C74.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/46708627-6308-E811-877A-002590DE6E30.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/F6FCE467-6309-E811-8924-B083FED138B3.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/CE25F315-4605-E811-906A-D8D385FF1940.root',
'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/E88BE1C2-0F07-E811-9938-68B59972C37E.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/4400755E-4E05-E811-A766-5065F3812261.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/94F9C75F-0105-E811-8655-24BE05C6D711.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/76A1EE0B-4005-E811-B8B8-24BE05C63681.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/3A4C7EF6-9705-E811-940C-E0071B7A3540.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/D4BFCE54-8A06-E811-8D2C-44A842B46A71.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/1ACE1CC9-F308-E811-AF01-A4BF0112F6B0.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/826B3CE4-6C09-E811-A2E9-008CFAF558E0.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/E4BEF4C8-6009-E811-977E-00269E95B124.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/00B5A092-560E-E811-8AE2-000E1E875C10.root',
#'/store/mc/RunIIFall17DRPremix/TTTW_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v3/40000/46F86B76-A50E-E811-AF84-7CD30AC0313C.root',
] )






