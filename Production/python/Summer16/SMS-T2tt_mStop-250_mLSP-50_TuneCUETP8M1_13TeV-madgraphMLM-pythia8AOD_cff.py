import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7854C421-6DD4-E611-9606-002590E3A286.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/26164099-6ED4-E611-BFFD-002590E2F9D4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5ECD2FAC-6DD4-E611-A5A0-0CC47AD98F78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/46C69888-6FD4-E611-BEF2-002590E39F4E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D4BAD2EC-71D4-E611-97B3-002590E3A286.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0257DCF6-70D4-E611-BCDC-0CC47A13D052.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/224B0F48-74D4-E611-A713-0CC47A13D2A4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/74B16B93-73D4-E611-95C1-0CC47A13D3B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4C37753A-A6D4-E611-95B5-0CC47AA989BE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/128D161F-73D4-E611-B600-FA163E68F93A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4C1AF17F-75D4-E611-8700-FA163E93D6B9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/58812F90-77D4-E611-B096-FA163E68F93A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4EC604C0-78D4-E611-B66F-FA163EC1284A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2633F2B8-7AD4-E611-A266-FA163E7C12D1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA0F0AC1-79D4-E611-AFAD-002590494DA4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/76CA4620-78D4-E611-8F34-02163E017689.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D4689CFB-7CD4-E611-83BC-FA163EBAEAC1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E053C772-8ED4-E611-942D-02163E00BD03.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5062A9F5-8CD4-E611-8C7C-02163E00AFA7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9E0079D9-8DD4-E611-B6F7-02163E0131CB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F8CBE9A8-A5D4-E611-91D7-02163E013AFC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/48BCEC00-A6D4-E611-8A86-02163E00B754.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2EE98861-A5D4-E611-9085-0CC47A0AD476.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6C366073-72D4-E611-BF5D-0CC47A4D7602.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F296FE7C-75D4-E611-8ABA-0CC47A7C357E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0A486B04-77D4-E611-B843-0CC47A4D76D6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6CFF76B9-74D4-E611-8A7D-0CC47A4D7600.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/40B4E97B-75D4-E611-A35A-0CC47A4D765A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1A8148C2-74D4-E611-8AB9-0CC47A4D7600.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FEF19707-77D4-E611-A11A-0CC47A7C3424.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0E65331B-77D4-E611-AFD9-0CC47A78A42E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A0FDF0A9-78D4-E611-854A-0CC47A4C8F30.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/76661F81-75D4-E611-8375-0025905A6056.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BC6268C7-76D4-E611-AE56-0025905B8566.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7A5BFDD5-76D4-E611-87F9-0025905A611C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D6F0BCD9-7BD4-E611-80AC-0CC47A78A3F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/041F4A63-77D4-E611-847C-0025905A60CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FA02137A-72D4-E611-8583-0025905A48BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6AE50290-79D4-E611-A387-0CC47A4C8ECA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BCE6B540-77D4-E611-A80B-0025905A60EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A653F2B5-78D4-E611-8521-0CC47A78A42E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EAE05C82-7AD4-E611-A772-0CC47A7C3412.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F4F4C89D-75D4-E611-855D-0025905A6132.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4A3AA065-77D4-E611-96F8-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B48D518F-7AD4-E611-8DBB-0CC47A7C356A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE9B6DCD-74D4-E611-9DFE-0025905B85CA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C6A1C2F1-7BD4-E611-AAC5-0CC47A4D7600.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/32D640E6-7CD4-E611-99F1-0CC47A7C3424.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/40F0F0FC-7ED4-E611-9C02-0CC47A4C8E28.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C8A1B448-77D4-E611-ABA0-0025905B85CA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A2E8A999-79D4-E611-90C5-0025905A612E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/96E87FF7-7ED4-E611-93DA-0CC47A7C3412.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/18707995-79D4-E611-8276-0025905A6068.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1CA446F6-7CD4-E611-B16B-0025905A48F2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1C88BF69-7FD4-E611-A18D-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/94005D8B-7FD4-E611-AC4E-0025905A60A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1A0A0C7C-A5D4-E611-8763-0CC47A7C3410.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/463E2274-A5D4-E611-A39F-0025905A6136.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6E8D6E9A-6BD4-E611-9EAF-B8CA3A70A410.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FA929E8F-73D4-E611-80E2-B8CA3A709028.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E2C9F98B-75D4-E611-B741-5065F38122A1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/569DFFCD-72D4-E611-AE2E-E0071B7A8550.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/84A63942-74D4-E611-B927-E0071B7A9800.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0C8056E0-75D4-E611-8322-24BE05C62611.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA47FAA7-78D4-E611-9A29-E0071B7A9800.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0EF7C163-77D4-E611-B4EF-B8CA3A70A410.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5EFE3CEA-78D4-E611-9493-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6C88A78D-78D4-E611-BE9E-B8CA3A709028.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0099A072-82D4-E611-BF5A-B8CA3A70A5E8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D2FC26CD-75D4-E611-83C5-008CFA5D275C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/063B5097-7ED4-E611-9F2F-008CFA110DD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/50E6C5E0-83D4-E611-9453-008CFA110DD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BAA416D6-6FD4-E611-A04A-1866DAEA6D0C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2E717B1E-73D4-E611-B40F-14187741212B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D036A708-73D4-E611-B95A-141877410EC1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F21E1927-74D4-E611-B3A0-1418774121A1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/102E4F31-75D4-E611-B442-1866DAEB40CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D88EE66E-77D4-E611-8434-1866DAEA812C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/243D6F6F-76D4-E611-86B2-1418774124DE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/00742584-75D4-E611-B8B0-1866DAEA6D0C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CCCD531D-74D4-E611-8FA3-782BCB50ACF1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BE2D666A-77D4-E611-AA39-1866DAEB4100.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1806545F-76D4-E611-88A9-B083FED045ED.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/164A12EE-78D4-E611-8EC9-141877410ACD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A86DE262-79D4-E611-AE18-1418773425EA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/58A88489-7AD4-E611-96F4-1866DAEA8220.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BE7AA609-7DD4-E611-9B28-141877410ACD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3AB37809-7ED4-E611-AC63-141877410B85.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/42F5514B-A5D4-E611-93AA-B083FED4263D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9C74496F-6AD4-E611-90B0-90B11C12D371.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5E4DB688-6CD4-E611-A5B3-001E67E5A38B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0E8B9B74-71D4-E611-AE16-A4BF010256DF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AEFAF2DE-72D4-E611-B722-001E67A40442.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9AD8F84E-74D4-E611-BFD7-001E67DDC051.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5433E2D5-71D4-E611-AB26-001E67E5A38B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FCF1F95A-A5D4-E611-B834-001E67A406E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E827F273-77D4-E611-80F8-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/00900995-73D4-E611-ACAC-001E674FBFC2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B247F864-A5D4-E611-BDA1-001E67586A2F.root',
] )



































