import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/BA270B54-8288-E911-94C8-0CC47AA53D60.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/CAEA47B8-8188-E911-B5D1-ECB1D79E5C40.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/7C475919-8388-E911-B70B-34E6D7BDDEDB.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/E2EB1322-8388-E911-953B-3CFDFE54E31A.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/4CD8CEAE-4488-E911-96A3-1866DAEECFD0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/EAA15D25-8288-E911-AB84-20040FE9CBB0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/345F8AAA-0588-E911-80E2-E0071B7A6850.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/E6B49EC5-8288-E911-9701-20CF3027A55F.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/B82DE4D1-8188-E911-B79E-44A842CFC9D9.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/02A675B9-8288-E911-9F93-0025901D0946.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/12044C29-8388-E911-A188-002590DE6E92.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/8CF7C3A0-B387-E911-AECA-3CFDFE6AB014.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/B4BDE7A0-8288-E911-BF93-008CFAC93B70.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/CCDDBE36-3D88-E911-AE8C-AC1F6BAC7D10.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/5C11844F-8288-E911-B639-AC1F6BAC7C20.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/B07D649D-3E88-E911-BB69-001E67E69E05.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/4E4EB5B7-8288-E911-8CC4-001E67D195F0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/86E2208A-8288-E911-B248-001E67504645.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/5A539B1A-8388-E911-B8A6-1866DA890574.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/CA863140-7488-E911-B9BF-FA163E5CA627.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/40EFEBC1-8188-E911-A153-7CD30ACE22DE.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/230000/7AA6E639-8288-E911-A55A-A4BF0112BD3A.root',
] )












