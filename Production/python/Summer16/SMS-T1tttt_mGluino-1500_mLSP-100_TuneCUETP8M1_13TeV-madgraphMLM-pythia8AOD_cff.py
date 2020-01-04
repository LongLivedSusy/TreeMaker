import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/387C7D5B-40B8-E611-87D4-001E6779238C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F2142840-45B8-E611-BE8A-001E67E6F76A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/84FAE133-48B8-E611-9995-002590A3A3D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2274DA88-E2B8-E611-AADE-001E67E71CA4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9A12553D-48B8-E611-87A2-0025907DCA0C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B0576B5A-4BB8-E611-913B-047D7B881D0C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F677249E-4CB8-E611-B959-00266CF2AE10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B8339FE6-FBB8-E611-802D-E41D2D08DFA0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8A23C1FD-3DB8-E611-987D-44A84225D0B7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E472788D-43B8-E611-A227-B083FED13803.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/50362A2A-48B8-E611-91BB-44A84225CFF0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/38B82D45-47B8-E611-A777-0CC47ABB517C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/64C9AF43-FCB8-E611-B22C-20CF305B05AE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C677F768-FCB8-E611-98B3-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/284377E4-FBB8-E611-8131-3417EBE643F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B084ACAD-3EB8-E611-ADF5-0090FAA57470.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C40182E0-40B8-E611-8D31-0090FAA576C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E811A1A0-41B8-E611-9391-00259073E4EA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/66A02814-44B8-E611-9CED-0090FAA576C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2867D331-48B8-E611-8B6E-0090FAA569C4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A4F982AE-49B8-E611-839C-0090FAA59184.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/443E781E-4BB8-E611-97EB-0025907B4F08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/909CBFF3-FBB8-E611-B983-00266CFFBCFC.root',
] )



































