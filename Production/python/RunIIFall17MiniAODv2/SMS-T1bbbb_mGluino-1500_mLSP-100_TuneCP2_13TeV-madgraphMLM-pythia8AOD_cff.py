import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/32E09A08-0EBB-E811-8ACC-0025904B7C40.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/887038B8-66BB-E811-B02A-0CC47A4D762A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/94DB2642-0EBB-E811-BB09-34E6D7BDDECE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/F641F16B-15BB-E811-894D-0CC47AA53D92.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/E0921AD2-0EBB-E811-96C9-A0369FD20DA0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/CCC95952-0EBB-E811-A9A6-0CC47A5FC2A5.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/C8D4C1D0-66BB-E811-A4D9-A4BF010F1208.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/DA805F7E-67BB-E811-8921-141877638F39.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/7E165B07-0EBB-E811-9725-A0369FE2C206.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/96E8EB4F-0EBB-E811-A100-24BE05C3EC61.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/16AD9733-67BB-E811-B81B-0CC47AD98BEE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/8212EB86-67BB-E811-8810-20CF3027A5E8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/589AD8D1-21BB-E811-B70F-A4BF010298CF.root',
] )






















