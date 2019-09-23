import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/32330D3B-50EA-E811-B20A-5065F381C1D1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B218D8B5-7CEA-E811-B963-EC0D9A822396.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/8AD70081-7EEA-E811-B853-24BE05BDAE61.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4AC4E117-7DEA-E811-9C15-EC0D9A82264E.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/620BC2C2-83EA-E811-A6FE-24BE05CEDCF1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/886D8129-80EA-E811-B20C-5065F381D2C1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/C0194CD2-7DEA-E811-AC35-24BE05BDBE61.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/286D02B8-0CEB-E811-9D6C-E0071B7A45D0.root',
] )
