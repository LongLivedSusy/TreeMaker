import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/FCC0F9EE-B09B-E811-A5A5-008CFAC93BB0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CA4BBCD6-5D9B-E811-9A9A-A4BF01125880.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0215245A-9E9B-E811-ABD1-001E67792508.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A2EB08DB-9E9B-E811-9995-001E67E6F369.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/FAEED105-9B9B-E811-B1EA-001E677924C6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/10EB74BA-9F9B-E811-86A2-A4BF0112BE14.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/20E55E66-B89C-E811-94A3-A4BF0112E0F0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CCC9EA78-BB9C-E811-B9CE-A4BF01125E2E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D099B2D8-619B-E811-A195-3CFDFE634DE0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D249F2D8-A19B-E811-95AC-3CFDFE639880.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/FE040D5E-A29B-E811-9E9D-3CFDFE635A40.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/603DD129-FF9B-E811-951D-3CFDFE63F320.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/1EA37C05-FF9B-E811-AB69-3CFDFE6390C0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8273443B-0A9B-E811-BB09-24BE05C63791.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BEB16D8A-499B-E811-9192-5065F381A2F1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/20661F7D-C09B-E811-A393-EC0D9A8221DE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A6B14304-499B-E811-8B26-E0071B7A6850.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BA1D6869-499B-E811-BB7D-24BE05C4D8F1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/74DEE3D7-C09B-E811-9C0D-A0369F301924.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/282EFD78-AD9B-E811-A07B-E0071B6CDDA0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8274142E-AF9B-E811-8495-5065F3816222.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/26C6B4E3-FE9B-E811-B66F-EC0D9A8221CE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F0FC7DFB-FE9B-E811-9D2E-24BE05CE3C71.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F0CD2D7E-B99C-E811-86B0-24BE05C488E1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F6BC0778-789C-E811-ACEE-24BE05CEDC81.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EE919266-389B-E811-94A0-A0369FD0B1F4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D043D7D5-1D9B-E811-8776-A0369FE2C02E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/66864E56-689E-E811-9261-C45444922ADE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D6D8775A-6F9D-E811-B3D8-246E96D14BC8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8A80823D-FF9B-E811-A908-001E67DDC254.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6E6FBC26-FF9B-E811-A35C-001E67E5A38B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/FC2330B4-6E9D-E811-9B9C-A4BF0101DCC9.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CE9C12EF-089B-E811-B96E-7CD30AC03054.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8E8D3EE5-089B-E811-AE46-28924A3504DA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/289BF793-269B-E811-B411-0026B94DBE24.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C477093F-8B9C-E811-8D96-009C02AAB484.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7E67CDEB-6F9D-E811-8AF9-0090FAA575B0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/10A6AE1D-D29D-E811-BA10-0CC47A4D769C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3C88BF33-279B-E811-82BF-0CC47AA98B8C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8C36A7C4-AF9B-E811-AFD0-0CC47AD99112.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/42270397-899C-E811-A2CD-1C6A7A26C41F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/1A6D855B-6F9D-E811-B22D-002481CFE888.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9408F855-6F9D-E811-830E-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/201C9ACD-EE9B-E811-9B06-0CC47A0091C6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B411ACC9-889C-E811-B1C7-D4AE5269DC07.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2043AEBB-6E9D-E811-B1CB-1866DA87D585.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7A69005F-E99D-E811-8EF6-3417EBE65F56.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AE9645AC-279E-E811-96D0-008CFAFC6284.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2224F2FD-6E9D-E811-98BC-0CC47A6C1864.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AA9A5D02-6F9D-E811-AE67-0CC47A7E6B00.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EEADEFB4-889C-E811-A305-0025904C5DE2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C0D81A67-F99C-E811-808F-0025905C54F4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/DAE9C19F-479E-E811-AB58-002590A887F2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/2C319C9D-CDA1-E811-86AC-EC0D9A0B3360.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/7C880DBC-CDA1-E811-B8D8-A4BF0100DD3E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1110000/F6F63C72-46A1-E811-9F2B-A4BF01125E06.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/2A2B7BB5-3DA2-E811-B852-001E67792620.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1110000/9E256F80-E9A0-E811-8602-EC0D9A8225FE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1110000/CEBC39F1-FAA0-E811-9E6F-5065F381F291.root',
] )




































