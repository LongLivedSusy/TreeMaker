import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/5E2C42FE-07D5-E711-9022-001E67E63AE6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/568FCBD8-07D5-E711-87F4-A4BF01125740.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/605F5D03-21D5-E711-9D86-A4BF011253D0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F29EEDE8-1FD5-E711-BA4D-A4BF0112BE3C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AC746D21-5AD5-E711-91F6-A4BF0112BE34.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D0A14380-6ED6-E711-AA61-A4BF0112BD24.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FA97CA47-5FD6-E711-B163-001E67792626.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/86B5569A-4AD6-E711-8501-001E67397003.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FAFDBF5E-79D6-E711-A75B-A4BF0112BD7E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E83682F0-CBD6-E711-80DF-0CC47AF9B20A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/CC15C3EE-C9D6-E711-ADE2-0CC47AF9B2C6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/920A7D29-CAD6-E711-8BA3-0025905D1D62.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/40FF0F59-E2D6-E711-8D6E-0025905C3DD6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C6C70FC0-D2D6-E711-AD75-0CC47AF9B1EA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C271F8B2-CED6-E711-90DB-0025904C67B8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/800633C5-EDD6-E711-9E51-0CC47AF9B20A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/28CA594F-D1D6-E711-BDB0-0025905D1D50.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1831CF90-EBD6-E711-ACEB-0025905C53DE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/8E2CB5C5-E1D6-E711-A907-0025904B9B3C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F0F2FE70-F1D6-E711-807D-0025905C2CE6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/84F4BAC3-D9D6-E711-B285-0025904C6624.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/98AF324B-FCD6-E711-8AFB-0025905C54C4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/88D6DB7E-F9D6-E711-A57D-0025905D1D62.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F47F4E09-F1D6-E711-A7F5-0CC47AF9B2C6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3C6F8058-FCD6-E711-9F16-0025905C5438.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/94BE894E-F1D6-E711-9EFE-0025905C42FE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E000C1E3-F0D6-E711-AEA9-0025904C6414.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/140FEA75-11D7-E711-BE97-0025905C3DF8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AA25C4BD-0BD7-E711-A5CB-0CC47AF9B1B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/8EA65A8C-05D7-E711-95B6-0025905C3DD8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C4652B79-11D7-E711-BD99-0025905D1D7A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6AE6B776-EDD6-E711-AEBA-0025904C66F4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7CB26B6C-1AD7-E711-AE4C-0025905C3DD6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2E6DFEB8-0AD7-E711-9244-0025905C5488.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/185AC09A-17D7-E711-99E1-0025904CDDEE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/44D98558-FDD6-E711-BC3C-0025905C96E8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/DCF6AE72-3BD7-E711-86D0-0025905C9740.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C65C38CB-40D7-E711-81B5-0CC47AF9B1B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/5C9065AA-8DD7-E711-9867-0CC47AF9B2E6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/DA7FFB29-4FD9-E711-8C9C-484D7E8DF05E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/884F101F-4FD9-E711-AE72-44A842CFC9D9.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/72D38680-5CD6-E711-9D0E-001F2907EE22.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A2989AA1-28D6-E711-BBFC-FA163E5840B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/92C045AA-2AD6-E711-9188-FA163EA114BD.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/62AC96FC-2AD6-E711-951D-FA163ECA3816.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C8FBAF69-2BD6-E711-B81A-FA163EBB7C1A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6E4E598C-3ED6-E711-93E8-FA163E909D3A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B6E3773E-3BD6-E711-BEE4-FA163EA7BEB3.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D2062F49-3FD6-E711-8F50-FA163EFA55B0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/225A4BD2-37D6-E711-BE5D-FA163E18B68C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/88658A07-43D6-E711-A7F1-FA163EE0F5F8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/32AD89B0-2BD6-E711-8DCC-FA163E0D73D2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9A2FA34F-3DD6-E711-9C93-FA163E4825B4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E6AFE243-47D6-E711-BB23-FA163E5840B2.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/CCFC21D0-3ED6-E711-8B53-02163E013DF9.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3ACCE190-58D6-E711-BCA8-FA163EF5CD9F.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/10E12307-38D6-E711-9A89-FA163E24EC20.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7E0F172F-44D6-E711-BF32-FA163E401012.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/38B5F23B-4CD6-E711-A045-FA163E70D9DA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C4424649-40D6-E711-94F1-FA163ECDED06.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/32F7AEED-3DD6-E711-B40E-FA163EFDA0D3.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/106555B3-49D6-E711-8163-FA163E9807B3.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FAD3EADC-4AD6-E711-9643-FA163EDE1F00.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2AB97423-56D6-E711-A7B4-FA163EC5A4A8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BA9FD985-5ED6-E711-8A06-FA163E378B16.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6CDC6AAA-5FD6-E711-8215-FA163E6BA1DB.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/826E7872-55D6-E711-925C-FA163EF16E94.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/20F44F60-5DD6-E711-A037-FA163ECA3816.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C8AB3B03-47D6-E711-B682-FA163E03B294.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/52996B88-5BD6-E711-8733-FA163E2AAE6D.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/64F9F351-65D6-E711-8C6F-FA163EA71FB4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/5E875344-68D6-E711-8FA4-FA163EE2FC08.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9445CACC-6AD6-E711-8BBB-02163E013C35.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/28C12F4A-50D6-E711-808D-02163E013126.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/ECFADBB8-69D6-E711-A93B-FA163E275D07.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/963C83C7-63D6-E711-84C3-FA163ED2406E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7641465F-60D6-E711-BE9A-FA163EC9C155.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/44497366-60D6-E711-B765-FA163E067942.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3AFCC9FE-59D6-E711-B620-FA163E11448A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2E335884-6BD6-E711-B51A-02163E00C1BA.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/5C29762D-16D7-E711-A3A2-FA163E994D19.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/22570C20-82D5-E711-A1BD-001E67E6F823.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/C645D072-65D5-E711-95B0-A4BF0112BBDE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/4C679177-66D5-E711-9034-002590A83190.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/BAB490C1-66D5-E711-ABA5-001E67E6F503.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/E23CF2AA-66D5-E711-A71B-A4BF01125488.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/0A931F0B-88D5-E711-9920-001E67E6F616.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/568E01D6-84D5-E711-B752-001E67396FA9.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/AAB22933-CDD5-E711-BA16-001E677923E6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/D2E1C4F8-88D5-E711-AB83-A4BF01125A80.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/74C75D54-7BD5-E711-9FC3-A4BF011257B8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/EA1B270A-A0D5-E711-88EB-002590A83190.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1E4236B1-A2D6-E711-8CB1-0025B3E01806.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/04601FB4-A8D6-E711-8E8D-A0369F8362AC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C4CCC4B0-A2D6-E711-87D7-00266CFFBCD0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FE842A3E-A9D6-E711-81C7-7CD30AC036FE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6E4924C1-B1D6-E711-B698-C4346BC78D10.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B4757B99-BAD6-E711-BE42-00266CFF0AF4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D23A1529-AED6-E711-8F13-A0369F83627E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3881C5F1-BAD6-E711-AFEC-A0369F836382.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/F295602F-64D6-E711-9F2D-C4346BC8E730.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/8A97ED98-65D6-E711-A459-C4346BC85718.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/848A90A6-5BD9-E711-88C4-44A842CFD626.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/90BE1F2C-3CD6-E711-9B64-0CC47A009E26.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/726640B4-40D6-E711-8A0D-1866DA890A68.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/CECEFB60-4BD6-E711-8103-44A842CFC9F3.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/82EC0EA9-50D6-E711-AD55-44A842CF057E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/187E5C8C-98D6-E711-BB50-008CFAF52120.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7A6BEF4D-95D6-E711-A7D8-848F69FF914E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/DA212F90-98D6-E711-808E-008CFAF35A2A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A8BC3292-98D6-E711-9FE6-3417EBE643E7.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/CCFAB23D-D1E7-E711-A4A0-A4BF0115A0C0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/A0ED4F17-C5E8-E711-B408-001E6779283A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/EC63DBCE-F1F2-E711-B9A6-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/9CA1F6CF-F1F2-E711-BEB8-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/20600F01-8DF3-E711-9D21-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/82AF3434-8DF3-E711-A4B4-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/C0C187E3-D0F3-E711-A16B-0242AC1C0502.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/309F79E5-D0F3-E711-B7A4-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/70AF71E1-EBF3-E711-9569-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/0E3F4654-CCF3-E711-8338-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/76FFBF51-D2F3-E711-A859-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/587B30F0-ECF3-E711-86B2-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/C01A923B-EDF3-E711-B73F-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/D8853443-EDF3-E711-8296-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/5C80D85D-14F4-E711-9152-0242AC1C0502.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/1453C48B-1FF4-E711-A06A-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/30C04830-22F4-E711-99D8-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/E4703EDA-2CF4-E711-A7FF-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/80000/DCDA0A7E-5201-E811-86D9-001E6739834A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/0C568C9D-0606-E811-AE74-0CC47A7C35F8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/82122487-E405-E811-B044-0025905A60F8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/249B4442-0606-E811-B0F7-0CC47A4D7638.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/8ADEE01C-EB05-E811-BAAB-0025905A48EC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/4A39D74E-0706-E811-9955-0CC47A7C354A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/267965E8-FF05-E811-8FBB-0CC47A4D76C0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/BCD3638D-2A06-E811-A602-0CC47A4C8F0A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/1CC5174F-FA05-E811-9E1C-0025905A610A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/9C821D69-0106-E811-9D51-0025905B855E.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/52B005BB-0606-E811-B13F-0025905A48E4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/4A156E5E-0706-E811-B3F1-0025905A48D8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/98687411-2A06-E811-90C8-0025905B861C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/CE26EFCD-9F05-E811-9E33-0CC47A7C34A6.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/86759566-A505-E811-8904-0CC47A4C8E20.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/4CAAEC8F-B105-E811-868C-0CC47A4D75EE.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/18E03D9A-9F05-E811-8471-0CC47A4D764A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/D4753C6B-BF05-E811-B36C-0CC47A78A440.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/B489C2F6-C805-E811-A080-0CC47A7C35D8.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/F23068B5-BB05-E811-9B80-0CC47A7C347A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/52F84F6B-AB05-E811-820B-0025905B85A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/B80A3D0B-B505-E811-B48F-0CC47A4D769C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/74498761-AB05-E811-84AF-0CC47A7C35F4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/149A146C-A505-E811-9404-0025905B85DC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/6CC32226-F205-E811-BF28-0CC47A7C347A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/7215C75F-A305-E811-964D-0025905A60B4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/FAC50188-E405-E811-A8C2-0025905AA9F0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/722E8E19-EB05-E811-9A36-0025905B85CC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/B473D05B-2006-E811-BFA3-0025905A60E4.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/C24CA29F-B005-E811-8221-0025905A60A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/2850AB62-F305-E811-A67B-0025905B85A0.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/F296784B-FA05-E811-99BB-0025905A6134.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/901B4871-BF05-E811-A22B-0025905AA9CC.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/468F15EB-F305-E811-8F53-0CC47A4D769C.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/B878038B-0006-E811-940E-0CC47A7C3404.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/1CDD9AE5-FF05-E811-BCCC-0CC47A7C356A.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/985FBCE8-FF05-E811-83EA-0CC47A4C8E28.root',
'/store/mc/RunIIFall17DRPremix/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/4A4D81AD-F405-E811-A234-0CC47A4D75F8.root',
] )




































