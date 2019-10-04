import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6007DB2A-8ECB-E611-A924-141877411FCD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CC6830AF-91CB-E611-829C-1418774108DF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5E698AAE-91CB-E611-81CF-1866DAEEB344.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/242B0D6E-90CB-E611-AB39-842B2B0A39C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/461BCAA5-93CB-E611-A69B-1866DAEA7D94.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/688AB1A5-93CB-E611-8BC5-549F3525C380.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BC11412C-93CB-E611-B20A-B083FED42FB0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/788F1BA3-94CB-E611-BBC4-1866DAEECF18.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7EA6FC8B-8FCB-E611-9780-001EC94B4F61.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/320600AC-94CB-E611-91A1-0019B9CABD35.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D6A9FA2A-97CB-E611-A81D-549F3525C380.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4E66593E-96CB-E611-BD20-B083FED14CE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/848C2FEA-94CB-E611-B50A-842B2B0A39C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9AD658B6-8FCB-E611-A05B-001C23C0F148.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E289BB12-94CB-E611-99A8-001EC94BFB39.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F4F1070A-9ACB-E611-8562-549F3525C0BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/56CCF27B-97CB-E611-B076-842B2B0A39C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B6CA1650-9BCB-E611-BC97-842B2B1732D5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0E2A3678-9CCB-E611-9B3A-B083FED14CE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/60D5DBAF-9ECB-E611-9A82-549F3525B220.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/245BD671-98CB-E611-8A56-001EC94BFB39.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CCD0330B-A2CB-E611-AAF8-141877411FCD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/16475CD3-A0CB-E611-A114-842B2B1732D5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CE9C2589-A0CB-E611-93D4-B083FED42C03.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0CF6C196-96CB-E611-A57D-0019B9CB025A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A4DDFB82-A5CB-E611-B118-1866DAEA6D0C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FA2F5312-A3CB-E611-856F-A4BADB22B643.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FA8EAA96-9ACB-E611-9C9F-0019B9CABFB6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/52A39DCD-A9CB-E611-9654-B083FED4239C.root',
] )

























