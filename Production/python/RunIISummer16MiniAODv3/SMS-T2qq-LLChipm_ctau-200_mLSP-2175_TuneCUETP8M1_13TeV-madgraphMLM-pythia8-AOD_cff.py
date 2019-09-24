import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A0155A42-36A5-E911-8413-FA163E859C32.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1ACC7B89-51A5-E911-9724-FA163ECDB2A3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/64C85E92-51A5-E911-88A5-FA163EE3F21F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/8EBDB64D-56A5-E911-BDF4-FA163EEF12A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B2DCC992-51A5-E911-9C59-FA163EF6A4E5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F6D7A370-5AA5-E911-911D-FA163E4EF85E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2468D48A-51A5-E911-BE23-FA163EBFFD16.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7069F42C-56A5-E911-A7D7-FA163E046984.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A437441C-56A5-E911-9205-FA163E752B41.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/022836AA-5AA5-E911-A7A6-FA163EACAE8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7A0B982D-56A5-E911-8D70-FA163E8D532F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B2C01C3C-34A6-E911-B3E3-FA163EE3F958.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/22A813B7-E3A5-E911-A227-801844DEF068.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/BA7029DE-F5A5-E911-A81B-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/22059327-56A5-E911-90A1-0025905B8590.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2A5A501C-56A5-E911-B47F-0CC47A78A3EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/38620F24-56A5-E911-9FCD-0CC47A4C8E64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7026A9CF-5FA5-E911-AA70-0025905B85D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/428D68C7-2DA6-E911-A1BD-0025905B858E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6A3D87EB-25A7-E911-AFC0-441EA1615F8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B08DDACC-A1A6-E911-A725-002590D8C740.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/688F4AF0-D5A7-E911-A9B0-D48564599C64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B2901DCE-25A7-E911-B65B-A0369FC5EBB0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/008F6A6D-1AA7-E911-AB50-FA163E2AABB7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C0601F40-F8A5-E911-A10F-0025905C431A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/54968987-0EA6-E911-94D8-0CC47A706F42.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/AA247501-5BA6-E911-95A8-0242AC1C0504.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3CE9C7D5-E0A7-E911-B228-002590FD5838.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3E457F97-63A8-E911-8A49-0025905C42A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/489FEC3D-8CA8-E911-9E97-0CC47AFF248E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B0400B62-AAA7-E911-9C63-008CFA105EFC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6CBA931B-B0A7-E911-B471-00266CFFBC38.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/302D883A-97A8-E911-882D-246E96D14D60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/94A08F57-8CA8-E911-91B4-0025905B85BA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3C133718-8CA8-E911-8698-EC0D9A8221CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-2175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3069A3C8-8EA8-E911-B63F-0242AC130002.root',
] )
