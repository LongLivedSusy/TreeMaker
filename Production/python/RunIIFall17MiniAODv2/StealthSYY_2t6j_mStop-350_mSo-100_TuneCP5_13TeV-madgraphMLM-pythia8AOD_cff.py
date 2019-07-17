import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/402B9F9A-F19C-E811-8D6E-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/7A56C5F2-B39C-E811-B635-5065F38102F1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C669C0C1-759D-E811-A978-EC0D9A82264E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8E4138D2-FE9B-E811-A2B5-24BE05C63681.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/42003F83-579B-E811-A095-A0369F3102B6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/767F09A0-DB9A-E811-A9AC-B8CA3A708F98.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/7600F5E8-6E9D-E811-B3BA-008CFA165F18.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/0A3A8BF0-AC9E-E811-B5F8-90B11C27F8B2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/307F9A02-8E9F-E811-B8DE-E0071B791111.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/521A60CE-43A0-E811-8027-008CFA0A58F8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/6AB25D9D-03A0-E811-B130-AC1F6B1AEFFC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/7A7744CA-AEA2-E811-8A10-A0369F8362E2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/64101804-E09F-E811-89B1-0CC47A7C34A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3A9F7A7D-1AA2-E811-A5AC-0025905B8606.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/541C7B3F-09A0-E811-895C-3CFDFE630800.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1818AC14-85A4-E811-9685-008CFA197480.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/5E1D7F69-64A2-E811-84A1-A0369F836400.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9030E6AD-B4A2-E811-9C64-1CC1DE055158.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C61988C1-CAA3-E811-8784-0CC47A0AD6FE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/78D34F6F-91A1-E811-83CC-44A842CF05F3.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/2896DAB1-92A1-E811-9AC7-44A842CFD626.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B292CD90-C9A3-E811-BCBD-001F2908AF38.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B2F3CA32-C9A3-E811-B518-B499BAAC00E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/EED1752E-26A4-E811-8D30-0017A4771054.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/AE62C9A9-29A4-E811-B5C3-0CC47A5FC67D.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D02706A8-84A4-E811-BFEF-90B11CBCFF68.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/96CDBA19-CBA3-E811-B09E-0025901D08B0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4A8E75F8-84A4-E811-AC4E-24BE05CE1E01.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/EA752447-FDA1-E811-8901-0CC47A0AD668.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/24694464-84A1-E811-A5B9-0025B3E025B6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/7AFB9703-BDA1-E811-BA94-5065F3812201.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/F48F8FF1-E1A6-E811-8BEF-002590E39DF4.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D6CBCBDF-BAA8-E811-9A2B-FA163EBC0B5E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/507B1E61-69AC-E811-8DBA-0CC47A5FC67D.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/946F56FF-64AC-E811-8E40-001F29087EFC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8A61AECA-44AD-E811-AC90-44A842240F8D.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B8E1A9EC-F8AA-E811-842C-509A4C74D078.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/BACDB1BB-E8AA-E811-98E3-F04DA275BFC2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/E82CED1F-6AAC-E811-970D-28924A33B9FE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/BEC9358D-40AD-E811-82EA-EC0D9A0B3070.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/2830AE84-D9AB-E811-B3E4-008CFA1CBA20.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9E8157B0-64AC-E811-AC2D-B496910A8AA8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/308DAAC9-64AC-E811-B35D-FA163E2746ED.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C8769062-F0AC-E811-8890-FA163EBDB6D0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/94CB6E1F-67AC-E811-9B28-A4BF0112BE02.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/04B646B6-38AD-E811-A4F7-782BCB38EE38.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/165A5C73-65AC-E811-84BF-AC1F6B0DE0A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/BA582142-66AC-E811-A33A-3417EBE644CE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/CAC571DA-64AC-E811-BB31-0CC47A4DEE08.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/666F7173-6DAC-E811-AC59-44A842B298F1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B2736E84-45AD-E811-822E-24BE05C6E711.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/920CCD9E-58AD-E811-BDD6-842B2B765E01.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3436AD63-8DAD-E811-B80A-0CC47A4C8E70.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B6A70A74-3BAD-E811-BC2E-0025905D1D52.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/7C999B27-3AAD-E811-9048-0CC47AD98F74.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/524A64FF-4EAD-E811-9E55-0CC47AFC3C6E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/120AA5B0-C1AF-E811-B6FB-FA163EBA50EF.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1110000/C66156BB-31C3-E811-9D12-0425C5DE7BEA.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/9A25DD33-FEC3-E811-8A88-008CFA165F5C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6490B883-11C4-E811-902B-008CFA197B74.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/EE2C4516-75C5-E811-AD31-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/140DCD3A-A0C4-E811-A1BA-485B3919F111.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8233A8A2-A0C4-E811-A865-A4BF0102A5F9.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C636ED12-9FC4-E811-94FC-0CC47AB0B828.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/EC2F5DEF-09C6-E811-A90B-008CFA197948.root',
] )


















