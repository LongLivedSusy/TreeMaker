import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2ABE5D22-645C-E911-9424-B8CA3A70BAC8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6A7E153C-375D-E911-A9F9-E0071B7A5540.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8CF681D8-C65C-E911-B068-AC1F6B23C88C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CA3EFBF4-905D-E911-9C6E-0CC47AE0F33A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5EDE110F-DC5D-E911-B80F-0025904B5FD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B68883F8-6B5C-E911-8355-000AF7386230.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BAC43564-725C-E911-B68D-D094661ED34D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1406080D-3D5D-E911-8E36-90B11C444A17.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AC588A50-DC5D-E911-93B9-D094661ED34D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6E35C81E-DC5D-E911-A875-0025904C7DF6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/34C3775D-D65D-E911-B632-0CC47A1DF806.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/42826224-3A5D-E911-A591-AC1F6B1B238A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/149EB2B6-DC5D-E911-A454-AC1F6B1AF188.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E484715D-525D-E911-AC97-FA163E39F695.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/00B9553F-DC5D-E911-B9F0-FA163E347297.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/54811BDB-DB5D-E911-8FA2-A0369FD0B3B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/52D17E40-FD61-E911-A292-FA163E9F222D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F8A9CEE9-CF5D-E911-85F5-A0369FC51AE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B84E2ABE-275D-E911-A2D7-008CFA1978F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D8F5348C-DC5D-E911-8117-3417EBE33927.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4624A7A4-C55C-E911-91D1-089E0158CFB8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/925DFAFA-905D-E911-8AB8-98039B3B003A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A84FEF3F-905D-E911-8CD5-F4E9D4DF1730.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/50EAD816-DD5D-E911-B2B5-98039B3B01B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D6614A16-DD5D-E911-BB62-D4AE526CEF9A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EADAAEBE-395D-E911-8F1C-0CC47AD9901E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7AC0DF3F-535D-E911-B949-AC1F6B4E0130.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D6191F64-DA5D-E911-9AAC-D48564599CEE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4A830844-7B5C-E911-AB96-003048CBA4EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C4184135-DC5D-E911-BC4A-003048CB8610.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/76B0B91C-DD5D-E911-82D4-544810A08360.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/10275033-EE61-E911-AF29-1866DA879B33.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3ED99D91-395D-E911-8AFB-0025905B85CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AC4BD6EE-DB5D-E911-8FDB-0025905A60F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/98278919-DC5D-E911-B9B5-28924A3504DA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6A39751C-DC5D-E911-85A0-B02628342170.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/14BF8524-DF5D-E911-9441-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/849D161B-DC5D-E911-BD8F-002481CFDE08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B6482255-325D-E911-AD22-D4AE5269F919.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CCB1A322-DC5D-E911-9D65-1866DA879EDE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/841D668C-DC5D-E911-8AC6-A4BF010F10EA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B27D556D-6765-E911-A1A2-A4BF0112BD12.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D6EE7FA8-9064-E911-B74E-0CC47A7C3420.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1446AF26-5765-E911-9C00-0CC47A4C8E38.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EC98CE27-8E65-E911-BB06-509A4C748056.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9A5958BD-FE66-E911-9EA6-0242AC1C0503.root',
] )




































