import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C4362D8C-2F9B-E811-A5EA-3CFDFE63F3C0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/047437FB-F69B-E811-AF92-3CFDFE6396C0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7ACBD5B3-FA9B-E811-814D-3CFDFE634DE0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/24464848-449A-E811-B98B-A4BF010114F4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B86F4DD7-0E9C-E811-9EFF-A4BF0101202F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5E7B116C-2D9B-E811-8CC9-A0369FD0B374.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AC79BAD1-1D9B-E811-8DB9-A0369FE2C12A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2A6512AD-269B-E811-A99D-0CC47A2AED04.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9A4DF05A-A19B-E811-9625-0CC47AD99144.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AECE5716-AD9B-E811-A5F9-0CC47AD98D12.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CA9FAFDD-F59B-E811-A78C-002590E2F9D4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/88CDA8C9-B09C-E811-B12D-0CC47A13D2A4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/340A7ADE-D29C-E811-BED9-002A6AE0E1F5.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AA947DCE-0198-E811-AB97-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B4E93FD7-739C-E811-9C97-0CC47A5FC679.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0C63F5D3-6C9D-E811-A6A3-003048FE2B6C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8E9ED6D0-6C9D-E811-97CD-0026B93F40B2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/40F1849B-339A-E811-810F-EC0D9A8221FE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/20A2A827-299B-E811-B1B0-A0369F301924.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0CD7C68B-269B-E811-A7F4-24BE05BDDE22.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A6D32AE9-1E9B-E811-88A6-E0071B749CA0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F2ABA4C6-489B-E811-A3AE-24BE05C616C1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/38B3B9E6-489B-E811-8318-24BE05CE1E51.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F8399EE3-489B-E811-A0BD-24BE05CE4D91.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C870F446-B59B-E811-A6C2-E0071B693B41.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F0FD9EAB-F59B-E811-8733-008CFAC93D44.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/32100CC7-F59B-E811-8203-008CFAE453CC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C28BB7B1-3A9C-E811-AFCA-008CFAE45338.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AA5A1ED7-3D9C-E811-B5B4-008CFA11113C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D45D5276-A19C-E811-B61E-008CFA1974A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D6164D1C-A19B-E811-9650-A4BF01125828.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D2C70553-A09B-E811-B6CF-A4BF0112DDCC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/76E37E34-9F9B-E811-BFDD-001E6779267A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/742BDAC7-B49C-E811-B540-A4BF0112BDE2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A4D3589D-4D9B-E811-A3C0-7CD30AC030B4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EEEB32B6-889C-E811-8A2D-1CB72C1B649A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B0BF8B1E-829C-E811-A511-0026B92779A3.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/24D93412-6C9C-E811-8497-00266CF3DE6C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A0693DD8-6C9D-E811-BAC5-002590747D9C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2463941C-6D9D-E811-8C4D-F01FAFE159E3.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D4BBA249-349C-E811-8910-842B2B42B582.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4044F1C6-699C-E811-88AD-B083FED42FC3.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/86497D50-FE9C-E811-AF59-A4BADB1E602F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D60E6301-6C9C-E811-9C41-002590E7DFE0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B8442EE0-F59B-E811-9AA2-0CC47A0AD630.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D4892F14-6D9D-E811-93F5-003048CB8768.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4ACE4C5F-789C-E811-8959-0025905C54FC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BE49FA7E-AD9B-E811-8A67-0CC47A7EEE76.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/40D975C0-ED9B-E811-B2C2-1866DA89035E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/52232DA2-7F9C-E811-9F32-0025905A610C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/E0277BCE-6C9D-E811-BE9E-002590DE6C48.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4E61B31F-B59C-E811-B415-24BE05C6D731.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CEB3C7C6-F59B-E811-883E-E0071B73B6E0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/0E8A77F0-0CA9-E811-BBFF-A4BF0101DD64.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/40A5A77E-10A9-E811-99C1-001E67A3FF1F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/24E84FEE-08A9-E811-82E2-0242AC1C0504.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1220000/089DF319-A7C0-E811-B29A-0242AC1C0507.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1220000/E0E302F1-A6C0-E811-9960-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1220000/069EF3D9-A6C0-E811-B8C0-0242AC1C0507.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1220000/64808840-A7C0-E811-A983-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/1220000/761BF545-A6C0-E811-8F86-001E6779263E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/120000/32296A3F-EBC0-E811-8A11-001E67E71C04.root',
] )



































