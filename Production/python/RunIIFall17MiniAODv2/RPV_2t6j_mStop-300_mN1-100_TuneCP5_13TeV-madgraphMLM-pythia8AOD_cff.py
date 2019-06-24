import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4EFE85AE-0C97-E811-B003-E0071B7AC5D0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/DCA2C408-1F9B-E811-8FFA-20474791DE54.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CEB7F2CD-8C9C-E811-83A5-B49691091EA2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/98ECCF23-0D9A-E811-B4D8-24BE05C68681.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6C3113BB-149A-E811-BDCD-24BE05BDBE61.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3CE68C3E-159A-E811-B0FA-24BE05CE3C91.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E803C855-949A-E811-A8F4-24BE05CE1E11.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2CF39920-009B-E811-86AC-EC0D9A82262E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/368CE329-1E9B-E811-AD16-EC0D9A80980A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/62C07D32-489B-E811-BC81-24BE05C48821.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7638B311-489B-E811-BC6E-24BE05C49891.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5023780F-489B-E811-93E5-E0071B7A4550.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E4F5F30E-489B-E811-82FA-24BE05CE4D91.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/1CB66B2B-C09B-E811-AACA-5065F37D01A2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F6AF2BAB-C59B-E811-AE74-E0071B7AF7C0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/58F2BE52-F59B-E811-936B-24BE05CE3E61.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C0C7AEB8-FD9B-E811-B059-24BE05CEFB31.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E461C591-F59B-E811-8479-24BE05C618F1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/84AB8961-F59B-E811-BF1F-5065F37DD491.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7C758260-F59B-E811-B3AB-E0071B7A5540.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BA40585E-F59B-E811-9115-24BE05C33C61.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/243FE36A-189C-E811-929B-5065F38192D2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/80972362-F59B-E811-BF19-5065F381A2E1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/868E50B5-CD9B-E811-8F35-1866DA87B230.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6237314B-C89B-E811-8D13-842B2B766242.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AA3E2C32-E29B-E811-92EB-D4AE526A092E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9C55DD6E-2D9B-E811-A932-A0369FE2C0E2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9C946070-2D9B-E811-AFD3-A0369FE2C11C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5AC2B6B8-349B-E811-BFD5-00259029E81A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C29851AA-469B-E811-B747-0007432CAA50.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5A9D6F94-C99B-E811-AA88-0CC47A57CDD2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D4F36489-F59B-E811-9BFB-002590D9D98E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D8FA9A22-C59C-E811-92FE-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/449EF8AE-DF9C-E811-94B1-A0369F83627A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8E69F6DC-DF9C-E811-A639-3417EBE64426.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/FC230639-9D9B-E811-BD1C-001E67792810.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/966E0F5D-9F9B-E811-A81E-001E6779248C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2AC5FFA9-9F9B-E811-94BD-001E677924CE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C8F9B068-B19C-E811-9355-001E67E71D03.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BE21122A-9A9B-E811-94EC-008CFAC9410C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/766499F7-E09B-E811-B4BF-801844E561C0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/FAF819C7-329B-E811-BD4F-1C6A7A26CA0F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/12E9FAE2-469B-E811-8C71-0CC47A13D416.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/604299DF-DF9C-E811-B9CF-1866DA8F73E2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EA79B57A-129C-E811-A67E-0CC47A7C347E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/42C10840-C89C-E811-B969-0025905A60DE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/30111DFE-349D-E811-89BE-002590E7D7EA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F43989E1-DF9C-E811-901D-001E6757F1D4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B2143446-489B-E811-B63B-001E67A3EAB1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/765FC1E2-F59B-E811-A6F9-001E67DDC6C8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B45BE1ED-349D-E811-8C6F-0025904E9012.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E6CD0813-E09C-E811-ADE7-D48564591B64.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/922B9AEE-8C9C-E811-9158-001E67443F66.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/066D8185-F59B-E811-89C4-E0071B7AC700.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/28D560D6-DF9C-E811-9296-0CC47A5FC61D.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6A441089-F59B-E811-BE4F-008CFAE4537C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E0160D67-F59B-E811-82DF-008CFAC9409C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D47734CD-DF9C-E811-B225-008CFAC91A00.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B4C2854F-C89C-E811-B982-0025901E1158.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/18A52186-8C9C-E811-A332-14187729F16E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/868FFFF4-07A9-E811-A060-EC0D9A0B33A0.root',
] )








