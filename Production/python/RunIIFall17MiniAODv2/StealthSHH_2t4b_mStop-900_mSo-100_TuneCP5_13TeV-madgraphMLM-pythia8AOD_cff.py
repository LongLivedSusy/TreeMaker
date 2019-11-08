import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4EF02193-9DA2-E811-856D-EC0D9A8221CE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D8C61B10-BDA1-E811-B995-EC0D9A8222E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9481E2CC-66A8-E811-8F48-FA163E1FD66F.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C43384B2-66A8-E811-B22A-FA163EA81608.root',
] )































