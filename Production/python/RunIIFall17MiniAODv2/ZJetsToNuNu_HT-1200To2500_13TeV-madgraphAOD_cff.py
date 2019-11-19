import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FEB9461C-7409-E811-89F6-5065F3819241.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8C033920-7409-E811-9153-E0071B73C610.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A2E54033-B609-E811-8D87-02163E0144D1.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A063D937-B609-E811-878E-02163E01A3B9.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F0F9336D-A409-E811-95CC-02163E014715.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/DEC15275-A409-E811-983F-02163E019D88.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/4ABAA04C-D409-E811-A6A8-02163E01A72C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/54D2334C-D409-E811-8B96-02163E01A2B5.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/CC207905-190A-E811-B2AC-02163E01A2F0.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/EA9FD7A3-650A-E811-AE12-02163E01A5B1.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/80189B95-650A-E811-84B6-02163E01353B.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A02ABF01-D208-E811-9413-0CC47A13CEAC.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/D0FBB620-4109-E811-87FF-0CC47AA99438.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/D2C9C8EA-D108-E811-9649-0CC47A6C1054.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F42BC121-4109-E811-96BD-0025900B20E2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/486D0AD6-5B0B-E811-BA5F-0CC47A4D7654.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/BE3B3E30-5C0B-E811-87ED-0CC47A7C35B2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8E7EE756-BC09-E811-861D-FA163EE6B824.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/568A126A-BE09-E811-AE61-FA163E504E41.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A876D224-F40B-E811-AADC-02163E019E01.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/80000/4ECA6968-A512-E811-B4DF-44A842B2D631.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/80000/E4BB5307-EA12-E811-A549-44A842B420F1.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/80000/383FC612-EA12-E811-B422-008CFA1CB8A8.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/80000/122AD70A-EA12-E811-9FC0-001E67504445.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/C485B93B-C110-E811-A642-90B11C27F8B2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/626B5F2C-2411-E811-ADC1-44A84225CFF0.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/C84D2933-2411-E811-AB8E-3417EBE64696.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F25615FA-C010-E811-B513-24BE05C63721.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/88906BB1-C010-E811-A6A8-FA163E61009F.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/7AF7E8B7-C010-E811-BDAB-02163E0120D2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/44C6EF84-1E0F-E811-AC68-0025905C42F2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/52D61DA4-1C0F-E811-A858-0025905C5500.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/30407B12-C110-E811-B7BB-C81F66B782DC.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/54937461-2411-E811-8BAD-008CFAFBE6B2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/343D11F9-C010-E811-B680-0CC47A7C3430.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/20000/CC3ADA49-0F18-E811-B1FA-02163E01A464.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/20000/68836E58-0F18-E811-96CF-02163E0140E5.root',
] )

































