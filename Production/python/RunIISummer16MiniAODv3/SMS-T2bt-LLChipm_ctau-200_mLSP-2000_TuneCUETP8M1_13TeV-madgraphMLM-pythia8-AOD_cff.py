import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/0CA8FFCA-F4A5-E911-BDDD-0242AC1C0500.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/7EC9A780-ADA6-E911-BA33-0242AC1C0507.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/92D8BB57-0FA5-E911-9EC7-6C3BE5B59218.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/8E3D276D-E1A5-E911-A601-6C3BE5B58198.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/B04FBE5E-DEA5-E911-B88E-008CFAC919D0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/D627547C-26A7-E911-BA83-842B2B1814F3.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/B64088E5-4BA5-E911-A452-0CC47A5FC491.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/5EAF6971-F4A5-E911-A78B-B02628342CB0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/E0C3B3DC-0DA5-E911-A624-44A842434705.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/F20ACFEF-17A5-E911-B1DD-20CF3027A561.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/98480E51-20A5-E911-80D2-D4856459C3E0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/86715A5B-DFA5-E911-9E15-AC1F6B0DE2EA.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/509E48E6-1FA5-E911-8C74-0CC47A1E047C.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/F08B9E2D-04A5-E911-9708-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/32357F72-DEA5-E911-9CAB-001E67F99C0A.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/6EAA2586-0FA5-E911-87CB-002590DD7C9E.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/D854B05A-E1A5-E911-B610-98039B3B01D2.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/2EC80917-21A5-E911-8879-008CFAF558E0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/4A6BE944-F4A5-E911-AD76-0026B94DBDE3.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/C2C3877F-26A7-E911-AAC5-0CC47A4D76AC.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/40285BBB-22A5-E911-8F80-549F358EB762.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/3A843E71-C9A5-E911-9DE0-0CC47A2B0214.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/C4D3800A-18A7-E911-A157-20CF3027A6B0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/4CD9AB20-D7A5-E911-B75E-002590DE6E92.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/045AC549-28A7-E911-AA7C-0CC47AC08BD4.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/CA2F57D2-D7A5-E911-9B3B-B8CA3A70A5E8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/0270362B-FBA4-E911-AA6B-FA163E3F6D58.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/FE14BE27-08A5-E911-A208-FA163EC6C162.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/F471D950-2FA5-E911-A7C7-FA163EDEF72A.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/BC4D78B9-38A5-E911-8306-FA163EBA546F.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/545A97AB-5FA5-E911-8686-FA163E6EA274.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/10A5984C-61A5-E911-A98F-FA163E144907.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/B2F55949-79A5-E911-8DB7-FA163E5E72D1.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/6A000DF8-13A5-E911-9194-842B2B765E01.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/D615BBD6-26A7-E911-9FAD-002590766A2A.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/CC67DB2E-EAA5-E911-88CC-D8D385AE8BAE.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/8A08E769-F4A5-E911-89F8-0025905C53B2.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/2843E3B0-27A7-E911-AC52-0CC47AFF248E.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/4AB2DA23-27A7-E911-B19B-2047478D3908.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/AC97C11C-28A7-E911-971D-7CD30AD091F0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/3AF4C2E9-28A7-E911-901B-00266CFFBF64.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/9E8CC01D-28A7-E911-B77A-A0369FF8852E.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/94882FB4-32A5-E911-9B13-0CC47A4C8F08.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/96D1D1C9-06A6-E911-B5C2-0025905A606A.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/260000/98DF2264-28A7-E911-8D41-002590DBE1CA.root',
] )














