import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BADC55DD-DC96-E811-8496-A0369F310120.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E07B1C7E-159B-E811-98FC-AC1F6B1AEF94.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/DE8533EB-979B-E811-91D2-C4346BC87798.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8A181DEC-369C-E811-8759-A0369F83630C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0CA66193-9A9C-E811-A8D5-C4346BBCB408.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F20F767F-429A-E811-9697-3CFDFE63CD00.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F055DA24-189A-E811-9BB7-0CC47A4D7636.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8693DA8D-169B-E811-B70C-0CC47A7C3412.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/16F414D3-E19B-E811-AA7E-0025905B85CC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A8B3BEC9-949C-E811-A887-A4BF0112BE3C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/600C8ED7-009D-E811-A0C2-FA163E942E01.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4839C99F-019D-E811-84F5-FA163E76E4F3.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7044E8A2-019D-E811-B706-FA163E924530.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7064E3B4-019D-E811-B71D-FA163E498C7B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/62D0CE80-559D-E811-8285-FA163EFBCBE7.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/DCEB7564-369C-E811-BEFE-24BE05C648A1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A6E3FBF4-359C-E811-8983-E0071B7A45D0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/1EEA995F-369C-E811-8170-24BE05CEEDA1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/943B1E7E-5C9D-E811-9B3A-24BE05BDCEF1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/522DFA99-659C-E811-9805-0CC47A7C3472.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EAF6A495-8F9C-E811-98E8-0CC47A4D7618.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D03D2B44-929C-E811-98DC-0CC47A78A340.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BCDE7BAA-859C-E811-AAFF-0CC47A4D7678.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5EFBE52E-929C-E811-9211-0CC47A7C35F4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/983FB50B-F99C-E811-B2A6-0CC47A4C8E0E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D4F46C66-319D-E811-AF84-0CC47A7C3408.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/02BEAA01-2A9D-E811-B129-0CC47A7C35F8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D278D3EE-299D-E811-ADC6-0CC47A4D7650.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EA3ED34F-819D-E811-922D-0CC47A4D7654.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A83E6E6B-3F9D-E811-81A7-0025905A6104.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/C62DD723-35AB-E811-9D7D-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/630000/C022C42B-F6BF-E811-965A-0242AC1C0504.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/630000/82D902AE-FDBF-E811-8B19-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/630000/7E67AE18-F9BF-E811-8466-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/BE8DCF4C-65C0-E811-809F-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/6ABFDFDE-6CC0-E811-8161-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1230000/A898BFF9-F6BF-E811-8DD2-0242AC1C0505.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1230000/00CCF914-F3BF-E811-84D5-0242AC1C0501.root',
] )




















