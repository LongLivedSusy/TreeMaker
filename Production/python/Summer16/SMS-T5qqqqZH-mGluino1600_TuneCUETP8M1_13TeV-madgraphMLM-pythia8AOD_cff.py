import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5CE01A47-FAF6-E611-B60A-002590A3711E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/34E07404-FCF6-E611-84A2-001E67E6F922.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/727DC64C-09F7-E611-AE4E-001E677927EA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2ADEE385-D0F7-E611-82AC-A4BF0108B872.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/42CDDC12-0CF8-E611-AE82-DEDBE4AC1313.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/0CA3B611-11F8-E611-A289-6CC2173BBED0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/1611E222-11F8-E611-9DD0-AC162DAB0B08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/0E28CAF0-0FF8-E611-B6A1-00266CFFBC60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/98C1706D-14F8-E611-817D-6CC2173BC0B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9C42726E-14F8-E611-BA59-6CC2173BC370.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C832532B-19F8-E611-9C56-6CC2173BC850.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E87A2503-16F8-E611-8299-C4346BC83480.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AE5E2A09-16F8-E611-B0CD-AC162DACB208.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2AA6546A-1CF8-E611-B501-6CC2173BC850.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9E4E2431-19F8-E611-B7C6-AC162DACB208.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F2EF16C2-18F8-E611-A4B7-AC162DAB0B08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/EA3DBA6B-1CF8-E611-A241-DEDBE4AC1313.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E6D30EE3-1DF8-E611-9C34-6CC2173BBA60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/201F99DD-1DF8-E611-871B-A0369F83637E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/76C7A7BF-1FF8-E611-A87F-6CC2173BC850.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CC52D4F4-22F8-E611-A363-A0369F83637E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/48B0496E-DEF6-E611-AD9A-E41D2D08E010.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2E0E4D8E-EAF6-E611-B7A5-002590DB925E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A0CB302F-F0F6-E611-AF0D-0242AC110004.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3CE376C2-EFF6-E611-ACBE-70106F4A93CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5A932095-F5F6-E611-9D62-047D7BD6DD9A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/008245D1-F0F6-E611-B98E-0CC47A7FC4F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B00E5E8A-F6F6-E611-A49F-70106F48B9A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F898B79A-F6F6-E611-804C-0242AC110004.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/0A44DD50-F9F6-E611-805D-0025907FD430.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2EDEC93F-FBF6-E611-B2AA-047D7BD6DE24.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6ED8A20A-04F7-E611-91DD-0025901D4932.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F4349773-CDF7-E611-A263-002590DB927A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F0D9EE41-02F7-E611-814E-02163E014A0B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B269045B-09F7-E611-9EED-FA163E5E764A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/682CE045-C9F7-E611-B387-FA163E8EFDC2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/848BACF2-D9F7-E611-874D-FA163E15C21F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BA326589-CCF6-E611-8AB4-008CFAF75602.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6EA62ADB-D3F6-E611-A45B-7845C4FC3C86.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FA375BDD-ECF6-E611-A4E8-008CFA002184.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E2023BAF-F6F6-E611-AE25-008CFAFC043A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7056D11E-FBF6-E611-9822-3417EBE46EDF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BC0353E1-FEF6-E611-B34C-3417EBE644B3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/50E545B6-02F7-E611-AD98-3417EBE46EDF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2A98BEC8-03F7-E611-AC63-7845C4FC3C26.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2688BE78-08F7-E611-B5E7-848F69FD2484.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/22A7679C-07F7-E611-A7EA-7845C4FC3B00.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/02AD8B91-08F7-E611-89F4-008CFA000280.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B8C054D6-D5F7-E611-8991-848F69FD294F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/52BAAF32-09F7-E611-B99F-6C3BE5B59200.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/80E18A0C-D1F7-E611-90F8-484D7E8DF051.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/144F8E98-E5F7-E611-BFF3-02163E014330.root',
] )























