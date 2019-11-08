import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A8A6C140-8FD7-E611-948B-0CC47A4C8E86.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/16959E39-8FD7-E611-883C-0CC47A7C3430.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C88E523E-94D7-E611-94A2-0CC47A78A33E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7E9EA340-94D7-E611-B258-0CC47A7C3432.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/966FE943-94D7-E611-B861-0CC47A7C34EE.root',
'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/26297041-94D7-E611-9DAE-0CC47A74524E.root',
'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C2E49D7B-93D7-E611-A961-0CC47A7C34C4.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/545CA083-93D7-E611-A3FA-0CC47A4C8EEA.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/94E5D467-93D7-E611-9D0B-0CC47A4D767A.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9A89620F-96D7-E611-A990-0CC47A7C340E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/46592D6F-95D7-E611-828B-0CC47A4C8E1C.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/603F2F50-94D7-E611-9087-0025905A4964.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AC30BFA1-93D7-E611-B695-0025905A6118.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B67853B7-97D7-E611-A050-0CC47A7C34C8.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6A9DD7B9-97D7-E611-A0FE-0CC47A4D7662.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4C5A88C9-97D7-E611-A6A4-0CC47A4C8F0C.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CC423ACD-97D7-E611-AD9A-0CC47A78A456.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/12CB13E4-97D7-E611-9AF7-0CC47A4C8ED8.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/66B03EFD-97D7-E611-B7D7-0CC47A78A33E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8EA2DF1B-96D7-E611-9935-0CC47A78A2EC.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/24BA0B24-96D7-E611-A263-0CC47A7C34EE.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5C25CD28-96D7-E611-9C9A-0025905A6110.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C4E1E40-96D7-E611-A9DA-0CC47A7C354A.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CEB9F918-96D7-E611-9D4F-0CC47A4D7632.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/40FFD30C-98D7-E611-B34C-0025905A60B2.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/72796844-98D7-E611-9D7E-0CC47A4D7632.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D475E347-98D7-E611-BEF9-0CC47A4D769C.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F4F9712B-96D7-E611-AAE7-0025905A613C.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/30D8A673-95D7-E611-9066-0025905B8568.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0E385A5A-9AD7-E611-A17B-0CC47A78A458.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EEC0BE69-9AD7-E611-BE95-0CC47A4C8F12.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E4D17673-9AD7-E611-8C3A-0CC47A4D76B6.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5071EF62-9AD7-E611-BCB1-0CC47A4D7698.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D83F7491-9AD7-E611-A19E-0CC47A7C3432.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/30CF804A-98D7-E611-AEEB-0025905B85F6.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F6838096-9AD7-E611-B806-0CC47A4D767C.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1AD5AE7A-9AD7-E611-8292-0CC47A4D767E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D6F71486-9AD7-E611-87E4-0025905A60BC.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FA194170-9DD7-E611-801C-0CC47A78A4A6.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B6FBEC9D-9ED7-E611-8842-0CC47A4C8F10.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F2D68B8B-A0D7-E611-96F8-0CC47A4D760C.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/529F5B29-A1D7-E611-B457-0CC47A7C351E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/80E74B92-9AD7-E611-85D1-003048FFCBB8.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E00A2F6D-9AD7-E611-BE2D-003048FFCBB8.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/484CAD86-9AD7-E611-8B76-0025905B857E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C0D3A31-9DD7-E611-8D5C-0CC47A4D7674.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/224A643B-9DD7-E611-8B77-0CC47A4C8F06.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FE8F3660-9DD7-E611-AEBC-0CC47A78A33E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/38381770-9DD7-E611-8F9B-0CC47A4D7694.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2AC26FF0-9DD7-E611-ADF5-0CC47A4D7632.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CEA010EC-9CD7-E611-8D11-0CC47A7C34C8.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9A6AB1F1-9CD7-E611-945E-0CC47A4D7632.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1C3A1621-9ED7-E611-A334-0CC47A7C347E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4EC89234-9ED7-E611-91FE-0CC47A4C8E0E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C83D1928-9ED7-E611-B0E4-0CC47A78A426.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/822EE73B-9ED7-E611-BBC0-0CC47A4D769C.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B892309E-9ED7-E611-BEDA-0025905A60AA.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E2627C88-A0D7-E611-A1E5-0CC47A7C3444.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AEDBC3C4-A0D7-E611-B355-0CC47A78A3F4.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5E8C3262-9DD7-E611-8A1F-003048FFD772.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/347FCE75-9DD7-E611-8130-0025905A612E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B49803ED-9DD7-E611-A07D-0025905A607E.root',
'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6EC9A807-9ED7-E611-A4D3-0025905B85B6.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8AA7812A-9ED7-E611-A21F-0025905A60FE.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B8A86EB3-9ED7-E611-A94F-0025905A609E.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/ACACADB3-9ED7-E611-BA92-0025905A6060.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E63B42B5-9ED7-E611-AEDC-0025905B85EC.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0455E4CA-A0D7-E611-B958-0025905A6110.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/665EFD71-9DD7-E611-A32A-0025905A6090.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E935E80-9DD7-E611-B1F7-0025905A609A.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/62DAB12B-9ED7-E611-B83C-0025905A60CA.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6C50A7C7-A0D7-E611-84D5-0025905A6068.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/20E1DA9B-B3D7-E611-9615-0025905A60FE.root',
#'/store/mc/RunIISummer16DR80Premix/WW_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F8CE5D99-B3D7-E611-9909-0CC47A4D762E.root',
] )































