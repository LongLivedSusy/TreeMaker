import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/4A715DCC-44BE-E811-B228-48D539F38636.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/74921280-45BE-E811-B7FA-48FD8EE73A7F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/74B651A4-45BE-E811-B2D8-AC1F6B0DE3E8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/0A42C65E-45BE-E811-A17A-48FD8E282487.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/FA169B01-9FBE-E811-AC82-0090FAA57460.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/7415428C-8FBF-E811-BE4C-0090FAA57AF0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/B8FE0E9F-79BE-E811-98B4-E0071B73C640.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/82068099-8CBE-E811-93E1-24BE05CEEDA1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/58F21D85-CCBF-E811-82F0-5065F37DC1D2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/3C8E8FE4-C2BE-E811-87B8-0CC47A2AED0E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/3CEF251D-C5BE-E811-90FC-0CC47AD98F6A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/265EF33D-FBBE-E811-9291-90B11C2C93C9.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/3C29A056-D1BF-E811-8906-002590489776.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/2A53F529-AABF-E811-8D2B-0CC47AD99238.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/F02ADE1B-AFBF-E811-81FE-008CFAE45410.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/BA821AEA-AFBF-E811-A61E-0025905487CE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/6A8B64D2-C9BF-E811-879A-3CFDFE63EC80.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/12CE1B13-8BC1-E811-94D1-1866DA85D967.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/AE7BD052-C0C1-E811-99C6-E0071B73C640.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/9EE86C78-14C2-E811-A95B-24BE05C64601.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/8ECA2511-A0C2-E811-A977-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/7C652231-DAC4-E811-BAD3-AC1F6B0F6752.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/321CCD21-DCC4-E811-8A78-48FD8E282481.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/6E8605F7-40CA-E811-9D6F-0CC47AA99070.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/B8D68788-83CA-E811-9533-0CC47AD98CF8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/B8E3C790-83CA-E811-92AC-0CC47AD98CF8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/E64C5822-1ACB-E811-BD55-90B11C26815F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/4C5D2221-8BCA-E811-A2B0-008CFAFBF52E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/FCF064F4-8BCA-E811-B27F-A4BF01158940.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/B098BCCE-8ACA-E811-8E47-F01FAFD9CCDC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/723161A7-8ACA-E811-B479-20CF3019DF19.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/065E4FC1-8ACA-E811-B825-A4BF0102611B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/B079C6FC-20CB-E811-8333-549F358EB7BD.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/1ABDC904-8CCA-E811-A642-246E96D14AB0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/A8CCB897-8ACA-E811-A0E1-E0071B74AC10.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/427B6164-21CB-E811-BED9-008CFA197418.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/AAC33BEB-56CA-E811-8B79-0CC47A4C8E64.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/D041614D-6CCA-E811-9B56-0CC47A4C8E86.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/BC481323-60CA-E811-9032-0CC47A4D75F4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/CE780EDC-69CA-E811-88A4-0CC47A7452D8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/70FF887C-8ACA-E811-8AD4-0CC47A7C3604.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/6AC6531C-B4CA-E811-8A9E-0025905B8580.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/7A96B2D4-20CB-E811-8691-0CC47A4D767E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/36E65A25-21CB-E811-A317-A0369FD2068C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/F0101009-21CB-E811-BC7D-34E6D7E05F28.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/0EA194F9-20CB-E811-955E-509A4C781389.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/9CB33CF7-20CB-E811-B113-0242AC1C0501.root',
] )









