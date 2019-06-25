import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F81BECF8-FFB9-E611-BCA8-0025905A6092.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/708B6D6B-DEB9-E611-BBCD-ECF4BBE1CEB0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BE845E2A-E7B9-E611-BF3D-001E67397DF5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2C8ABB99-EDB9-E611-A186-0242AC130006.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2ADFF19C-EDB9-E611-AB72-0242AC130008.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/96214E9C-EDB9-E611-8438-0242AC130007.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/06ED6E9F-EDB9-E611-AF04-D067E5F91B8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/301D44A7-EDB9-E611-A695-D067E5F914D3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A23DD48D-F3B9-E611-9CFE-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/48DF5D8A-F3B9-E611-9926-ECF4BBE16468.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F449B4A4-F3B9-E611-81F4-001E67456F68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CAF0DFBB-EDB9-E611-B94A-D067E5F91F05.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8A063CE6-FFB9-E611-8786-001E674FB149.root',
] )









