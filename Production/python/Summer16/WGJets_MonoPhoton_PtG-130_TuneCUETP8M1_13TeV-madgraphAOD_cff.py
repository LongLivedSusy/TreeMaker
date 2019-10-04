import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0E4E52BF-F8B0-E611-A251-ECF4BBE1BE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4AA35A14-1EB1-E611-B9B5-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B82CDF37-92B1-E611-94BC-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9C315163-8EB1-E611-8F04-001E674DA347.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8E49E06E-B2B1-E611-A9A0-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C0943785-1DB1-E611-A753-1866DAEA8394.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AAA65B8D-1DB1-E611-BDDD-A4BADB1CF89C.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AA2E40CA-23B1-E611-A183-549F3525DDFC.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AA509D49-8EB1-E611-A63E-1418774120C3.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FE2EC074-90B1-E611-B679-1866DAEB4284.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DEA72148-B2B1-E611-BCCE-141877410522.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DEB6481E-E8B0-E611-8403-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/002E96C5-EBB0-E611-9397-5065F37D4131.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/98E9E038-EEB0-E611-BCDD-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5CA42FFF-F0B0-E611-8CDC-24BE05C666B1.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA72AA1A-F5B0-E611-87CB-B8CA3A709028.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4E8C6965-F9B0-E611-ADA4-24BE05C6C7E1.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5AE716E0-32B1-E611-B5B6-5065F381E251.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/266BE2BB-31B1-E611-963A-24BE05C44BB1.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/583023C0-31B1-E611-940F-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/98C3A21A-34B1-E611-A7E1-5065F38152E1.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/042B88B4-31B1-E611-849B-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/82B58885-34B1-E611-B717-24BE05C44BB1.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0E52066B-49B1-E611-A741-5065F37D7121.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/22664950-8AB1-E611-9C23-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7E39F0EE-ABB1-E611-8F37-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EE4CCD3C-B2B1-E611-80FA-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6034000B-8FB1-E611-A774-0CC47A4D769A.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F48B5C0E-8FB1-E611-B4F4-0CC47A4D7638.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/647E6D74-92B1-E611-8C39-0025905B85B6.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA06D774-92B1-E611-9F6C-0025905A60B8.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EE1ED65D-93B1-E611-B018-0025905A6066.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/400A333B-B2B1-E611-94D4-0CC47A7452D0.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B8798934-B2B1-E611-9FBB-0CC47A78A426.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/76E5B25C-00B1-E611-86CD-FA163EE1F3FE.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CE4DD718-B4B1-E611-9816-02163E013199.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EE62CD5D-B2B1-E611-B11A-FA163E740B03.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DED94E69-FBB0-E611-8FDB-0025905B8594.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FC859E1C-FCB0-E611-B7E6-0CC47A4D768E.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F8869D25-FCB0-E611-B411-0CC47A7C3604.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/90E7DE88-1DB1-E611-ADBB-0CC47A4C8EA8.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FE031A82-1DB1-E611-939B-0CC47A4D7666.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0833F784-1DB1-E611-A9F7-0CC47A4C8E5E.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3ED08C8A-1DB1-E611-A861-0025905A613C.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/983FFE8B-1DB1-E611-80D5-0025905B855A.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1883588C-1DB1-E611-9953-0025905A48EC.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D83491B3-23B1-E611-B802-0CC47A4C8E66.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BEAC60E1-90B1-E611-80EF-001E67A4061D.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/84C2F648-B2B1-E611-B37A-001E67A4061D.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/52CB76BB-F8B0-E611-BCC2-0CC47AD98D6E.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BECC688F-FCB0-E611-8341-002590E3A224.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/723F9B02-17B1-E611-852B-00238BBD7678.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/74E24584-1DB1-E611-9230-0CC47A6C1874.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2670EE87-1DB1-E611-B617-0CC47A13CC7E.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5C0E2B90-1DB1-E611-9583-0CC47AD98F70.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F8E4F188-1DB1-E611-ADA1-002590E2DA08.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/164DAE8C-1DB1-E611-8362-0CC47AD98F78.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/967A765C-23B1-E611-B66D-0CC47A13D418.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BEF8A984-8FB1-E611-9D50-0CC47AA989C6.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/363784CE-91B1-E611-B8DE-0CC47AA992D0.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A88DD746-B2B1-E611-AE1B-0CC47AA989CA.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C81C8BF-94B1-E611-A3CB-003048C91B0E.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88712355-B2B1-E611-932A-003048322CAB.root',
'/store/mc/RunIISummer16DR80Premix/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B68ED6F1-B2B1-E611-80E3-002590574544.root',
] )

























