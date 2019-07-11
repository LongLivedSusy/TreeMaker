import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/706C36AF-01B3-E611-BB0A-0CC47A6C1810.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/707ED3C5-FFB2-E611-B310-0CC47A13CB62.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/48E89498-01B3-E611-BC3C-B0FAEB00DCC7.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/0A023AB6-03B3-E611-9877-0CC47AA98F96.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/14607493-06B3-E611-BDB1-0CC47A6C186C.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F69846D4-05B3-E611-80C8-0CC47AA9943A.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/243C18E1-05B3-E611-B464-0CC47A6C0716.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/60BE90CD-05B3-E611-83E7-0CC47AD98D6C.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B456C237-05B3-E611-B1D7-0CC47A13CCEE.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2EA25BD8-05B3-E611-A4DD-90B11C2CA412.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/0A1753D6-05B3-E611-A533-0CC47A13CB62.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/A21D0B35-05B3-E611-8D29-0CC47A13CB36.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/6C9DBA4A-05B3-E611-B4EB-90B11C28232B.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/429D4947-08B3-E611-8D88-0CC47A13CB62.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/3A26CA4C-10B3-E611-B80E-0CC47A13CB62.root',
'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/7EEC35E9-02B3-E611-8F61-1C6A7A26C87B.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/E6386068-18B3-E611-8881-0CC47AA99436.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F801118E-1BB3-E611-A931-0025904A91F6.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/EE4E154F-1DB3-E611-9A27-003048F5ADF2.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/4CDB92BC-01B3-E611-B4E3-0CC47AD98F64.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/CCBC88B5-01B3-E611-8F91-0CC47AD990C4.root',
#'/store/mc/RunIISummer16DR80Premix/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C20D84BE-01B3-E611-9F4C-0CC47AD99146.root',
] )















