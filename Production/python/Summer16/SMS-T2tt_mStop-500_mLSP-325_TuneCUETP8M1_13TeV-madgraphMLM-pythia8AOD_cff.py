import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C23F090-FDC0-E611-B8B4-B083FECFC6ED.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/76BA7C86-FFC0-E611-9059-20CF3027A5A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0EC3CABE-00C1-E611-B9DA-0025907277CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/823717E3-01C1-E611-B501-00259073E544.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/98A736E3-01C1-E611-872F-00259073E544.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/36ED5DAC-05C1-E611-B4CC-44A8422411EB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7439A4BB-02C1-E611-B4D3-20CF3027A613.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/86D6CDB4-03C1-E611-93EF-20CF3027A5A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/804F793F-05C1-E611-9E4C-B083FECFC6ED.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/727761B5-05C1-E611-95B7-0025907277CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DEC56168-06C1-E611-AA73-00259073E544.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C8338DA8-06C1-E611-B88C-00259073E544.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C82D815A-07C1-E611-A4FB-001D09FD0D10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DCF8E058-06C1-E611-8331-001E4F1B8E39.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CA5CCFCB-07C1-E611-B2A3-20CF3027A61A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/004E9C63-08C1-E611-9B61-20CF3027A613.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CC6552F8-0BC1-E611-8ACE-20CF3027A5CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C2A77F39-83C1-E611-B637-20CF3027A5A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C87A2B96-01C1-E611-82AB-001E677926C2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E64B0C93-02C1-E611-A5A9-001E67E6F5D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/86467CC3-03C1-E611-B4CB-001E67E6F5D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0E46A525-05C1-E611-9128-001E677926C2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A6CE7AA-05C1-E611-B37F-001E6739670C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5800F6A7-05C1-E611-AB03-001E67E6F5D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9871339E-07C1-E611-BC56-001E677926C2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F49B56AF-06C1-E611-B7A5-001E677928DC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4EE4372C-06C1-E611-AE75-001E6739670C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0285BF35-07C1-E611-8E11-001E67E6F9E5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/20F48CB5-04C1-E611-BC16-0025905C6448.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7614039E-07C1-E611-B74A-001E67E6F9E5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90A90E38-08C1-E611-8106-001E677926C2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E80A6B30-09C1-E611-A537-001E67E6F49A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B68CBFB3-09C1-E611-8659-001E67E6F5D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6A9D685E-0AC1-E611-B011-001E67E71408.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/00DD0648-0CC1-E611-BE71-001E67792624.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F488CA8D-0DC1-E611-BB3D-002590A80DD4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A061F6C0-0BC1-E611-8851-002590200964.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B0C1EE36-0FC1-E611-A2BB-001E677926C2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/24AC6424-11C1-E611-8BDE-002590A80DD4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B6BA50A2-15C1-E611-80ED-001E67792624.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E6434AFD-16C1-E611-B154-001E677928DC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DA7C4AA5-19C1-E611-9747-001E677928DC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CCC6EA43-35C1-E611-A430-001E67792624.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A2E2FB24-83C1-E611-B9C6-0025902008F0.root',
] )









