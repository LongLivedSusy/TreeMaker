import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/9AC9ADAB-BF1B-E811-ACA6-A0369FC5E9A4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/AA29E22C-E91C-E811-931F-008CFA56D6F4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/C655F4B3-C71B-E811-8038-FA163ED784C2.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/8EDF47DC-C71B-E811-BC75-FA163EA9DC0A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/D6C7BAE9-C11B-E811-876A-24BE05CEBD61.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/0E254359-C11B-E811-B6D4-24BE05C636E1.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/C8AC34EE-C11B-E811-BF6E-E0071B7AC760.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/30EE8929-181D-E811-A85E-4C79BA18094B.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/1A7C2B2D-8E1B-E811-8129-801844DEE7F8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/9212708B-961B-E811-8C70-1866DAEA6BC4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/ACC49E39-931B-E811-8665-141877411FCD.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/84E13056-211C-E811-8CE1-0CC47AD9908C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/84D780E1-221C-E811-A80D-001CC4A64C3E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/260D0040-351D-E811-A10E-3417EBE706C3.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/968FE49C-BD1F-E811-AC09-5065F3812221.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/A8D23589-B120-E811-93DB-00000065FE80.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/7215DA49-7022-E811-90EC-002590DD7E50.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/78014D95-6923-E811-9EF5-3417EBE7002A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/EA74778D-9D23-E811-8B35-0CC47A7E68AA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/4E36BE0B-921C-E811-A34E-F01FAFE5F125.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/16126459-691C-E811-A9F7-1866DA85D9A3.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/9436F17C-521C-E811-8D29-F01FAFE157DF.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/40FA7E2F-A71C-E811-900B-1866DA7F967F.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/927F58BF-8E1C-E811-A1DE-F01FAFE1592F.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/1CBE6DDA-B31C-E811-AF89-F01FAFD67AE0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/B2F38229-C620-E811-B7D1-1CB72C1B6CC6.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/7E1FDC65-9C1C-E811-A5ED-D4856445F6CC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/DE638A53-891C-E811-9085-3C4A92F8DC66.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/3A765D0D-BB21-E811-84B5-1866DA7F9225.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/527400EE-BC21-E811-B956-1866DA85DC67.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/14742DC4-C71F-E811-B136-008CFAC94254.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/702669DC-BD21-E811-8B53-5065F38102F1.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/A0D954E9-1E1C-E811-9D44-C4346BC7AAE0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/8EF15B3F-CE22-E811-9CCD-44A842CFC98B.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/FCE74073-CE22-E811-A8FC-B499BAAC014E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/9AC24AEE-E021-E811-92ED-FA163EBF8D85.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/468C7607-7122-E811-9257-FA163E92806B.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/585CD347-B21B-E811-B221-00A0D1ECBAFC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/5A8FCDC1-F123-E811-A778-7CD30AD09010.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/4A6584B9-B324-E811-9C7C-7CD30ACDCA34.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/4AA5A0C4-1A24-E811-AD0C-1418773425EA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/1633BB02-B423-E811-8565-F01FAFE5F879.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/D81A62B9-D923-E811-83F5-0242AC1C0502.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/5C12075C-2E25-E811-A8A6-001E67504E7D.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/6A9AB687-2D28-E811-9188-002590FD5A52.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/665DF065-4124-E811-A316-FA163EEB3CB5.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/5E51D0E4-C324-E811-A46C-FA163E6A6DD4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/DAC07FB6-E527-E811-AA2B-02163E01A020.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/F29CF5BA-DB27-E811-A70A-FA163ED6905C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/4E59BDC6-0D28-E811-9D20-02163E01A168.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/D44CCDA1-FE27-E811-9CCA-FA163E63310A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/220F826B-0628-E811-86DD-FA163E6CFA01.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/D61A78C7-0D28-E811-9D6E-FA163E8ED26E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/2E3E1B24-0628-E811-BF9B-FA163E03FB38.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/0AA2C5B4-0828-E811-A4B3-FA163E3924E6.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/F6FB3B4D-FF27-E811-9BDB-02163E00B091.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/100000/22FE4CE6-0828-E811-B15D-FA163E2DC6DB.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/0CE34ED1-F623-E811-AB91-002590DE38C8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/18960155-FB24-E811-9D11-3417EBE34BFD.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/90B4439A-FB24-E811-A9E7-ECB1D79E5C40.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/9667A724-F623-E811-BDB5-0425C5902FB0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/60EBB091-9123-E811-9B55-0CC47A6C0682.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/CAE04C59-0A24-E811-A751-0CC47AF9B2EA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/D01D1D5F-9223-E811-ABA8-6C3BE5B59210.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/72019D80-F723-E811-8C87-002590D9D966.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/04D55831-F323-E811-9EA9-002590E7DEBE.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/B2A5A724-9223-E811-9C0C-002590E7D7DE.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/30000/DA13BB5B-FB24-E811-A676-001E677923F4.root',
] )








