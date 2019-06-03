import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/141F8836-7C1B-E811-AAC8-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/CC86A831-7D1B-E811-B11B-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/F6CCFFB9-3C1B-E811-99B0-24BE05CE2EE1.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/0229F2A2-071C-E811-B753-4C79BA180A01.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/4AD7E0E9-BC1C-E811-B08A-E0071B7A6670.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/BE231017-311D-E811-A4AB-0025904C7B26.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/78F7EC4D-161E-E811-BA30-001E67504A65.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/6841FBE4-FA1D-E811-A16A-008CFAF74E6A.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/FCFB3502-291C-E811-818F-38EAA78D8B54.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/F260F37A-381C-E811-B288-38EAA78E2C94.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/86DE8F77-D21D-E811-B469-984BE164D07A.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/8A92246F-E31D-E811-8AD7-3C4A92F7DD0C.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/140BD642-0B1E-E811-8119-8CDCD4A9A484.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/E2DFEEC5-801E-E811-8DB0-3C4A92F7DD0C.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/08F53DF1-0E1C-E811-94F2-6C3BE5B5B078.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/ACB69933-471C-E811-B238-0CC47A4D765E.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C8285EF8-561D-E811-A90F-0CC47A4D767E.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/8C589FB9-291D-E811-BC15-E0071B741D70.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/2EE1C6DF-661C-E811-BB56-A4BF0115964C.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/3CE3D250-4C1D-E811-BFCB-A4BF0112BBF8.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/42486B52-0A1E-E811-AA0E-68CC6EA5BE3A.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/628FC4C2-341D-E811-87EC-A0369F836342.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/90000/728DFB06-0825-E811-BD4A-008CFAE45264.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/90000/FC380306-0825-E811-AD9A-008CFAC94260.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/90000/C2018DB4-FB23-E811-8536-FA163E9BEDA1.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/90000/4077ACC8-FC23-E811-BA10-FA163ECD3B69.root',
'/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/90000/ECD29B75-F126-E811-B88F-B083FED00117.root',
] )


