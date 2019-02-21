import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/86427CCA-D2BA-E811-B89C-001E67504D15.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4A8473C3-D2BA-E811-83A3-0CC47A2AECDC.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FA5C25C5-D2BA-E811-9B54-6CC2173C4580.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CC9029B6-D2BA-E811-B4E8-001E677927FA.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2EF93214-88BA-E811-8DF6-A0369FC5B848.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A8ECBB83-9FBA-E811-A673-1866DAEA8808.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/820A484A-87BA-E811-B864-A0369FE2C05C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7674A4BC-D2BA-E811-9473-0025901AC0FA.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1CAD7710-87BA-E811-B896-EC0D9A822616.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FC1672B7-D2BA-E811-8A4C-1CC1DE782F02.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7A58E93F-87BA-E811-867E-0025905D1D62.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E2274CAA-D2BA-E811-8F50-001517FA7A98.root',
] )
