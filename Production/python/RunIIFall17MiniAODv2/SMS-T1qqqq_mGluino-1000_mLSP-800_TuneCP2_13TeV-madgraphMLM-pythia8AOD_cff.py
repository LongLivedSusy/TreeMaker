import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/247ADB4A-7DBA-E811-9EDB-48FD8EE73A07.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E8EB3C1D-7DBA-E811-B94B-A0369FD0B12C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AE8F04E5-FFBB-E811-AF71-48D539F38880.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/18FBFB6D-6FBA-E811-ADE4-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1A96F8E7-6FBA-E811-96F6-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4EFE26AA-97BA-E811-9A64-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8A8116D6-70BB-E811-B28A-0242AC1C0504.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4C72502B-2FBB-E811-9501-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/348C7821-19BB-E811-8523-0025904C66F0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/82B3E033-F1BB-E811-91F2-0025904C6626.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1CFBE4F8-2DBB-E811-A7C8-AC1F6B0DE0C4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/92EBD7C6-FBBB-E811-A335-001E6757EAA4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3E5E9DBB-18BC-E811-BD2D-5065F3818271.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/9037403B-02BC-E811-B0DD-A0369FD20750.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/02A7CDB8-06BC-E811-A92C-A4BADB3CEBCE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BA60C22D-A2BD-E811-92D9-7CD30AD09C10.root',
] )






