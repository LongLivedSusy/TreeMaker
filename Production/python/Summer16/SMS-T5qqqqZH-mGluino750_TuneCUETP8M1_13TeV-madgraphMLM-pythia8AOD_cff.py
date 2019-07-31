import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F224D701-31F6-E611-B051-0CC47AD98BC2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/505DC980-CEF6-E611-BC14-0CC47AD98BC8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/464E8E99-23F6-E611-95AF-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/425B4D5B-44F6-E611-952E-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8202779B-CFF6-E611-BE6B-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3003FC85-CFF6-E611-80D8-02163E014963.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/00309500-29F6-E611-94C4-008CFA1113F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CEEA86A5-45F6-E611-9222-008CFA197E0C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C81B2B16-51F6-E611-A899-008CFA111290.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F65C2DAE-CEF6-E611-835F-008CFA111210.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0ED0A78E-CFF6-E611-9EC6-FA163E50CB14.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/767D0C97-CFF6-E611-B96C-FA163E50CB14.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F023306B-D5F6-E611-97E1-02163E00C0EF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6E65A56F-D8F6-E611-9D2D-02163E00B2D9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A2BE2958-D4F6-E611-B565-FA163E691593.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/440E80AD-13F7-E611-BFBD-FA163EC2D734.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5E8D66F0-14F7-E611-94E4-FA163E6DCC97.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EE51C0C0-13F7-E611-85AE-02163E016120.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BCCD9E5F-15F7-E611-B66D-02163E016482.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BA2F4A95-15F7-E611-AC20-0025904B11B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/34C166BA-23F6-E611-81C9-002590D9D896.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6A290CD9-3EF6-E611-8F4A-002590D9DA9C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2225B7AA-45F6-E611-AE45-0CC47A0AD476.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7651E53A-CFF6-E611-8480-002590FD5A52.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C0592E80-1CF6-E611-B9D5-782BCB1D28F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/82B0E1F8-22F6-E611-A2F7-549F3525D084.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A8C9770C-2BF6-E611-A990-1866DAEA8394.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/285F72C3-31F6-E611-A11C-1866DAEA7E64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/609AFEC1-CEF6-E611-8441-D4AE52651CDE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6E87B9CB-68F7-E611-96C2-5065F382B2D1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7C6DE000-69F7-E611-B2CE-E0071B740D90.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/82676F03-69F7-E611-A850-24BE05CEED91.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02B3D9FA-68F7-E611-B852-24BE05C4D8F1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8696BA9C-98F6-E611-A8E0-0CC47A4D769E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/101C469D-98F6-E611-9795-0025905A6138.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3A6F809A-98F6-E611-AA17-0CC47A78A3D8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/046EEA9E-98F6-E611-9571-0CC47A7C35A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/689506A2-98F6-E611-97AD-0025905B85A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FE77DB3A-9EF6-E611-8705-0CC47A4D7664.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/962FC899-9EF6-E611-90C8-0CC47A78A3D8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/98210DE7-9FF6-E611-9D1C-0CC47A7C35D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D4A2A141-9EF6-E611-BBB3-0CC47A4C8F06.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1A0BBBE2-9EF6-E611-9E91-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/26D721A4-9EF6-E611-BD7A-0025905A48D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/64118BE0-9EF6-E611-A389-0025905B855C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E25EFE88-9EF6-E611-BE96-0025905B85EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/98C8D6E4-9FF6-E611-B569-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4E2A3390-ADF6-E611-A25E-0CC47A4D76B6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3086F13E-ADF6-E611-B090-0025905A48FC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7C8C63A2-ADF6-E611-8656-0CC47A7C3412.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3A2C2083-ADF6-E611-89F1-0CC47A4D75EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/284AC769-6DF7-E611-9997-0CC47A7C340E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/64D8D996-6DF7-E611-8E3A-0CC47A4D767E.root',
] )




















