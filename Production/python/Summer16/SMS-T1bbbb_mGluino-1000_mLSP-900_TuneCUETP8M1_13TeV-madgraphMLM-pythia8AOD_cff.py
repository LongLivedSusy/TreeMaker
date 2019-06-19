import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/046E057E-99BA-E611-BF12-0CC47AD98F72.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4E2B36AF-99BA-E611-8454-001E67457E7C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AE7273B3-6FBA-E611-A0C1-0CC47A4D769A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/648EF5B4-6FBA-E611-90E8-0CC47A7C347A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/361492CD-71BA-E611-B7C5-0CC47A7C357A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0E0510BE-71BA-E611-AB79-0CC47A7C3610.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/66CD0857-74BA-E611-8429-0CC47A4D75EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BE451962-74BA-E611-88AF-0CC47A745250.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/001EDDA3-72BA-E611-877C-0025905A48F2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/44B20C70-99BA-E611-B165-0CC47A4D76A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/92770B6D-99BA-E611-BB3F-0025905A60FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6C8612B1-6FBA-E611-8611-002590AC52CA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/48545F68-99BA-E611-91E9-047D7BD6DF00.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/92A9287D-99BA-E611-9B38-782BCB53B63D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F20B2FE1-99BA-E611-A166-002590760A10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4C2E5898-6ABA-E611-9135-0090FAA58274.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E4CC057F-6DBA-E611-A350-0090FAA57C60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9EC1E2C2-70BA-E611-AEA5-20CF3019DF17.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CCECA706-73BA-E611-AD6C-20CF3019DF17.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0037C067-99BA-E611-AE61-20CF3019DF17.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6270838B-99BA-E611-A7F5-001E67A40523.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/481A05C0-99BA-E611-B874-002590E7D5A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6C191AAB-99BA-E611-926A-001E67E71DFD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B81F09A1-99BA-E611-B5E4-02163E00B294.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3AA44B67-99BA-E611-B77C-FA163E75895B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5683656B-99BA-E611-A1ED-00266CFFC0C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B8174865-99BA-E611-AE71-3417EBE64AFE.root',
] )






