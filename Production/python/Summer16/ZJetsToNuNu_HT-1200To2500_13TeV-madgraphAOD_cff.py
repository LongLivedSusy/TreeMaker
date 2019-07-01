import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/36EBEC56-DAB9-E611-B42A-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A6840964-DEB9-E611-B0FE-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/90F25969-E0B9-E611-88FC-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9E44AA10-E3B9-E611-9DE8-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/60FFD683-E4B9-E611-AC21-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2E141A8C-E8B9-E611-AD9A-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EA5831E6-E9B9-E611-94ED-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/22908B45-EEB9-E611-BAD7-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A08381AF-EFB9-E611-8ED0-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/168EBFA5-C7B9-E611-A98F-B083FED14CE0.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8440413C-DAB9-E611-9719-1866DAEA79A4.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1A1906BC-DBB9-E611-B112-1418774118F6.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/12A64257-DEB9-E611-909C-141877411FED.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/34EFDD80-E0B9-E611-AB72-1866DAEA6CC4.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0A2E3B69-E0B9-E611-8818-1866DAEA6D0C.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F2CA52C3-DFB9-E611-AE47-1866DAEA6D08.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8646781E-E1B9-E611-8F96-1866DAEB5C94.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F0687F85-DCB9-E611-A0F7-001EC94BFB57.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/229C96B3-E1B9-E611-AFB2-141877411FED.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/843232D8-DDB9-E611-8386-90B11C0BD48B.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1C0AE728-E1B9-E611-A5C0-1866DAEA8218.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D29BF227-DFB9-E611-863E-A4BADB22B465.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2293CAFF-E2B9-E611-BF73-1866DAEB3628.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7437A85E-E2B9-E611-A517-141877410522.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/78D8E5B1-E3B9-E611-9AAF-141877410EC1.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4CCBF3B9-E3B9-E611-ACEF-D4AE526DF000.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/30191B88-E4B9-E611-8E77-1418774120C3.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC119661-E4B9-E611-B378-C81F66B78FF5.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC1B6320-E5B9-E611-A01D-1866DAEA7E64.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/52DCD521-E7B9-E611-BC46-1866DAEEB358.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/960E6477-E2B9-E611-BB4E-001C23BEBF16.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B874B66B-E6B9-E611-9D20-B083FECF837B.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/704EA2EC-E7B9-E611-937D-141877410EC1.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/704A7559-E8B9-E611-AAF1-1418774120C3.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DAFF1E35-E9B9-E611-BE8C-1866DAEA6E00.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F6FB6A54-E8B9-E611-B0DF-D4AE526DF000.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4AC59835-E9B9-E611-BDB2-141877411FCD.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5EAB40E2-E5B9-E611-BD20-B083FED42A1A.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C401107F-EAB9-E611-8D76-1866DAEEB358.root',
#'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6861BAFC-EBB9-E611-98ED-141877411FCD.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B4643334-E7B9-E611-94A0-001C23BED42C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/38F7832C-E7B9-E611-8136-001EC94B51D5.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D88AE392-E8B9-E611-9024-B083FECFEF7D.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A8D6D056-EEB9-E611-86B4-001EC94B51D5.root',
] )











