import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A279B86D-4AA2-E811-838B-0025905A60DE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8E8E231B-8BA2-E811-B640-3CFDFE6399A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/54FC62B2-66A8-E811-8A01-FA163EEFFA87.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/142037B9-66A8-E811-A782-FA163EA79EBD.root',
] )

















