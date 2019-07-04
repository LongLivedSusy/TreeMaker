import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/3461A247-8CBE-E811-8D8B-0CC47AD98F6E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/84C73B3F-86BE-E811-952C-0CC47AACFCDE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/3E80E856-86BE-E811-89FE-0CC47AA989C2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/9EFFE6B3-4ABF-E811-AF09-002590489776.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/6E39DF2B-3FBF-E811-8ED1-0025904A9430.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/58B32DFE-38BE-E811-BF8C-3CFDFE63EAA0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/A40BC1A1-11BF-E811-92D6-3CFDFE63ED40.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/8CA0059F-11BF-E811-A358-003048F2B302.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/AAE14E70-70BE-E811-92E7-EC0D9A8221E6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/DEA327DA-04BF-E811-9D91-5065F3818241.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/E039B301-0FBF-E811-9880-E0071B691B81.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/88D74A12-CEC1-E811-9D90-90B11C4440CE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/7C095F1A-2BCD-E811-A2D6-A0369FD20AFC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/DC5246A3-43CD-E811-8DD2-A4BF01014073.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/2AA7DC4A-F9CD-E811-BDA9-14187763663C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/447DAD40-25CD-E811-85C5-509A4C748A71.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/202AE031-19CD-E811-9E72-0CC47AD98D74.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/8CC91C59-EACD-E811-9491-0025904C66A2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/28B1C8D0-16CD-E811-A9A5-E0071B6CAD00.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/2E6B5F9C-A0D0-E811-82A6-008CFA197E74.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7042B63B-20D3-E811-9E1C-0CC47AF9B1DE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/64857E2E-0BD3-E811-A584-0025904C6620.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E8CEF6EC-15D3-E811-9EBE-0025904C5DD8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/96FAB022-56D3-E811-BD89-0025905D1D78.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/16ECCA46-56D3-E811-80FB-0025905C5488.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/5087125E-F0D2-E811-B383-0CC47AA478BE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1C2A31A6-3DD3-E811-962F-7CD30AB18982.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/78E92D77-40D3-E811-852D-7CD30AD08D94.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B0AFD095-26D3-E811-8277-AC1F6B0DE30C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/46271896-26D3-E811-B707-48FD8EE73A85.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2E465F6B-08D3-E811-A0A9-506B4BB134F6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6499D489-27D3-E811-8AA5-EC0D9A8222CE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/980356C4-27D3-E811-8644-EC0D9A82237E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AA804507-D9D3-E811-AFF4-24BE05CE1E31.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D458F53E-5ED3-E811-B71F-002590D9DA9C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/92669EBB-5DD3-E811-8C0C-0025901AC3EE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8236B35C-B5D3-E811-952F-0025907DE278.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6892284B-B5D3-E811-B625-00259075D6B4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E010A714-54D3-E811-84AB-0CC47A13D110.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0E0CF083-54D3-E811-8FDE-0CC47AA989C6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5CFAE9BE-B9D4-E811-8F24-0CC47A2AECFA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E4FFECBE-BAD4-E811-A2F8-B499BAAB50A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/421A9242-BAD4-E811-8E28-509A4C7480D6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2C3A6F31-C6D4-E811-9D8D-0025904CF764.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/22FA2FAE-B9D4-E811-8583-002590909092.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C46C9876-BAD4-E811-84BD-A4BF010256DF.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/58BBDDEE-BAD4-E811-80BE-002590E7DE26.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/604A35F7-B9D4-E811-8767-48FD8E28297D.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/70E3A9BC-BDD4-E811-B85A-A4BF0112BBD6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4C62E303-BAD4-E811-B2BC-5065F3812291.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5A3E6297-36D4-E811-A61F-20040FE94288.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CAD226B4-04D5-E811-9A1B-141877411D83.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/22C064A3-BAD4-E811-8DB4-0017A4771070.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/26B41597-B9D4-E811-A8C2-0CC47A7EEE76.root',
] )













