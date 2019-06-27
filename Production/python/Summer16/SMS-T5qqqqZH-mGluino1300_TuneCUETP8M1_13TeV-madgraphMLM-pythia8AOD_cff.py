import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/44FB51D4-ECF6-E611-A2A8-0025901AC3FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5AE697A3-EAF6-E611-81B3-002590D9D976.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/806F31FD-D4F6-E611-888C-02163E017680.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9486D97A-D9F6-E611-8F24-FA163E9745A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B48BAD0F-ECF6-E611-B9E4-FA163EB6EC6C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A2F2BAE-15F7-E611-BD62-FA163EB12DDB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/345CB6B9-1FF7-E611-9159-001E675792D8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/24F22BFC-68F7-E611-BF7D-E0071B7A9810.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A003CC00-69F7-E611-827B-E0071B74AC10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90DCF290-6BF7-E611-BAB1-24BE05C38CA1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C678690E-69F7-E611-9A52-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/164D1492-6BF7-E611-A92F-24BE05CEDC81.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/16E326DD-A5F6-E611-B30A-0242AC130006.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/32BB917B-A8F6-E611-AD98-ECF4BBE1CF30.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/24F61FA2-A8F6-E611-83F7-001E674DA83D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BAAD1DFA-AFF6-E611-92BA-D067E5F9156C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/14B51000-B0F6-E611-A94C-ECF4BBE1CF30.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DA0E49FD-AFF6-E611-8CD7-D067E5F91B8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9C0B4777-ECF6-E611-B326-D067E5F91B8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A350306-AEF6-E611-8E64-0CC47A78A436.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5475B802-B0F6-E611-92B5-008CFA111334.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A141200-B0F6-E611-846B-008CFA11131C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/260BE806-ECF6-E611-A6A4-008CFA197D74.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/767CDA04-AEF6-E611-85EB-0CC47A4C8ECE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D635F10B-AEF6-E611-BBA8-0CC47A4D7658.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5295D391-B5F6-E611-87F2-0CC47A4D7678.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D832EA93-B5F6-E611-8A7C-0CC47A7C3472.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B20CA68D-B5F6-E611-8011-0CC47A4D75F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/86E2BD35-73F7-E611-8E94-0CC47A4C8ECA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9C27F845-73F7-E611-90D2-0CC47A4C8EB6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FAAF514C-73F7-E611-B23E-0CC47A4D7674.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BC039B47-73F7-E611-936E-0CC47A7C3472.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/268AC63F-73F7-E611-9272-0CC47A4D7600.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/84BAE447-73F7-E611-819A-0CC47A4C8F30.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E0E8AF38-73F7-E611-8B53-0CC47A4C8EE2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E640384D-73F7-E611-A9A6-0025905B8612.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7AB5233B-73F7-E611-921E-0CC47A7C345C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/12394959-73F7-E611-95BC-0CC47A7C34EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F275544F-73F7-E611-9749-0025905B85A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/94BF7952-73F7-E611-9032-0025905A48D6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EA828B91-77F7-E611-AC7B-0CC47A78A4BA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F82F3997-77F7-E611-8E00-0CC47A4D76AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B0A59151-73F7-E611-9BB0-0025905A6060.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02C18299-77F7-E611-BB6F-0CC47A7C35F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CE236D94-77F7-E611-AF56-0CC47A4C8ECA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/720D2793-77F7-E611-8A07-0CC47A745284.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/143F18AA-73F7-E611-BC9E-0CC47A74527A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7EC0674C-73F7-E611-81DA-0025905A6104.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C61FBD96-77F7-E611-82D0-0025905B85EE.root',
] )










