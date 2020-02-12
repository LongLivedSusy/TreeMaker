import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/600A3EFA-49A5-E911-BCFB-3417EBE7062D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/9E3F7174-3DA5-E911-8280-0CC47A7C354A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D0C03DB0-86A5-E911-8C09-0CC47A4D7614.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E6751E8F-69A6-E911-9479-0025905A48C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/264C8E51-40A5-E911-A1D8-FA163EC961E8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A09990FD-42A5-E911-9AF4-FA163E81C896.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/822A8004-43A5-E911-9E0A-FA163EFEDFA9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/98A31701-43A5-E911-9E43-FA163E0574B5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3AF0F842-4AA5-E911-82B6-FA163EF8EE11.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0CC74741-4AA5-E911-BC06-FA163EBADAE5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7064FD89-4FA5-E911-920D-FA163E876840.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/12F02F69-51A5-E911-894F-FA163E7CF110.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6EC7757D-5AA5-E911-94FB-FA163E7198ED.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0247F51B-56A5-E911-8E08-FA163E1A1070.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/BEC0F4B4-5FA5-E911-86C5-FA163EB47BBC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/30C5F2F8-5BA5-E911-B4F5-FA163E40207D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1AC4DF04-43A5-E911-BCE4-FA163E170647.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/64E414DC-26A5-E911-A547-001E67F99C0A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/44895EC4-51A5-E911-B8AF-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/14389D75-3DA5-E911-A825-0CC47AFCC3D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C8EC511A-DFA5-E911-9F91-506B4BB134CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3459FB37-43A7-E911-BAF6-40F2E9C6ADF6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/DA572421-90A8-E911-9143-40F2E9C6B036.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/00F55A04-EDA5-E911-939C-801844E56C20.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0E6D638D-F8A5-E911-ABE6-B49691386CF2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/38C57FE9-47A7-E911-BB99-BC305B390A4C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/FC421199-F8A5-E911-AB24-002590DE6E2A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/BA5C0378-45A6-E911-AEAA-A0369FC5B4F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A28D95DD-43A6-E911-BFDF-8000002AFE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/26B899FA-54A7-E911-9737-001F29082E7E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A4DE2438-1AA7-E911-BA26-FA163E2CAAB4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F6494651-23A6-E911-AD13-141877637B68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/162544CD-20A7-E911-924F-20CF3027A55F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/78477E10-99A5-E911-82D5-0242AC1C0501.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/72147468-6AA6-E911-A3CE-0242AC1C0501.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/92474B88-F8A5-E911-8D89-0CC47A5FC491.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/563C6D1B-EFA5-E911-85B5-001E675A5244.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3CCEF8C2-D3A7-E911-B7A3-48FD8E282979.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/124E1120-A9A7-E911-9B49-00266CFEFDE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/16CC2CB3-90A8-E911-8E93-00266CFFBF68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/AE0A173E-90A8-E911-A133-842B2B0A39C6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C8D48ECC-91A8-E911-A0FA-E0071B7A6850.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1469BC9B-91A8-E911-8708-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/981BAE18-97A8-E911-894A-246E96D10C28.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/BA1B82F7-94A8-E911-B09B-0CC47AFF01B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/82279D30-90A8-E911-AADD-001E67586629.root',
] )


















