import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/DE9C7805-F8A5-E911-8DCC-E0071B7AC770.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/00EAB9D7-70A5-E911-ABA3-0CC47AFF2A52.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/4E9DC6D4-7EA5-E911-A3ED-0CC47AFCC392.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D24D293C-F8A5-E911-828A-0CC47AFB7D90.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1CC48CBE-6BA5-E911-B720-FA163ED1FE6B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/9478E8B6-77A5-E911-BA7D-FA163E598572.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C0AA2BAC-77A5-E911-870D-FA163EB01154.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1CBBC335-76A5-E911-B23E-FA163E02E0A1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D238AE9D-77A5-E911-90C4-FA163E1C8AA5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1E74CFDE-7EA5-E911-B7BB-FA163EA6996A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/125A0CD2-7EA5-E911-808D-FA163EDA0D86.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D4A883CC-7EA5-E911-90F4-FA163E22847B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/620083E2-7EA5-E911-8D7F-FA163E9B3C4F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E04133EB-83A5-E911-A77A-FA163EACE1C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/38AB1BF6-83A5-E911-A264-FA163E0FBDE4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D005DAF4-83A5-E911-BE04-FA163E3A5C74.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/EE6842F2-83A5-E911-AA31-FA163E3A5C74.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7E2BF63F-8AA5-E911-93BA-FA163E2B69AB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/42F672BB-8FA5-E911-84EE-FA163ED1FE6B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6026021D-92A5-E911-BEFD-FA163E60B222.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2ABA6A8C-A2A5-E911-AA0B-FA163EEF12A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B4B07B3B-F8A5-E911-B954-FA163EA937D7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/BADBF2DF-7EA5-E911-9FE0-0CC47A4D7614.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/FABF4850-F8A5-E911-A5ED-0025905A6090.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E0D6B103-F8A5-E911-84F2-549F3525BF58.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/82363A54-BEA5-E911-86C5-0242AC1C0503.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3C7E0A6B-F8A5-E911-AA93-0242AC1C0504.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/5E353B33-ACA7-E911-8822-AC1F6B1AF01A.root',
] )
