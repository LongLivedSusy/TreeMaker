import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7C47F0D9-1397-E811-8083-F01FAFE380AF.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A666C307-7497-E811-92C4-D4AE529017EB.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8AF3FD48-7397-E811-9382-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/666656D7-EB98-E811-A0ED-D4AE52E7FBCA.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C615A89B-C698-E811-A290-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D28F314C-C197-E811-8718-0CC47AD98D08.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5E195431-C297-E811-A12E-002590CB0B5A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BAB0003E-6598-E811-B21B-0CC47AD98F72.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A22F774D-0A98-E811-BE7C-008CFA166134.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AA0194FB-7497-E811-9E49-008CFA1113E4.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/743A83D9-8F98-E811-A766-008CFA110C94.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4A7B7415-C498-E811-9F4B-008CFA197D0C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/04BE80CE-1F99-E811-A0C8-008CFA110C94.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/14B2B74D-DA97-E811-846F-0025905B85B6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/24D926EE-9298-E811-A99F-0CC47A74525A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CC946FFC-1597-E811-A6A8-001EC94BA153.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0A3EBDD0-C097-E811-B5D7-001C23C0F146.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1ED9B321-4B99-E811-B0C6-F45214101150.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/326F82F9-2B9A-E811-8353-002590FD5A72.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/DE13629A-549B-E811-9D4B-AC1F6B1AF000.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/90BA3E33-4A9B-E811-8F5A-001E67E6F52B.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/20DBB311-839A-E811-A0E5-008CFAC93C50.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/84180303-929A-E811-AA7A-008CFAC91A44.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6AF1F679-2E98-E811-8C64-EC0D9A0B31B0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/16D41F18-2399-E811-BC9E-EC0D9A0B3180.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/9E625CC6-CB99-E811-B124-001E67E69E32.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BA7E9BF7-7399-E811-BD53-0025905A60FE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/26360B8D-6999-E811-AB90-0CC47A7C3472.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/744318F3-8B99-E811-A09D-0CC47A4C8EC6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/50C14D9E-5B99-E811-9592-0CC47A4D768E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FCD07A22-A899-E811-AE10-0CC47A4D7668.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/56FB1A5F-5B99-E811-AA5F-0CC47A4D75EC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/ECE89A27-A899-E811-A5FB-0CC47A78A42E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0038579D-8B99-E811-80D5-0025905A6060.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AC860471-CE99-E811-B882-0025905A607E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/EC5BA65D-F899-E811-8E2B-0025905A60B2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7EF893CA-CE99-E811-8715-0CC47A78A4A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/16C5D7DA-CF99-E811-BB12-0CC47A4C8F06.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/149FEB55-8C99-E811-9C75-0CC47A4D7630.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E4A3D691-2B9A-E811-8726-0CC47A4D767E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A20387D4-CF99-E811-B1B1-0025905B85BA.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/08479849-6999-E811-96C4-0025905A60CA.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6C03D415-6598-E811-86BC-24BE05C4D801.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A8FBEE3E-3D98-E811-91F1-5065F381C251.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FC7DC4F7-3C98-E811-9E7D-5065F381C251.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CE4007C5-4699-E811-8671-5065F37DD491.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2AE3B321-F998-E811-BFDA-EC0D9A89AA0A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/92574A6E-839A-E811-B5AB-24BE05C6D5B1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/067BB740-569B-E811-A029-5065F38122D1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1CC880ED-639B-E811-A9C1-E0071B6CAD00.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/40C6A494-0C9C-E811-8923-EC0D9A8221E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E227EE39-B29A-E811-B7E0-0025905B85A2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/56E4A867-619B-E811-B31D-0CC47A4D76B2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5265CD48-619B-E811-99F6-0CC47A7C3434.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4A51F49B-0C9C-E811-8D7C-0025905A4964.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C074FAB6-2299-E811-B56A-002590E2F5CE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/663CA6A0-699A-E811-A3DA-FA163EB4383D.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B617BFF3-0C9C-E811-96A3-0CC47A00941C.root',
] )






















