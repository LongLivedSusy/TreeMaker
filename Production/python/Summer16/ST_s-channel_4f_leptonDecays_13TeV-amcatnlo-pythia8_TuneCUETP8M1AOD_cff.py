import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2C410528-17BB-E611-9499-0025905B8576.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6A34ED81-17BB-E611-BB1D-0CC47A4C8EE8.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E20181AD-17BB-E611-92E3-0025900E3514.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/36B27834-17BB-E611-A7D6-001E674FBA1D.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/96935A61-8BBA-E611-9B72-0025907D2502.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/64347A7A-8EBA-E611-BA8E-002590791DA2.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/466D9657-93BA-E611-AD51-0CC47A57CBBC.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B46E17AE-97BA-E611-B1DB-00259029E888.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D664F6D6-9ABA-E611-BF71-0CC47A57D066.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4008F9A6-9CBA-E611-8802-0CC47A57CB62.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0C37863F-9FBA-E611-AC3F-00304867FDCF.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F869E18F-A2BA-E611-BEF8-0CC47A57D066.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F6EFF20D-A3BA-E611-B8F0-002590FD5A48.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2C6C6274-A2BA-E611-AC7F-00304867FD8F.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E448362B-A1BA-E611-9B0C-003048D333EB.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7228C2E8-A3BA-E611-9D68-00304867FDCF.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CA437E62-A5BA-E611-8A6C-0030483229E0.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/32503575-A8BA-E611-8C4A-002590FD5A48.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/022D1436-A7BA-E611-9F3C-0CC47A0AD6C4.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/32198E14-A6BA-E611-B8E8-00304867FDF3.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0CF0F5B6-A9BA-E611-8DA8-0CC47A57D1F8.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BEF4B0D2-A8BA-E611-B806-00304867FDCF.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2A3E1ED4-A7BA-E611-8C31-002590812700.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DA92B2AB-AABA-E611-98E4-002590FD5A48.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4A1F4578-AEBA-E611-9994-002590FD5A48.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E2E2A932-ACBA-E611-BB90-0025907859B4.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5E31A31C-AEBA-E611-8D12-0CC47A0AD6E0.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FC1FA1CF-ACBA-E611-BD6C-0CC47A0AD6FC.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0EAD43DA-B0BA-E611-A339-0025907D2430.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8CE3CC68-BCBA-E611-8572-00259075D62E.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2AFDCEBC-C2BA-E611-AFA4-002590D9D8B8.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F657EDF9-EABA-E611-BE81-002590FD5A3A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/28230FB3-17BB-E611-9ED4-0CC47A57D066.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/26F9D0A4-17BB-E611-BD61-24BE05C48801.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0E365B7E-8FBA-E611-8D36-842B2B76670F.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6C19F4DC-92BA-E611-A6DE-0CC47A7EEDB0.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4ACBAF24-91BA-E611-8596-D4AE526A0419.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6E325717-94BA-E611-8B2F-D4AE526A0D2E.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/229C2113-97BA-E611-B6D7-0CC47A00934A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3ABD71BE-94BA-E611-A5B7-D4AE526A05F2.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7AAF27A0-98BA-E611-BA64-842B2B7680D5.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/908A0958-9ABA-E611-A99B-D4AE526A0A7B.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AAFBD62F-9CBA-E611-AFD4-0CC47A00934A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E0E06802-9FBA-E611-A534-0CC47A7EEE32.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/784BDF6C-9DBA-E611-8C4D-D4AE526A0CE0.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A488070E-9DBA-E611-83CE-D4AE526A1654.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0057472C-A1BA-E611-B5EC-0CC47A7EEE92.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B47D3CB6-A1BA-E611-8A3F-1CC1DE18D04C.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0C6382B5-A1BA-E611-911F-0CC47A7EEE32.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7EB87B02-9EBA-E611-8ACF-D4AE5269F5FF.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/845D433B-A2BA-E611-97F3-0CC47A7EEE96.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8ACA5FE2-A2BA-E611-9ECF-842B2B758BAA.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9418AF8D-A0BA-E611-B475-0CC47A00934A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C8478B2A-A1BA-E611-8EA8-0CC47A009E26.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE00A688-9FBA-E611-AF52-D4AE526A05F2.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/085128FA-A4BA-E611-8F8D-0CC47A7EEE80.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A07D9A61-A7BA-E611-99BB-842B2B7682C7.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6CB67C31-AABA-E611-8C67-D4AE526A03AD.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B03F1CAB-AABA-E611-B83A-D4AE526A05C8.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F0AA6D61-A7BA-E611-A878-842B2B7682C7.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4E7B0823-A9BA-E611-9F28-1CC1DE192872.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/04BE3426-A9BA-E611-9808-1CC1DE19316E.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/64C14025-A9BA-E611-BF54-842B2B766849.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5C392922-A9BA-E611-8F30-842B2B765E01.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/90BF6BBB-A9BA-E611-962A-D4AE5269FEF3.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CCBA90C8-A9BA-E611-9F07-842B2B7680A2.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A8558C41-AABA-E611-94AF-0CC47A0093EC.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0E71739A-ACBA-E611-BB89-0CC47A010854.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AA107722-A9BA-E611-B95E-D4AE526A0419.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D81D50DE-ABBA-E611-8591-0CC47A01CB76.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6441D9C9-AABA-E611-9203-842B2B7680D5.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/50062CBD-17BB-E611-AFE5-0CC47A009352.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7C1DBBBB-A1BA-E611-96CA-D4AE526A0D2E.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AEA19BCA-A6BA-E611-A9FC-0CC47A7EEE96.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4CC31E8E-A0BA-E611-8F9E-842B2B7680D5.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/504FC7DE-A3BA-E611-9DA2-D4AE526A0AB5.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6467E3FE-A4BA-E611-ABBF-842B2B75FDA9.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C82BE43C-A2BA-E611-A0D6-842B2B7680D5.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C6E36761-A3BA-E611-B69E-0CC47A00934A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2AECFD8E-A5BA-E611-9831-D4AE526A0CE0.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F89623EF-A6BA-E611-BBB8-0CC47A00934A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0EBC6EE0-A2BA-E611-AA31-D4AE526A05F2.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3E1F6246-A7BA-E611-AB6A-0CC47A7EEE96.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5621A06A-A3BA-E611-94E2-842B2B758AD8.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1AB9125F-A4BA-E611-8CD4-0CC47A00934A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DACABBE0-A2BA-E611-9D4A-D4AE526A0419.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8A9ECFE3-A3BA-E611-AB15-D4AE526A1654.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8E20AD9E-A8BA-E611-BE40-842B2B758AD8.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EE7F88E0-A3BA-E611-8198-842B2B7680D5.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E2644719-A6BA-E611-8977-D4AE526A1654.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8E5CE0C2-A6BA-E611-B85C-1CC1DE18D4B6.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/821D805E-A7BA-E611-B154-D4AE526A0C7A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E8AC22A2-A8BA-E611-8917-0CC47A009E26.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8CCA58D4-ABBA-E611-B9ED-0CC47A7EEE92.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/066B809C-ABBA-E611-A7D8-0CC47A00934A.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D62872AB-17BB-E611-904E-001E675A6928.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8C9A69F0-EABA-E611-97B0-1866DAEB3628.root',
#'/store/mc/RunIISummer16DR80Premix/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BAA9E0AA-17BB-E611-A9B8-1418774117C7.root',
] )



























