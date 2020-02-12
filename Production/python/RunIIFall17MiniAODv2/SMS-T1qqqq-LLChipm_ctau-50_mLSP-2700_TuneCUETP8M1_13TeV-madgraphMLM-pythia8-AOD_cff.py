import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/2ACB40B8-F55D-E911-84A6-008CFA111148.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/5A1EDF72-F15D-E911-8D43-484D7E8DF0B9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/E01FD072-F15D-E911-9625-AC1F6B0DE362.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/E87FC818-0E5E-E911-A4A8-0025905AA9CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/A2F58BBB-F55D-E911-A4DC-90B11C3D393F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/2A8ECD6C-F15D-E911-BB82-48D539F38546.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/B2457A9F-F55D-E911-8105-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/0C36C8B6-F55D-E911-9B02-0CC47A13CB02.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/D26F5D4F-0E5E-E911-AA9E-7845C4FC3A0D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/A6CE6FF0-135E-E911-96C8-5065F3812271.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/6C6431CC-575D-E911-BF1B-002590766A2A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/629785E2-F05D-E911-8144-20CF3027A607.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/270000/087D786D-F15D-E911-B576-0CC47A5FA215.root',
] )




































