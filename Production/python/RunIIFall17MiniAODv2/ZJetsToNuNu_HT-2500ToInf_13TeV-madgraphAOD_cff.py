import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/BAE421CA-2F10-E811-9ED9-FA163ED7E826.root',
#'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/5A35489F-2F10-E811-8202-02163E013716.root',
#'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/16B3AA07-3010-E811-A7B9-0CC47AD99148.root',
#'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/9069B800-3010-E811-81CD-B083FED045EC.root',
#'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/1A24BBCD-2F10-E811-A4A6-0025905C54DA.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/54DB5B95-3010-E811-B106-24BE05C4D8C1.root',
#'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/C4BC9DEE-2F10-E811-AE4F-00A0D1EEEEC8.root',
#'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/00000/34745C9E-3010-E811-B510-0CC47A74527A.root',
] )


















