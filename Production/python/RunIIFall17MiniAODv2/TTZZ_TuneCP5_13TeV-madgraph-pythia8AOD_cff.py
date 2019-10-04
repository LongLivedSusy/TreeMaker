import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/4A5440F0-6806-E811-9421-34E6D7E05F1B.root',
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/3A3D1BED-5C07-E811-AB4A-0425C5DE7BF0.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/AABA7933-2106-E811-AC73-002590E2DDC8.root',
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/DC1FBCE0-0707-E811-9779-90B11C27F610.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/02EDB512-810A-E811-A1EC-008CFAF721CA.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/30F9315A-FC09-E811-A500-0CC47A7E6972.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/84E081CC-030A-E811-95D2-FA163E0E0150.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/66E595E6-020A-E811-803E-FA163E421A08.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/F2880347-000A-E811-8E1D-FA163E51E1A5.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/2C70EFD9-4B0A-E811-B4DD-008CFA197D2C.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/68048664-E105-E811-9513-0025901D4B0A.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/402CACA4-0607-E811-AA7D-0CC47A706CDE.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/EED6141B-9405-E811-88E4-1866DAEA7E64.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/20E6040C-9505-E811-8D6C-0019B9CB020D.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/44ACC6D8-AB07-E811-800C-44A842CFC971.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/7602F2AA-B207-E811-8499-44A842CF061A.root',
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/CE85A0F1-FD09-E811-A711-008CFAC9432C.root',
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/2C6709A0-FC09-E811-A96E-0CC47AF9B2F2.root',
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/1E377C20-FC09-E811-AFAC-24BE05C60641.root',
'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/80000/1AEDA521-060A-E811-84C7-0CC47A5FA211.root',
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/3CD03E92-990D-E811-BA2C-FA163E3E91EF.root',
#'/store/mc/RunIIFall17DRPremix/TTZZ_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v2/40000/EE07A5F4-A00D-E811-806C-02163E019EBE.root',
] )

























