import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8A089DF-1BC9-E611-B568-008CFA1C64A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8A6A1ACF-11D2-E611-8C4E-0025905C2CBA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4A61171C-11CD-E611-8F8B-0025905C94D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7626F2B3-16CD-E611-98EB-0025905C54F6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C2E9D2C9-3DCD-E611-819B-0025904C67BA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2EF49BA1-A8CD-E611-A8F8-0025905C42A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5AF4637D-2ED2-E611-B83F-0CC47A5FC281.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E64B625E-2FD2-E611-9D05-0CC47A7E6A88.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A81A7EE3-2AD2-E611-9A5B-0025905C54FC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7AC9D8D2-2DD2-E611-9C58-0025905C54FC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FC84FAC0-9CCF-E611-B530-0025905C3D6C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D6503905-6FCF-E611-BE9A-0025905C4264.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9A0650B9-84CF-E611-AC9F-0025905C3D6C.root',
] )














