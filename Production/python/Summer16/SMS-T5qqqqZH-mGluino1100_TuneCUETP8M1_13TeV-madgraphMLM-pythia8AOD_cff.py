import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/26D3466A-DAF6-E611-BEF4-02163E019E8F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/58EF91F8-11F7-E611-99BD-02163E014557.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/46F59673-16F7-E611-A960-02163E011B62.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/725BE5C4-48F7-E611-9CE5-02163E0140E4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F6FAA6BB-49F7-E611-988A-02163E011D28.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FEEAC840-46F7-E611-A912-02163E01467E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FE38C45B-46F7-E611-A1FF-02163E014411.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A29AF1F8-48F7-E611-9826-02163E014577.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/565A38C3-4BF7-E611-82FD-02163E01417F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/74F707DA-4FF7-E611-921C-02163E0144BF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7E2C26A7-4DF7-E611-8CAC-02163E014241.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A4E105C1-4BF7-E611-9BAF-02163E0145D9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AAE81DDE-4FF7-E611-B34E-02163E014677.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/561856DB-4DF7-E611-922C-02163E0143F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/68ACC1F6-4DF7-E611-BA89-02163E012403.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AC044A78-66F7-E611-951B-02163E0141A3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/667CEFE6-4DF7-E611-B458-02163E0143BE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E64507C7-4DF7-E611-BCF3-02163E011EF3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A01CC22F-44F7-E611-B624-02163E01A4AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/78E4DEBB-4BF7-E611-A3CD-02163E014700.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C4954669-66F7-E611-ADE1-02163E01A4DA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C8654DC8-54F7-E611-9784-02163E0142AC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C231A7C5-8CF7-E611-AE63-02163E012AEB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F032EDC8-8CF7-E611-A2B5-02163E011907.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D83310C7-8CF7-E611-BA3D-02163E0121C4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/4E7A7FC3-8CF7-E611-A975-02163E01A52E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9A749FE9-8CF7-E611-868F-02163E0136AE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2265A8C7-8CF7-E611-A90E-02163E011D6D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B604B7C6-8CF7-E611-B506-02163E01368C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/306D7CC4-8CF7-E611-B5AA-02163E01444E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/205C04C7-8CF7-E611-A55E-02163E011CA1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/00190BC4-8CF7-E611-B2E3-02163E01A25C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6295BCE3-8CF7-E611-958D-02163E011BAB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/4CD916C5-8CF7-E611-B2E4-02163E014324.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2E503AC6-8CF7-E611-B9FF-02163E01356A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7C6658C6-8CF7-E611-BCFE-02163E019B69.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/8EB1DFC3-8CF7-E611-9820-02163E01A267.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C851B6C7-8CF7-E611-90A1-02163E01A620.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7C6537C5-8CF7-E611-9388-02163E01A49D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BA714CCA-8CF7-E611-86C5-02163E01A79B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7C14FCCE-8CF7-E611-9399-02163E01A2AD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D0F878C3-1EF8-E611-BD72-02163E01A3F6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6EB57A1F-1DF6-E611-AA55-008CFA197DC4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F2BAA587-B3FC-E611-8A6E-02163E014332.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/78198BA4-B3FC-E611-B856-02163E019DFA.root',
] )




















