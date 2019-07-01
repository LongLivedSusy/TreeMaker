import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/12ACC668-C170-E811-A1E3-44A842BECCBE.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4AFBEC03-3370-E811-98A0-EC0D9A0B3370.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/52113C2D-3370-E811-A8DF-001E67E69E32.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3ECD2314-C170-E811-A6BE-44A842CF05CC.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/34D7FFAC-C470-E811-8C4D-00266CFFC13C.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8829AA3A-7C71-E811-B7B3-FA163E92FDFD.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A48AC48D-F670-E811-9064-008CFA197E10.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/96A809C8-7F71-E811-A674-AC1F6B0DE4A8.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/825F979A-C370-E811-9ADB-002590D5FFF2.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/E4E98542-7C71-E811-ACCE-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/527BDA6B-7C71-E811-9A7F-68B59972C49E.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C61B6F5E-7C71-E811-A78E-F8C28867C7D9.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/566B1A44-988A-E811-A15B-509A4C83D54F.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/AE27C3F9-E38A-E811-8502-7CD30AD0A75C.root',
'/store/mc/RunIIFall17DRPremix/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0E635531-488A-E811-8DD5-F04DA2747854.root',
] )











