import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E876B945-63EA-E811-8736-AC1F6B0DE2F4.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F2921195-63EA-E811-A561-AC1F6B0DE224.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F65EF6B2-63EA-E811-970F-A0369FE2C0D2.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/8C3E359E-64EA-E811-AE15-AC1F6B0DE462.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/407AD7D8-6AEA-E811-87EC-A0369FD0B33E.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F0E08166-6CEA-E811-8724-A0369FD0B282.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/6CA53711-71EA-E811-ADAD-A0369FD0B2D0.root',
] )
