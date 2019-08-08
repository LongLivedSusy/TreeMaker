import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C094C9F0-4CF7-E611-9BE5-02163E0161F9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/28B54D76-4CF7-E611-A077-02163E014878.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EECB2D72-4DF7-E611-8203-02163E01496F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/78367C98-4DF7-E611-81F8-02163E014975.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/54B33021-4EF7-E611-988A-FA163E09A161.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2C47484D-4EF7-E611-9DB0-02163E014989.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E25EFC71-4DF7-E611-A507-FA163E24A6AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9C0DB96F-4DF7-E611-BCE6-02163E0149F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BEC80DF2-4DF7-E611-A96E-FA163E6DCC97.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F6CEB976-4DF7-E611-95E2-02163E014A38.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7846CB07-4DF7-E611-9017-02163E0164E7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C46D06E6-4CF7-E611-B27A-02163E015D91.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/445AD1D4-4EF7-E611-BE4E-001E67C7B165.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/303AE398-4DF7-E611-B634-FA163E5B07B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B872CC27-4CF7-E611-AE94-FA163EDB733F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/523AEAD8-4DF7-E611-9F78-FA163E5CC0D6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/96447C92-4FF7-E611-BF90-02163E00E5AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5270AB40-4EF7-E611-BBD0-0025904B1FB0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F04F6763-4CF7-E611-A61B-FA163EC64A41.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3CC7E295-4EF7-E611-9891-02163E00C9B1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B8CA5226-4CF7-E611-BFB6-FA163EE2FFDA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/38D1A547-4CF7-E611-B421-FA163E2185B9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5CFB7D62-4CF7-E611-A351-FA163E44A24F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E685D253-4CF7-E611-93E6-FA163E63DC46.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E841C629-4CF7-E611-A6F0-FA163E7A3D59.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F0B9CA36-4CF7-E611-83A1-FA163E57D991.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3E284866-4CF7-E611-B5E6-FA163EE81AC1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A454EC2A-4CF7-E611-8974-FA163E620DD4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/34CC1F36-4CF7-E611-9CF9-FA163E5EF9B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0641E371-4CF7-E611-9365-FA163E81FC88.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/70629E53-4CF7-E611-A44F-FA163E900B1B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1EC24445-4CF7-E611-8032-FA163E76530D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4683E736-4CF7-E611-8FEF-FA163E9DC58E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7098F025-4CF7-E611-9879-FA163EB97D13.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/70A22465-4CF7-E611-85AF-FA163E2FCB5F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0C891268-4CF7-E611-91FE-FA163E438FAD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0A6BCC41-4CF7-E611-B7EB-FA163E9B7E1C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1AAC9464-4CF7-E611-924A-FA163E50AFA6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CE0BB45E-4CF7-E611-8967-FA163EF24EBC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/840A074D-4CF7-E611-9C86-FA163EE4BFA4.root',
] )






















