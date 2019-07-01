import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C269F8F7-3D1B-E811-92CE-141877410EC1.root',
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/A8F05E92-BB1B-E811-ACD9-5065F37DC042.root',
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/20DE7D6C-7B1B-E811-9982-0025905A60DA.root',
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/48B6EC85-481B-E811-A307-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/184653F6-481B-E811-82A7-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/8CC5DBBD-C81B-E811-9F87-A0369FC51BB8.root',
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/AC051A19-3E1B-E811-9E91-002590E39D52.root',
'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/72FAE819-B71C-E811-84FD-002590E7E050.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/DED183C6-CC1C-E811-87F7-002590E7DFA2.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/60000/C2FEF9D3-B21F-E811-9477-0025905B85E8.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/60000/0000E3D2-1C20-E811-92B4-0CC47A4D75F6.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C4751E3D-551C-E811-9FB9-00215A4509DE.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/72D24982-CE1D-E811-A814-8CDCD4A9A484.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/14089660-131D-E811-A9EA-00269E95B128.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/885FA7D8-321C-E811-B5CC-FA163ECCD70C.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/90FF4641-321C-E811-9AF3-FA163EDE7FEA.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/E8115FB2-FC1C-E811-AC5A-FA163E0F2333.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C0AE0F15-291D-E811-8894-02163E00C17A.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C2C26522-041E-E811-818F-FA163EE67239.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/9060EC6B-191D-E811-8ED3-008CFA1C9308.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C8526E4E-FF1B-E811-BA93-001CC4160632.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/70F812B4-F01D-E811-AA69-7CD30AC0301A.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/E0919852-2D1D-E811-80C0-001E67E7195C.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/9A6F5DD0-ED1D-E811-9B4F-A4BF0112F7C0.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C43E5821-271D-E811-8772-001E67E6920C.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/4A07981E-DD1C-E811-85C1-00259021A53E.root',
#'/store/mc/RunIIFall17DRPremix/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/06EC231A-E61D-E811-A59F-20CF3019DEEF.root',
] )











