import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/726DC26D-8EBA-E611-B226-001E675A68BF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AE3B0711-6FBA-E611-AC90-782BCB539B52.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1C4FF671-8EBA-E611-A076-B083FED42FC4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/52A08281-8EBA-E611-B395-90B11C27F383.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/16B21F6E-8EBA-E611-8304-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8ACD4B14-91BA-E611-A09E-008CFA165F48.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/36534F9B-8EBA-E611-A038-00259029E920.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D42212E4-6ABA-E611-BABA-5065F381A2E1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A2F1654D-6BBA-E611-A8AD-24BE05C6C741.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/24AE415B-6BBA-E611-8C01-5065F3812201.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D44919E1-6CBA-E611-8C97-24BE05CEEDD1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9CD80F98-6DBA-E611-BFA4-A0369F301924.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90623533-70BA-E611-A986-0CC47A4D769E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/26081049-71BA-E611-A561-0CC47A745250.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8786541-6FBA-E611-A408-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B4410508-73BA-E611-941C-0CC47A4C8F26.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0287C254-71BA-E611-8674-0025905A48BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02CEC319-73BA-E611-AAA5-0025905B85C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AC850411-75BA-E611-8E5A-0025905A6066.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E83A08AD-8EBA-E611-8117-0CC47A4C8F26.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CEEBF2AD-8EBA-E611-B182-0CC47A4D7630.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0482493A-8FBA-E611-AC63-0025904B1F90.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/56778F9E-8EBA-E611-9370-FA163E498786.root',
] )





















