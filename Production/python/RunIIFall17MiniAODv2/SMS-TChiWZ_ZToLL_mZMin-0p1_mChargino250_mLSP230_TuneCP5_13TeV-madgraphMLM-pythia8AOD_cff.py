import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/80DFC5F4-0B7C-E811-ABE0-90B11C2ACF20.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/98C2D314-667B-E811-A2A4-064F6A0002C8.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A06EBA9A-8F7C-E811-9A1A-FA163E680BEE.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/08613DB8-817B-E811-9565-1866DA890658.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/38F948A3-817B-E811-97AA-0CC47A0092D0.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/622B0AA7-E77B-E811-BEFA-001E67E6F8D7.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C4610EFF-0B7C-E811-A906-0025904405AC.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E49DBEC6-887B-E811-892E-44A84225C7BB.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/202411D2-587C-E811-B6D6-0CC47AFC3C80.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9CFF4FB0-FF79-E811-BB90-FA163E0CD754.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6C7262CA-C779-E811-9F9B-FA163EB6C63A.root',
'/store/mc/RunIIFall17DRPremix/SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/18AB3C9E-757A-E811-B3D7-FA163E4A2D1C.root',
] )












