import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/F02A20F2-EEE9-E811-9912-24BE05C4D851.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/B4CDDAEE-EEE9-E811-9D9E-24BE05C4D851.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/044ABAED-EEE9-E811-AC9A-E0071B698B11.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/CEC3B1EE-EEE9-E811-BD0E-E0071B698B11.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/E6CD8ABC-EEE9-E811-951D-EC0D9A809802.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/FA90C8BB-EEE9-E811-B110-EC0D9A809802.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/9CA6C1BF-EEE9-E811-846F-EC0D9A809802.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/92343AFF-66EA-E811-AC07-000008FEFE80.root',
] )
