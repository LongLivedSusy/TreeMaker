import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/16424AC7-C2BD-E611-99B4-1CB72C1B2D80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/481667D4-C4BD-E611-AE5C-1CB72C1B64E6.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B61CAA2F-C6BD-E611-B57E-002590FD5838.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C28B22CC-C7BD-E611-B90A-34E6D7BEAF0E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C142761-C8BD-E611-87EB-1CB72C1B65D4.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/50168C5F-CBBD-E611-B22B-002590FCF738.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/ECC439D1-CABD-E611-BDD2-90E2BACBAD64.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B404F740-CDBD-E611-86A9-1CB72C1B64E2.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/10D84D7F-CCBD-E611-8D4F-002590FD030A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E08F1430-CDBD-E611-BF8D-002590FD5E82.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C279B52B-CEBD-E611-A976-002590FCF738.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AA938FB6-D0BD-E611-933D-002590FD030A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/029179EC-CEBD-E611-ADA3-90E2BACBAD64.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D485432E-CFBD-E611-B295-90E2BACBAD64.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/38DDFAD0-CDBD-E611-B5AE-68B59972C49E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/860FB03C-D2BD-E611-A402-002590FD0F3E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E6FADC8E-D0BD-E611-A76E-D8D385AF8A16.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8458DEB3-D1BD-E611-9E50-1CB72C1B2D80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0083A7F0-CFBD-E611-98A5-68B59972C37C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2ED2A8AF-D3BD-E611-BEEB-90E2BACBAD64.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/10F9F75C-D3BD-E611-A9CC-D8D385AF891A.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5493DB68-D3BD-E611-9AB3-002590FD583A.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E8D854D6-D6BD-E611-9D9A-90E2BACBB038.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DC06B618-D5BD-E611-922C-34E6D7BDDEDB.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2A51193F-D6BD-E611-A29C-D8D385AF8A16.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F8A2BA37-D6BD-E611-9603-002590FD0F3E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BCADDA90-D4BD-E611-BEAD-68B5996B46D8.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/828E0BAB-D8BD-E611-8FA9-002590FD583A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8A383248-D6BD-E611-93FA-68B5996B46D8.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0CFCFA05-D8BD-E611-B3F1-B499BAABD022.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/761A896F-DABD-E611-9958-1CB72C1B2EF4.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9C664C05-D8BD-E611-885B-D8D385AF891A.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5AD7A59F-DDBD-E611-9C42-1CB72C1B2EF4.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C08144E4-A7BE-E611-AB76-68B5996B45F8.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A4B4F640-18BF-E611-AB8F-002590FD0F3E.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/40C918DE-C2BD-E611-8CB4-0CC47A4D76B2.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D470C4EC-C2BD-E611-B8AF-0025905A6088.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5ADCDC94-C5BD-E611-B727-0025905B8574.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C4855073-C9BD-E611-9AF8-0CC47A78A340.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7CE3FB3F-C8BD-E611-A3A5-003048FFCBB8.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3C22BC5E-C7BD-E611-89D2-0025905B8580.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A0A5374B-C8BD-E611-92CF-0025905A6088.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D8C73E95-CCBD-E611-9D35-0CC47A7C3432.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E2061064-CABD-E611-8C8B-0CC47A78A4B0.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/18CBE387-C9BD-E611-81BE-0025905A60DA.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9C2467DE-CBBD-E611-94F6-0025905A6066.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B63F15CA-CABD-E611-BAB5-0025905A613C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0600C8FA-CCBD-E611-9F2B-0025905B8580.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2884607E-CEBD-E611-90E4-0CC47A4C8E96.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE28147E-CFBD-E611-BC60-0025905A60DA.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/48DE064D-CBBD-E611-B216-0025905A48C0.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88652D8E-CEBD-E611-BDE6-0025905A497A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AC38E0A8-CDBD-E611-ABAB-0025905A6088.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4A756A5A-D0BD-E611-B1BF-0CC47A4D76CC.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5276720C-CCBD-E611-A606-0025905A6110.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A8910999-D2BD-E611-BC3A-0025905A48C0.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/249623C2-9ABE-E611-A857-0CC47A4C8ECE.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/641C941C-A0BE-E611-BC10-0025905A4964.root',
] )













