import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C0B49A6A-C495-E811-9AA7-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1EF42155-DC96-E811-8677-24BE05C4D851.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/204E3A0F-DB96-E811-9F74-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FEAEF461-C998-E811-ADF2-00266CFEFE08.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D43C97C6-F899-E811-8F69-90B11C27E141.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C6FA26E8-6F99-E811-953F-0025905A60F4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/00BE65D7-CB99-E811-BDCC-001E677923B6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BE1AE0BC-C999-E811-A0AE-002590207C28.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7E33F51A-CE99-E811-9824-0CC47AC08BD4.root',
] )



































