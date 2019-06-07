import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/30758237-66F7-E611-9444-02163E014550.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/34352612-65F7-E611-81BE-02163E014149.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/58768E5D-60F7-E611-9CD4-02163E01380D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5659DD31-66F7-E611-813C-02163E011C2B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A2FC14F0-5DF7-E611-9C04-02163E01A2D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D81E0A7B-67F7-E611-8A3E-02163E0134BA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A2CB6AC9-8CF7-E611-8746-02163E01290E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5893A042-8DF7-E611-A33F-02163E012537.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A4FEE4D3-8CF7-E611-A3F6-02163E01343C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9C28BCDF-8CF7-E611-A49A-02163E01436A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9483EDC9-8CF7-E611-A0A2-02163E013707.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2EBB2ACF-8CF7-E611-9367-02163E013825.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A446EB34-8DF7-E611-AC31-02163E013721.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9A087CC4-8CF7-E611-B4D1-02163E0146D7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9E430BCE-8CF7-E611-A95F-02163E011F8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2687740C-8DF7-E611-9180-02163E019E6E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/34BAA0CC-8CF7-E611-97EE-02163E01350A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/1E389E1B-8DF7-E611-825B-02163E0145D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/12FA53F6-8CF7-E611-A4AF-02163E0137E5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/94C44ACC-8CF7-E611-8575-02163E011BBC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7C32566A-8DF7-E611-AA77-02163E011AEA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/94AE50C8-8CF7-E611-AAB8-02163E0135B6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/4C4D6BCF-8CF7-E611-9B29-02163E011DE2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D293CEEF-8CF7-E611-99BC-02163E011EB6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/760C65E2-8CF7-E611-A303-02163E011D51.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D22644DD-8CF7-E611-999D-02163E011AF9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/44D709CD-8CF7-E611-8392-02163E013395.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/DE35FED5-8CF7-E611-868B-02163E019D56.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2E57BEC7-8CF7-E611-89F3-02163E01417A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AC2BD21F-8DF7-E611-8430-02163E01463F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3027DEC6-8CF7-E611-A6BC-02163E01A745.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CC3067CA-8CF7-E611-99B4-02163E01472F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E4AA4716-8DF7-E611-A710-02163E019E04.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/00484CCC-8CF7-E611-A935-02163E01377F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E46FAA72-B3F7-E611-A225-02163E011DC3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A24FC9C3-8CF7-E611-A815-02163E01A4C5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/8C4EA0C7-8CF7-E611-AF15-02163E01A544.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F4D42FD6-8CF7-E611-8934-02163E01A546.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/8EDB36C5-8CF7-E611-843F-02163E019DD5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AA9D34CB-8CF7-E611-860C-02163E01A74F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/44C887CC-8CF7-E611-8AD0-02163E01A2E3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/023D30C4-8CF7-E611-9CA9-02163E01A1FB.root',
] )



