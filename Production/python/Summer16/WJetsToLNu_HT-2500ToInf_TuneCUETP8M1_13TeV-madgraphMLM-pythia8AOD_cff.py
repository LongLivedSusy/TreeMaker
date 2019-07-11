import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/50334848-55C2-E611-9C65-001E67E719B6.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C2429C90-0FC2-E611-8D9D-FA163E05A8CA.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/728006FD-54C2-E611-B6E9-001E67E95A26.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/60C92B50-55C2-E611-B5ED-02163E015E4B.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0CF8B0C0-02C2-E611-AF7C-00259073E51E.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/86CD8E0D-0BC2-E611-BA10-B083FECFC6ED.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F6792A78-06C2-E611-90B9-C4346BC76CD8.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E8510E49-55C2-E611-A873-001E67F336A4.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0EAE4837-55C2-E611-B252-20CF3027A56A.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A8B40AC8-0CC2-E611-BF80-6C3BE5B51238.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3E43587F-5BC2-E611-B9D0-B499BAAC03BA.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2276808C-00C2-E611-AEFD-0025904C6508.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1ADD58DF-02C2-E611-9400-0025905C42A2.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/502F6DFA-54C2-E611-ABB2-0025904C51D8.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3AA36C06-0FC2-E611-9B22-0CC47A7DFC98.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E2B1661E-55C2-E611-8E31-0CC47A7E6BDE.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CE34E1E6-02C2-E611-A26E-008CFA000280.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4827544A-06C2-E611-A642-848F69FD4FB5.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/80B6EAFB-D7C2-E611-A2AC-180373FF8D42.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7CD015C7-CCC1-E611-9296-02163E011F3A.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/36434732-D1C1-E611-B714-02163E0118FB.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8AAA4945-D3C1-E611-93B0-02163E01442A.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/764A0CEB-D4C1-E611-BAFD-02163E011B5C.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8636183D-D0C1-E611-8A45-02163E011B06.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1E24A1D7-DBC1-E611-BFB0-02163E0137EA.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D23CB6B0-FDC1-E611-B086-FA163E1894DA.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D6D094EC-04C2-E611-9ACE-02163E0134BB.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/546D898B-01C2-E611-A93E-02163E014644.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8608B740-0BC2-E611-94E5-02163E0136E2.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/16580627-55C2-E611-A6FC-02163E01349E.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3E2E6213-55C2-E611-BC0D-002590494C8A.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/80CF37DF-07C2-E611-96EA-0CC47A7452D0.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2CC67ADA-08C2-E611-A8DE-0025905A60E0.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/96370604-55C2-E611-B016-0CC47A4D765E.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2E86501E-55C2-E611-8460-001D0967D4EA.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C6CD2014-55C2-E611-AAE3-0CC47AC08BC8.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/70EFD0FF-06C2-E611-8F12-F04DA27541F0.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/96E50370-5BC2-E611-B892-7CD30ABD278A.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E89DFDFB-02C2-E611-97AC-441EA1714E4C.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2429A308-07C2-E611-9202-68B59972C37E.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5C4B740B-0BC2-E611-8D6B-90E2BACBAB00.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/38402BA9-08C2-E611-8694-441EA173385A.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C6275071-0FC2-E611-BD2D-68B59972C37E.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1A6DC1E2-56C2-E611-84CF-1CB72C1B64E2.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7803994A-55C2-E611-8E45-00259074AEAE.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FCC89A6C-01C2-E611-8BBF-008CFA1CB73C.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0C18D60E-06C2-E611-BF00-549F358EB721.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F8D26883-0CC2-E611-A2F7-008CFA197D2C.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DED3E819-55C2-E611-B6B9-008CFA0646D4.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/226B62A9-02C2-E611-AEB8-0CC47A5FBDC5.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9A86DC07-55C2-E611-A256-002481DE4BFC.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC522B43-0BC2-E611-ACD3-002590E7D7CE.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC69721D-55C2-E611-A910-002590E7E07A.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/62A6E0BE-0CC2-E611-BBBF-F832E4CC4EB1.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F296D3EE-54C2-E611-AC5E-28924A33AF26.root',
] )















