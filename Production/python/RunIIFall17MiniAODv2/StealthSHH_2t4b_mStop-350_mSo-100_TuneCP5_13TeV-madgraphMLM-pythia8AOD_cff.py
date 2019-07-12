import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/94A3ED07-B493-E811-8107-1C6A7A26997F.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B63108D9-0894-E811-9202-1C6A7A26997F.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/DE7C2923-1194-E811-9C73-F8C288678781.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8C30FC28-1394-E811-98BC-0CC47A13CCEE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/30863469-6E94-E811-8313-002A6AE0D98B.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2E9F86E4-2E95-E811-984E-0CC47AD99050.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7ED56AD4-F294-E811-8456-003048F5B2F1.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A680C88C-6E94-E811-AD4E-5065F37D4131.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/686D4515-9C94-E811-BCEB-5065F381E211.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C485E151-B894-E811-B10B-E0071B73B6E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/EA73933A-FA94-E811-9025-4C79BA180A7B.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0479F3BD-7495-E811-B5EC-A4BF0115951C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/16420223-9D96-E811-A4D9-1866DA85DE6F.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/100DB625-E096-E811-86AB-F01FAFE5D12A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C4F223F1-0F94-E811-9487-D4AE529022BD.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3667DE75-7397-E811-9F39-1866DA890B94.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/20624D07-3D98-E811-8D86-1866DA890A68.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B065CF23-3D98-E811-9753-D4AE5269F611.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AE1D95A5-4899-E811-AB6D-1866DA89044E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C20FE76B-0794-E811-B5B5-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5ADA33A0-6D95-E811-9EC3-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/68C5F6AE-CA95-E811-BB85-0CC47A2B0700.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3AB088B1-9B96-E811-8E8B-E0071B7A16E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FCE200BA-9897-E811-BCFA-A4BF0115A298.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/12C57483-0898-E811-9082-001E677928AE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/12ECEF0D-CD97-E811-A555-A4BF01125BA0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6AA67A07-E197-E811-A081-001E67E33ECC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3A80EF20-6A95-E811-91E4-A0369FE2C02C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/72BF81E1-7C95-E811-A6E5-A0369FE2C02C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D40799BB-9897-E811-810F-44A842CF05E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E2AD25A5-8297-E811-8E55-484D7E8DF0FA.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/78979601-6397-E811-B74F-484D7E8DF09F.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BE1F0079-6496-E811-9F0C-FA163E1FB15A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F261AF8A-B694-E811-BD8B-00266CFEFF04.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FC5603C4-7495-E811-8495-00266CFFBF68.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/44C62267-C296-E811-8FC0-E0071B7A8560.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4C692E2C-AF97-E811-A274-E0071B745DC0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2EA4CEB5-8C96-E811-B2B8-008CFA165F48.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/76FB1ABA-F696-E811-BC2F-008CFA1113DC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5EC44C8B-2497-E811-9DBE-0CC47A7C345E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7CF1CC8C-A599-E811-B760-00266CFB991C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C2864028-009B-E811-A9B6-44A84225C893.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3C26C45E-919A-E811-A88D-008CFAC93F04.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E8448BA9-099B-E811-BD1D-002590791D60.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/40D1D3EA-B099-E811-BC1C-0025B3E01E66.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B4314BC4-9F99-E811-BE1A-24BE05CE2E81.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B456F9E4-919A-E811-82B2-24BE05C3DB21.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6E24FF31-A499-E811-AA26-0025905B8564.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D22A56C3-5B99-E811-A76D-0025905A6118.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7259177F-5B99-E811-AF87-0025905B8610.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/40174155-839A-E811-AEDE-0025905A605E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BC89F77B-9F99-E811-98F0-6C3BE5B59058.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2C873312-C999-E811-98FA-0CC47A0091C6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C2B2834A-A299-E811-8871-001E67E6F760.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2A56A5C3-EE97-E811-B527-B083FED18595.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4E402C8B-9F99-E811-919E-141877344134.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/22A392EF-CF99-E811-8D03-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1A8439AA-7398-E811-9AAD-1CC1DE056008.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/92AEE20C-ED98-E811-A2F4-AC1F6B1E2F5C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E8947128-3899-E811-90AB-00266CFFC13C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/40B8DEAA-9F99-E811-A8BB-0025901D08BA.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2E713E68-9F99-E811-A56E-002590E7DE70.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/34950654-A899-E811-A9ED-0CC47AF9B2C6.root',
] )
















