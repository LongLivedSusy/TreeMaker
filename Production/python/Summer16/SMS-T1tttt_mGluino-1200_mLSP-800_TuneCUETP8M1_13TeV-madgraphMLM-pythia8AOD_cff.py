import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/922B6856-65B8-E611-B98C-0025904C79C6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D6E263EC-AAB8-E611-B3DE-0025904C7DF0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/58B5C003-56B8-E611-BC94-008CFA580920.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/625E68DC-59B8-E611-AE11-A0369F7FCA68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/46D17565-58B8-E611-B04C-008CFA0A570C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8E786244-5CB8-E611-BADA-A0369F739F08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D4BA442B-5BB8-E611-A400-008CFA580920.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/402DC27B-5EB8-E611-A1D8-A0369F739F08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E2119AED-60B8-E611-AB37-008CFA580920.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/08683E1E-60B8-E611-9109-549F358EB796.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D6F1AFA7-62B8-E611-B11F-549F35AC7E15.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4CB89CCA-61B8-E611-BC11-008CFA165FD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/14369F13-67B8-E611-8084-A0369F7FC934.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/72AC0190-63B8-E611-8EA7-00266CFCC68C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DEBAF15F-65B8-E611-88A4-008CFA05EA24.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C0AEF887-65B8-E611-A0D9-008CFA580920.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/98813D90-63B8-E611-B977-00266CFCC214.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AC49ADF4-67B8-E611-AB66-008CFA165FD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88B9F73C-6BB8-E611-B3A2-00266CFCC21C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6222B0F8-6DB8-E611-959A-008CFA0A565C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8E3DF8F9-AAB8-E611-AE2E-00266CFCC304.root',
] )







