import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E8E6EB08-1AC1-E611-8031-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/163EA645-1BC1-E611-AED3-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5A5CC4AC-1AC1-E611-AD0B-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0A47F1B1-34C1-E611-ABE6-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EC27036A-34C1-E611-975E-FA163EACFC5C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9A5B6DAA-34C1-E611-B319-02163E013EFD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/749BCC6D-34C1-E611-913E-001E67397DF5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AEA199B0-34C1-E611-96A9-0019B9CABD1C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E43451D5-34C1-E611-A4A0-0CC47A4D76D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E8C907A4-34C1-E611-A257-0CC47A4D76B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/384B6E6C-34C1-E611-8D1C-0CC47A13CEAC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2C57284A-10C1-E611-84AC-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7475E8B4-15C1-E611-977B-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/82420BBE-18C1-E611-80AA-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F2047CBD-34C1-E611-95E7-002590550504.root',
] )





















