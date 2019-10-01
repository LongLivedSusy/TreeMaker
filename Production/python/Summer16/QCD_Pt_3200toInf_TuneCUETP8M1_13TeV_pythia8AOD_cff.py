import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/C8363F52-53BB-E611-8801-0CC47A78A3EE.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/06F4D048-57BB-E611-B0FF-0025905A60AA.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/E6C4C1D0-5ABB-E611-A888-0025905A60AA.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/92C164D0-27BC-E611-BD4D-0CC47A745298.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/206F329E-4CBB-E611-A3A2-B083FED42FC4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/1AB2373F-50BB-E611-8127-1866DAEA8230.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/048DCC32-53BB-E611-A3AB-B083FED4263D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/AEEC66F2-58BB-E611-9EF4-D4AE527EDBD4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/6C59D2E7-21BC-E611-AAA3-B083FED429D6.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/522980B2-53BB-E611-AF45-FA163EAAC069.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/0C6D35C5-56BB-E611-99C0-FA163EAAC069.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/52EDA94E-5BBB-E611-9698-02163E01481B.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/E2B500C9-5EBB-E611-B24C-FA163E28E51D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/8C34F77A-23BC-E611-93FA-02163E00C518.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/A4EB35C6-29BC-E611-8EFE-FA163E1ED279.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/9A13E984-4ABB-E611-90E1-001E675A659A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/A01EF122-39BB-E611-8691-001E674FB149.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/0AE55ABC-37BB-E611-A338-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/40849BD4-3BBB-E611-9D8B-001E6745764D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/66B8B488-41BB-E611-A8FC-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/1A72899C-4FBB-E611-BAE3-001E67E0061C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/7EB7B7E6-55BB-E611-83C0-001E67A40451.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/D69B7C43-1FBC-E611-895E-001E67DFFB86.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/94B8571C-41BB-E611-9786-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/449093EC-3EBB-E611-B881-001E67397CB5.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/C8FEBD60-44BB-E611-89FB-001E674FBA1D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/E0AF939F-48BB-E611-A926-001E67457A5D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B48DCD79-46BB-E611-9E83-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/56504500-3EBB-E611-AB7D-001E67397AF3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B63DBEE7-49BB-E611-9AA2-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/3EBC6133-4ABB-E611-B13E-001E6745764D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/42DBC162-4CBB-E611-B588-001E67346BA1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/30434CA5-4CBB-E611-89A3-001E67586A2F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/06EC091F-50BB-E611-BEEC-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/363928B3-52BB-E611-A79A-001E6745764D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/54E803A4-54BB-E611-BA81-001E67397AF3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/3E522959-4EBB-E611-8A20-001E674FBA1D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/ECC40814-52BB-E611-8904-001E67397AF3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/66FBB9E7-53BB-E611-AD33-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/9C7123F4-4FBB-E611-A091-001E67397AF3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/C8CBDD57-56BB-E611-A1B1-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/6CCFBE6F-51BB-E611-9A82-001E674FCAE9.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/9072575C-55BB-E611-8D99-001E67444EAC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B61C2B3D-58BB-E611-A9A7-001E673475A6.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B28ADBFA-5CBB-E611-8F12-001E67346BA1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/76E26981-63BB-E611-8D91-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B45DC289-67BB-E611-9C57-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/E2A43510-30BB-E611-A386-001E67457E9F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/9AAC7A48-34BB-E611-9098-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/B4A93BAF-36BB-E611-9270-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/BEA55F19-39BB-E611-ABA7-001E674FB149.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/54322D46-35BB-E611-B3E7-001E67457E7C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/7ED95BE5-3BBB-E611-AFA6-001E67397CB5.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/D4E84528-40BB-E611-9D17-001E67586A2F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/121CB2AD-09BC-E611-BE44-001E67457A5D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/94952E82-4ABB-E611-8DB2-90B11C26815F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/50F818BF-4FBB-E611-9067-002590E3A0D4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/0E94B7A6-56BB-E611-8B5B-90B11C26815F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/F653063A-59BB-E611-B7F8-0CC47AA9906E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/CE5D98AF-23BC-E611-B817-003048F5B614.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B473F8A5-54BB-E611-90A4-0CC47A0AD6E0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/AA513402-61BB-E611-806D-0CC47A57D13E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B8AE17E2-46BB-E611-8011-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/E0DDC620-4DBB-E611-A800-24BE05CEDCD1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/38AE3294-4FBB-E611-8821-24BE05BDCEF1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/7A633F79-52BB-E611-B6C5-A0369F3016EC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/26144678-1CBC-E611-8012-24BE05CEBD61.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/1AF4DEF3-7DBD-E611-9A91-0025905A605E.root',
] )























