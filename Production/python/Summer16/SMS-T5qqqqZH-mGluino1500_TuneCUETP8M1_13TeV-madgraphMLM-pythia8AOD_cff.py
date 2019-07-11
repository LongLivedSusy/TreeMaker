import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9E5D3F15-3BF5-E611-9211-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/88F693B7-39F5-E611-88CE-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9A6B3427-3EF5-E611-8629-D067E5F91644.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CAC63D1C-69F5-E611-8954-001E674FCAE9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/4A8F3E08-3EF5-E611-B15A-F04DA275BFFB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/50E536E3-68F5-E611-97DF-7845C4FC375E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/429297F9-34F5-E611-92BD-FA163E5CB81C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CE8C37E8-33F5-E611-A8ED-FA163E6BF2E3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/36130637-69F5-E611-BCB0-1CB72C1B65D4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CE71002D-69F5-E611-A370-008CFA197E58.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F66119C2-4DF5-E611-9E49-44A842CFD626.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9AE34140-3BF5-E611-9B0C-6CC2173D6E60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AEE57DFC-68F5-E611-90E1-0017A477047C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6CE17AE7-3AF5-E611-B46E-0025905C5488.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CEED2542-3AF5-E611-9EE0-0025905C9726.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/286B8A59-3CF5-E611-A646-0025905C96E8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BEB42B45-39F5-E611-9623-1866DAEEB364.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/129B7E9B-3CF5-E611-AD3A-782BCB20EDD2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/54414A1F-69F5-E611-9BBC-141877410E71.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E4778696-76F5-E611-9172-A0369F8363EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F442CF38-47F5-E611-9531-0025901ABB72.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E849DB2D-69F5-E611-963F-0025907D244A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/52F7DED4-33F5-E611-BFB0-0025905C2C84.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D6E96FFC-36F5-E611-8404-0025905C2CE4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/40487C0A-68F5-E611-97A8-02163E01A226.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A0883325-69F5-E611-B2CF-0CC47A13CFC0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BE4D8534-48F5-E611-B7E4-0026B94DBD6E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/36656584-51F5-E611-B9B7-BC305B390A0B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C6F8C081-39F5-E611-A3BC-3417EBE465FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AC2ED88F-39F5-E611-82B6-0026B93F4E32.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/367ECE63-31F5-E611-852D-0CC47A4C8EBA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C4C056DB-33F5-E611-8FF6-0CC47A4D76A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FE0CF0D9-33F5-E611-B32F-0CC47A4C8E5E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/167A2682-34F5-E611-B129-0CC47A78A41C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F08C49D8-32F5-E611-B592-0025905A6060.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/4262D3D5-33F5-E611-9B3A-0CC47A4D7674.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/DC699981-34F5-E611-8115-0CC47A74525A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/8CA6D6B9-36F5-E611-AFCD-0CC47A7C354A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C8B5A81F-36F5-E611-9279-0CC47A4D765E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BEEB0B02-38F5-E611-9CE8-0CC47A4D76A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/68968D09-37F5-E611-9C2F-0025905A48FC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B232178B-3BF5-E611-BC20-0CC47A4D765E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/38A289F1-3AF5-E611-86BB-0CC47A4D76B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6C121CF2-3AF5-E611-86AE-0CC47A7C3628.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5E022148-3AF5-E611-B93D-0CC47A7C34E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B6AC1646-3AF5-E611-B900-0CC47A4D7670.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B8251F8A-3BF5-E611-8976-0025905A608E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/44BD1998-3CF5-E611-99DC-0CC47A7C345C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/023C579B-3CF5-E611-85FC-0025905B85FC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D42A8441-3FF5-E611-A4F7-0025905A608E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/12FA2EFE-3DF5-E611-B88F-0CC47A4D7632.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6E8A4502-37F5-E611-A947-0CC47A78A440.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/62F59DBB-3EF5-E611-9C0B-0CC47A4C8E0E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B6753A00-3EF5-E611-946E-0025905A60BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2021BD7C-38F5-E611-BE83-A0369FD20608.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/32D51EED-40F5-E611-BB29-A0369FD20D28.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3CF9F519-69F5-E611-B1F0-00266CF85EA8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/404710F4-68F5-E611-826E-0CC47A4D7634.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/18FFCEE1-68F5-E611-8F55-0CC47A78A360.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/90EBA6F9-F0F5-E611-9E62-E0071B740D90.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/807BE775-D1F6-E611-89F9-02163E011503.root',
] )















