import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2CC9743F-A9F6-E611-AD32-02163E01A7B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CC937F8E-A8F6-E611-85F9-FA163ECF1EE2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AE165D57-D4F6-E611-8C01-FA163E96A35E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/26ACE77D-CFF6-E611-A6C6-FA163E641FB4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/761B0A83-CFF6-E611-AC40-FA163EF85254.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6087F181-CFF6-E611-9A10-FA163ED33CBD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/96E6965C-00F7-E611-ABBD-02163E01A83A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/086AD695-00F7-E611-B3E6-02163E013DFE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F05E3B59-00F7-E611-ADB9-02163E011598.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E05350C4-04F7-E611-95ED-02163E0161F9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BEF7CE4B-DDF5-E611-8500-FA163EB43C1A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AC418689-D8F5-E611-8352-FA163E41D172.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4A542C4C-E7F5-E611-866F-02163E00C997.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6C85087B-DEF5-E611-AE6F-0CC47AC08816.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3E5494BE-F0F5-E611-BAFB-002590DE6E92.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D65288CC-D4F6-E611-83BC-842B2B76670F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6E081961-A3F6-E611-9757-20CF3027A59F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CA4E6E74-42F7-E611-B7E0-0CC47A78A414.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6A677FAA-42F7-E611-BD60-0CC47A4C8E46.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/78D6BB2F-5FF6-E611-9469-6CC2173BC2E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/54B60214-5FF6-E611-BF9D-00266CFEFF04.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/50CFE2A6-63F6-E611-BE15-C4346BC7EE18.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/848929A4-63F6-E611-887C-00266CFFBE14.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/50FA21AB-63F6-E611-BC7A-00266CFFC6CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/06903327-6CF6-E611-8C93-C4346BC08440.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8F4D16F-6CF6-E611-9CE3-A0369F8363BE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E4204374-23F6-E611-9A90-848F69FD29B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D4476978-23F6-E611-B8FA-7845C4FC3C83.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4E1E97F9-28F6-E611-8F6F-3417EBE64591.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/542F7CAD-37F6-E611-8948-008CFAFBE7DE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1476FE36-D4F6-E611-A834-848F69FF914E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F29066D4-FEF5-E611-B841-001E67E6F52B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C64705C-C7F6-E611-AC92-002590FC5ACC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/64376190-D4F6-E611-BC99-001E67E6F8E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9EE5A96F-DEF5-E611-84B9-7845C4FBBD07.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C0BD81F6-A7F6-E611-B6CB-7CD30ABD278A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A8B22089-A8F6-E611-99C1-44A842CFC9E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90476634-9AF6-E611-B901-D8D385AF8AB2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9247E8A1-EFF5-E611-B9FB-F832E4CC4E51.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FEA96BC7-F5F5-E611-A89C-F832E4CC4D39.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B2CED0F6-FBF5-E611-A47F-0023AEEEB538.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C078C3F6-FBF5-E611-8AA1-0023AEEEB538.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3E833882-09F6-E611-8CB8-0026B9277A4C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E8EC7E78-09F6-E611-AAA8-0023AEEEB559.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BA85F263-03F6-E611-A0E2-0023AEEEB79C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/00CE3513-0FF6-E611-9B1F-0023AEEEB559.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D4F887FC-15F6-E611-B1C8-0026B94DBDA2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9022DB67-1CF6-E611-8486-14DDA9D4F20C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BEEC85D3-A3F6-E611-BED6-00259021A3D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5CEDC274-09F6-E611-BD6B-C4346BC8C638.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/88961DFC-15F6-E611-BFDE-C4346BBC1498.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0491267B-1CF6-E611-B6C0-00266CFFC76C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AA85754A-31F6-E611-845D-A0369F836400.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9CF8E15A-4AF6-E611-9A7F-00266CFFBCB0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A3EBFE1-51F6-E611-AE57-6CC2173BC2E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A03304DE-51F6-E611-B802-A0369F836364.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/56D7A0D6-58F6-E611-9692-6CC2173BC2E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6A661DDA-58F6-E611-A387-C4346BC78D10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9ACBC439-A3F6-E611-A88A-002590E7DFD6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E8B42A17-B0F6-E611-88CB-0025904C66E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B01BC1D6-EAF5-E611-934D-A0369F7FCA68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/74DE4791-B8F6-E611-AFB7-A0369FD8FDB0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4807F44A-51F6-E611-ABED-0CC47A7FC7B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9AC27F52-51F6-E611-974B-0CC47A7FC4F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C8096641-D4F6-E611-957E-0CC47A7E00A8.root',
] )
























