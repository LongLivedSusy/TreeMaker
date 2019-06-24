import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/604B04E4-FEF7-E611-B7A1-02163E019BF4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9424B0B9-F2F7-E611-AB25-02163E013598.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C20B79CC-FCF7-E611-A55C-02163E011D32.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C482DE16-F7F7-E611-8164-02163E011F96.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A8FE6EC9-F4F7-E611-B3C5-02163E014185.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1E184714-F7F7-E611-B311-02163E01476C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/16AD25B7-F2F7-E611-8FE0-02163E013570.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6470C68B-F8F7-E611-9668-02163E0142C1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/52D94592-F8F7-E611-BC54-02163E011A9D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5C4E04CC-F4F7-E611-8A69-02163E014348.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2CF3D4CC-F4F7-E611-B9D1-02163E0144EA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/48D67A08-FBF7-E611-9CC4-02163E01425F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FEE086D1-00F8-E611-B21D-02163E012A58.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4EDF1DD2-FCF7-E611-9900-02163E014559.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C2066CC3-FEF7-E611-98F2-02163E01232C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A2E696C9-FEF7-E611-BEB2-02163E0133EF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/888027A6-F8F7-E611-83BB-02163E01A494.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CE284BCC-FCF7-E611-A3D2-02163E013803.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/14732C20-FBF7-E611-BF10-02163E01A528.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6EA1E3E1-08F8-E611-AE99-02163E01A552.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7C8FDCD5-FCF7-E611-A904-02163E01A375.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2C083ACE-00F8-E611-89EC-02163E0136A3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A0FC6FBE-FEF7-E611-B91E-02163E014634.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3A73989F-F8F7-E611-AE65-02163E01A283.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/68554735-03F8-E611-8DCC-02163E01A4A9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1404A6DC-FCF7-E611-977F-02163E01A404.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D2C564CC-00F8-E611-9A33-02163E01374C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B64A87D4-FEF7-E611-9D2D-02163E01A2B1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2CB2E627-FBF7-E611-A0CB-02163E01A653.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F6AB04E1-00F8-E611-B4D3-02163E01A796.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/06284A95-F8F7-E611-84C9-02163E01A6F9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B6E0C93A-F7F7-E611-9E16-02163E01A497.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B47837C2-02F8-E611-B1D9-02163E01A33D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/ECFB6DC5-FEF7-E611-AE12-02163E01A449.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FA5D782A-F7F7-E611-B3AB-02163E01A347.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/505856F6-FCF7-E611-8475-02163E01A554.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5ED99924-F7F7-E611-B47F-02163E01A46E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A8D6110F-FDF7-E611-BB40-02163E01A589.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D2E25F2D-FBF7-E611-812B-02163E01A712.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6407BD1E-FBF7-E611-A2DC-02163E019DE6.root',
] )








