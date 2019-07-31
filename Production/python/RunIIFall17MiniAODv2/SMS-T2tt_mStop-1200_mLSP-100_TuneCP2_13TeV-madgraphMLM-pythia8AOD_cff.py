import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/26663617-ABB8-E811-A536-AC1F6B0F676A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/3E1886C4-88B9-E811-A7E9-AC1F6B0DE30C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/E2278B34-32BA-E811-BB34-0CC47A4D7630.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/EAC1729B-32BA-E811-ABE6-008CFAF732F2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/9E581D09-EAB8-E811-90F8-0CC47AA53D6E.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/D8DD5366-00B9-E811-8C70-0CC47A0AD6C4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/3C01C9DD-7CB9-E811-BCD3-0CC47AA53D72.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/E27F1A42-57B9-E811-9758-0CC47AB0BDDE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/EE633398-D8BA-E811-940D-001E677927C2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/DC99E770-32BA-E811-8EB7-0CC47A6C1864.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/E2B07EFB-3EBA-E811-B13B-782BCB5364D4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/AA92F3B0-2FB9-E811-837E-24BE05CEFB41.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/A69123E3-30BA-E811-901E-E0071B7AC770.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/2EEC16A7-32BA-E811-A63C-5065F381B211.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/58DCD9EC-32BA-E811-A79F-0CC47A4DEE86.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/0A7AE31A-33BA-E811-9E39-B49691091EA2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/1C2D738A-32BA-E811-A64D-246E96D10B14.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/56E08AC1-32BA-E811-A6BA-F04DA275BFDD.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/010000/CEA7A988-F6C6-E811-AB52-002590D9D8A4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3CF21EAC-FAC6-E811-9614-001E67A4055F.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D6912381-CDC7-E811-BB6D-A4BF0101DDD7.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A40ACC98-62C7-E811-9636-0CC47AA53D8A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B66183AA-43C8-E811-BA11-002590FD5A52.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E0426BB7-C0C8-E811-8D21-001F29082E7E.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/12383729-F7C8-E811-9117-001517FB2238.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4CD65D8D-1BC9-E811-9548-1866DA87E080.root',
] )




















