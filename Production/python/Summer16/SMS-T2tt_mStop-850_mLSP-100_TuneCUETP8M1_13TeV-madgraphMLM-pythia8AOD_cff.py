import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1227D3BF-E3C1-E611-A785-70106F45D198.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E299A7B7-4CC2-E611-A35D-047D7B881D10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2B4260C-4DC2-E611-9FAB-14DDA9D4F168.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7091E0C3-D7C1-E611-B4C9-C4346BC87798.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4E199378-C9C1-E611-BE2A-7845C4FC3A07.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4E68FA2A-D9C1-E611-A507-7845C4F92EAF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FC5195C7-D7C1-E611-A72E-3417EBE64402.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0AA130E6-DEC1-E611-BB14-7845C4FC368C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7A12E506-E2C1-E611-B7CA-7845C4F91450.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/72F7EF1A-DCC1-E611-AD75-3417EBE64402.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/14A2B451-EEC1-E611-B725-7845C4FC37B5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8A4A80B6-F4C1-E611-A8B6-848F69FD4ED4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5E7316B7-DEC1-E611-AF8E-848F69FD090E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/421A6F37-07C2-E611-9281-848F69FD2940.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FCF5588A-93C2-E611-8A1F-7845C4F92E7F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2CFE0C4D-4EC2-E611-B956-001E6779286A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3C8EC35A-4EC2-E611-B6CB-00259074AEDE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E68D4977-DFC1-E611-91A8-02163E0145C6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CA94BBA5-DBC1-E611-9208-02163E01393B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9295899F-E1C1-E611-A97E-FA163E63EF24.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9C2BF9C4-E3C1-E611-B6FD-02163E014432.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D48D3893-E1C1-E611-A260-02163E01253C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/48A45238-DEC1-E611-BE93-02163E01392F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2D513D3-E6C1-E611-8420-02163E01391A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2617BD66-EFC1-E611-B02D-02163E0146B9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5ADEDF7E-E1C1-E611-AF6B-FA163E5F2D5B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/440DE5CE-EBC1-E611-83C9-02163E014788.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/58151612-E8C1-E611-A541-02163E019C84.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8EECD69B-F9C1-E611-9B23-FA163EBFD44B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B08A7D90-07C2-E611-AF93-02163E01453C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C511716-14C2-E611-8835-02163E011A35.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C2BC91BC-50C2-E611-BD8E-00266CF83980.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A4EF085A-FAC1-E611-88A1-00266CF83D7C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3089B7C0-0AC2-E611-91DB-000E1E878860.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4488EE05-12C2-E611-8503-A0369F63681A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BA613AC6-4CC2-E611-969E-10983627C3CE.root',
] )
