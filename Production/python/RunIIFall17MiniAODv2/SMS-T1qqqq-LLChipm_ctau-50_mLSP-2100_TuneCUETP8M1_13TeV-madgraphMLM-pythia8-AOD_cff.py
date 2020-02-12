import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8BA3B5F-DA5C-E911-B358-AC1F6B0F6758.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/EEA341AA-A564-E911-A5CA-0CC47A5FC495.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/C22E350D-A564-E911-A691-D0946626135C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/12E52D2F-A264-E911-A1AA-0026B9277A59.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B0AECE2A-D85C-E911-9259-001E67F334EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/86CBAC94-5C5C-E911-B1B5-008CFA1974A4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D4AC0BD1-7D5C-E911-8F97-008CFA197B48.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D241EFB3-605C-E911-A194-002590489776.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9C5E7B60-645C-E911-83EA-90B11C26815E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1A58E109-D85C-E911-BAFA-90B11C27F89E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/14AFB0B0-5C5C-E911-8F8D-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A09768B7-605C-E911-8944-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E4540264-645C-E911-BF66-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/78E4A15F-BE5C-E911-9C92-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/32BEC7C4-A164-E911-8291-0025904C6414.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/3A3C732B-A564-E911-A26C-0025901AC3FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/922A8738-A264-E911-80BD-A4BF01158EE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/A49C01F7-A364-E911-B232-B02628343EC0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/B4D501C6-A464-E911-9FAD-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/E621B22B-A264-E911-A6F8-0242AC1C0505.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/6EC2C22E-A264-E911-BB86-008CFA0A5738.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D4C5FE7E-555C-E911-ACD9-5065F3812221.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C8BFE949-5C5C-E911-8720-B8CA3A70A520.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/96DE67A9-D75C-E911-8347-506B4BB16AE6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4E78D77D-D85C-E911-8BF0-7845C4FC3A19.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/C08ABEC6-A364-E911-A758-0CC47A6C115C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/34FA30EE-A364-E911-9628-509A4C848CAA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/02E74DB6-A964-E911-BC03-FA163E8D4408.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0230E4F1-D75C-E911-8473-B499BAAC00E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CA70423A-D85C-E911-902B-F4E9D4DF2670.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A272590-D75C-E911-BFCB-A4BF01288315.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1EAB02C4-D75C-E911-8E57-A4BF01025A8B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2A9362E3-D75C-E911-A8D6-002590D8C7BE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/24F04FCD-8B5C-E911-BD98-FA163E94DEC6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/30CFF4CE-8B5C-E911-8DD1-FA163E94DEC6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4A7F4907-8F5C-E911-A190-FA163E37C3D5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F84E8EFE-8E5C-E911-A547-FA163E4E0AAF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/565AD3F5-8E5C-E911-A3F3-FA163EA9FE8F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DA19695C-CC5C-E911-A92B-FA163EBEC51A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/827A1645-D85C-E911-84F1-1866DA890700.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8CA5E19A-D75C-E911-9843-20CF305B05B3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0225DC8F-5C5C-E911-9C90-F01FAFE159A3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F02CCF53-645C-E911-A3F9-1866DA7F90B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3E3A9B6D-7D5C-E911-BD85-1866DA7F8EE4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4CF3680A-D85C-E911-9A4D-F01FAFE0FA6E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A0FE68B0-D75C-E911-9A27-AC1F6BB1783A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/70E34929-D85C-E911-AA01-002590A3716C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3E2BE02B-935C-E911-BE6A-0CC47A4D76C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/30F58B4D-965C-E911-B8F0-AC1F6BAC7C4A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2E2F21E2-C55C-E911-BE06-0CC47A745282.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/942FA51D-A264-E911-9616-1866DA87E080.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/BEBFEED2-AC64-E911-A800-90E2BAD1BDF0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/782745DD-A264-E911-92AB-3417EBE528AF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/10000/905D121D-A264-E911-B171-20CF305B05CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/92B7CC41-D85C-E911-8C7B-509A4C9EF923.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5863CA40-D85C-E911-8813-7CD30AD09C64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/721A3554-525C-E911-B99A-0025904B307E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E26D45D7-D75C-E911-BC8F-B4E10FD217E1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AC8E650D-D85C-E911-9C55-1418774105B6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F8DBFB9C-D75C-E911-A237-00269E95AF28.root',
] )




































