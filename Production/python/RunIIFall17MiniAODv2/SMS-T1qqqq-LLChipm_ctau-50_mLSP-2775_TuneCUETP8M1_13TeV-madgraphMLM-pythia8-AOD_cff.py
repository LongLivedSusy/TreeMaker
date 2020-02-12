import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/70C0778F-F35C-E911-B263-002590E7E004.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8AF5BCF6-D362-E911-A9C7-0025905D1E08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EAD89930-F35C-E911-B68D-40F2E9C6ADBA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DA12024E-F35C-E911-B67B-40F2E9C6AD78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/50A420FA-DA61-E911-A8B6-AC1F6BAB6860.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/94B7E4BA-F45C-E911-B638-A0369FD0B22A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C21B816A-F35C-E911-A1AB-A4BF01159268.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/68B69C7C-F35C-E911-9A95-AC1F6B23C736.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6A60E90A-F45C-E911-B0F7-FA163EAAA912.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0844156D-F35C-E911-AC38-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02D3D18B-F35C-E911-8423-008CFAC93BB4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A81089B9-F35C-E911-9C99-24BE05CEEDB1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0CC0E1D4-F35C-E911-8FE2-001E67A4069F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CE96853E-F35C-E911-AF2E-AC1F6BAC7C78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3A3A98C6-F35C-E911-8479-0CC47A13CBEA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C0848892-DA61-E911-966E-7845C4FC36D7.root',
] )




































