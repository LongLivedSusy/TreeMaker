import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/60B78CE0-E5B9-E811-BEB8-0025904C51FE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/2C264CD7-E5B9-E811-994B-0CC47AFC3CA0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/763419E9-E5B9-E811-93D5-00145EDD75E9.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/6288111F-6FB8-E811-8082-001E67E33C6A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/9C70121A-6FB8-E811-B3E5-A4BF0112BC2A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/2C78B872-6EB9-E811-9A8C-7CD30AD09D24.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/AE1CFAEC-68B9-E811-9AA7-1CB72C1B2D84.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/9EC30DE3-E5B9-E811-A6B7-6CC2173D8740.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/E402935E-6AB9-E811-8008-7CD30AD08E8A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/AA51CC91-6BB9-E811-95CC-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/A827D91B-6AB9-E811-A296-A0369FE2C152.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D41088B1-60C8-E811-A501-A4BF011255B8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/1AA6E04C-41C8-E811-83FC-008CFAF5543A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/1CC0A0FF-1BC8-E811-8F0F-0026B9278651.root',
] )



































