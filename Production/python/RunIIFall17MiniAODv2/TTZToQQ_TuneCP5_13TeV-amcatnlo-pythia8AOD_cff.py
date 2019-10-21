import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A205C6A5-FADA-E711-B1E3-FA163EDBEE1C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/EACA83E4-A5DA-E711-8EDE-24BE05CE3C91.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/520FDBC6-A6DA-E711-AE81-24BE05C6C7F1.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FED87528-86D9-E711-9F9A-FA163E857E08.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A8072956-86D9-E711-BB30-02163E013275.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/566A1B30-B2DA-E711-B22B-02163E013196.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A6534381-B4DA-E711-881E-FA163EDFCEAD.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FCF8B6E0-F9DA-E711-A1C4-FA163EB1639C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/38381C41-A8E1-E711-BAAE-0025901ABB72.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B2B1DAA0-57DF-E711-BD75-1866DAEA812C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/5C40F1A1-57DF-E711-81AD-D4AE527EEA1D.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B214ACC5-95D9-E711-923E-0CC47AD99144.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/26689580-93D9-E711-90BD-0CC47A6C186C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/8485AD01-BBD9-E711-B2F4-00238BBD758A.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1C5BF33D-BCD9-E711-955E-0CC47AACC8A0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/5830051E-C1DB-E711-89B9-008CFAC919F0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/8090E13F-B7DC-E711-8608-008CFAC9409C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/38D82C4B-C0DC-E711-93D2-008CFAC941D8.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/6E34BE15-C3DC-E711-8D0F-008CFAC919F0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/72A7A105-24DC-E711-AA99-1866DAEA8230.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BEC88DA0-25DC-E711-A16C-1866DAEA6D0C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3C037AFC-24DC-E711-88CD-1866DAEECFDC.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/882A14F9-24DC-E711-9637-549F3525BBCC.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/40499911-8BD9-E711-A304-008CFAE452D0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9CCE5A4F-F5D9-E711-AD3D-008CFAE452E0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2AAAF602-FBD9-E711-BEAA-008CFAE45060.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A0E4B514-0BDA-E711-951F-008CFAE45400.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/74CDA224-65DF-E711-AA66-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/3A5A3910-56DD-E711-AF43-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/B85723C6-8AE2-E711-906B-FA163E79DF8A.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/0889ECDD-90E3-E711-AE50-0CC47A0AD6F8.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2CCF8CC3-F6DD-E711-A779-782BCB539A3F.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F689F54F-1DDE-E711-BF55-1866DAEEB0A8.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/A61159A2-3FE2-E711-8B5E-24BE05C46B11.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/208BCF09-CEE1-E711-842C-1866DA85DEC3.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/8253DC5B-50E0-E711-B07D-24BE05C626B1.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/BA94E548-54E0-E711-A57F-24BE05BDBE61.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/EEB367DF-79E0-E711-AEC1-E0071B73C640.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/140AE126-CDE1-E711-AE33-5065F381E1A1.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F263DC17-05E0-E711-A76B-008CFAE45198.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/610000/44633EA8-F2EF-E711-B1A4-EC0D9A8221EE.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9855529F-68F1-E711-9354-E0071B74AC00.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E8D107A8-B0F1-E711-A3C1-0CC47A4D7690.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E684E4A8-E0F1-E711-91E0-0025905A60B4.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D889C618-B1F1-E711-9D7B-0CC47A7C34D0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/749915BA-B0F1-E711-9AE9-0CC47A4C8E28.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/82DD38CF-B2F1-E711-8E49-0CC47A78A3E8.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/96FFB1D1-B0F1-E711-B56C-0CC47A78A41C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B01025C0-B0F1-E711-A484-0025905A6056.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6A41D8AA-CDF1-E711-9CF9-0CC47A4D76D2.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/20521319-CCF1-E711-BCA0-0025905B858E.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/46CB3D5E-0DF2-E711-AB9D-0CC47A4D7626.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/EE35C913-EAF3-E711-8D49-0CC47A7C35E0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B6B95306-EAF3-E711-BC4A-0CC47A4D76C6.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6E8771F9-E9F3-E711-84B7-0CC47A4D7654.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9A6BF1DC-E9F3-E711-91E9-0CC47A4D7640.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A2EA0EDE-E9F3-E711-B60B-0025905A607E.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AE2AC643-EAF3-E711-8A9A-003048FFD76C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/CC98C21F-EAF3-E711-BC02-0CC47A7AB7A0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C8242F3A-EAF3-E711-9B1A-0CC47A7452DA.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C675D1E4-E9F3-E711-BB52-0025905A609E.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BABC8202-EAF3-E711-93F2-0025905B85A0.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F411C24C-EAF3-E711-9584-003048FFD72C.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AE3DA4FD-E9F3-E711-A3E5-0025905B859A.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B01C4F86-75F4-E711-B225-0CC47A4D7678.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2C5C4782-75F4-E711-8057-0025905A6104.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B03D0A01-A1F4-E711-ABA8-0025905A6126.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9EDE2A24-A1F4-E711-921E-0025905A612A.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/DA7DCB5B-E6F1-E711-8D3B-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/610000/209F5B2D-4AF2-E711-A4B2-0242AC130002.root',
] )




























