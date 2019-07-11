import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/A64110CB-C0B9-E811-8AB4-B496910A9A68.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/FEE609B1-C0B9-E811-B93A-0CC47A7C3404.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/D8C1B9F1-C0B9-E811-BA92-A0369FD0B38E.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/BA795831-C1B9-E811-B25B-008CFAF558E0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/E89F913F-C1B9-E811-BABE-008CFAF2224C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/1A4D2CD5-33BA-E811-A50F-90E2BACBAE58.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/4C94C462-C8B8-E811-ACA5-0025905C2CB8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/E261C2F9-15B9-E811-9E31-0025905C53B2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/22717439-16B9-E811-BC45-0025904CF764.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/A083BFFA-D7B9-E811-8E92-0025905C4262.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/B0FDBA82-C0B9-E811-BEDF-0025904C51FE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/0A066B94-FCB8-E811-A1F7-0CC47AD98B94.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/461E09B1-D8B9-E811-8D42-1C6A7A264EC9.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/82CC4974-C2B9-E811-8D2B-509A4C72D497.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/1C498C6C-C1B9-E811-A820-A4BF0108B162.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/F2D37BFE-33BA-E811-BFF6-0CC47AA53D64.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/FE6C3634-F0B8-E811-9389-5065F3818281.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/60E6AA54-F3B8-E811-A024-E0071B7A8550.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/569D4AF3-C0B9-E811-ABE2-24BE05CEED81.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/3C9579C7-36BD-E811-9C66-44A842CF0600.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/1C4B6D1B-34BA-E811-8FC5-44A842B4210B.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/3C056879-CDC0-E811-BC40-44A842CF05F3.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/40CF049B-CDC0-E811-B656-B499BAAC0658.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/5E33696D-E7C0-E811-A917-44A842CFC98B.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/264EC9D9-23C1-E811-8B29-B499BAAC3786.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/BC013EF7-E3C0-E811-A214-B499BAAC055E.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/24A8CAD0-D7C1-E811-A16D-6C3BE5B56498.root',
] )















