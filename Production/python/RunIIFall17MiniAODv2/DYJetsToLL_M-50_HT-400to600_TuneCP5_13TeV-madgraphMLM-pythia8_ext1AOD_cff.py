import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/16AEF9AF-9409-E811-B522-A4BF0108B89A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/127E53EC-5F09-E811-9978-A4BF0112F778.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/92142A36-7E09-E811-853E-A4BF0112F53E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/36DE45BD-A409-E811-B567-001E67E6F544.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/6A22085C-A309-E811-879A-001E6739722E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/0C0BFFB7-AC09-E811-B1EA-001E67E71BE1.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/CAE089BE-BE09-E811-AC15-A4BF010F10EA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/6E824D0A-AB09-E811-886A-001E67792600.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/FE8A271D-AD09-E811-BB2F-00259020084C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/0451E170-C909-E811-B684-A4BF011258D8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/80A67176-0C0A-E811-861C-A4BF01125408.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/D83B411C-7809-E811-9231-AC1F6B1AF186.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/D2CA0DAC-D309-E811-A65C-00266CFFC9EC.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/7214ABFC-000A-E811-8525-008CFAF5550C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/48314F5F-0C0A-E811-B2CE-A4BF01125358.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/24CA2153-3A0A-E811-BD7E-A4BF0112BBE6.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/70FA0E9E-3A0A-E811-831C-001E677925E6.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/8E7B6C42-7C09-E811-87F8-00266CFFB7D0.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/E81A38EF-D209-E811-AB16-FAF699D8EA61.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/1EE6F9A0-2506-E811-8484-0CC47AF9B13A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/94F8C32E-2706-E811-A0E9-0025905C2CB8.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/E85E1F46-1806-E811-B3D5-0025905C431A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/32A2CE22-1806-E811-B96E-0025905D1E00.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/1A8E9C8E-5F06-E811-A489-0025905C548A.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/8C772BF8-6A06-E811-B97B-0025905C43EC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/A2488C0D-4506-E811-9FC2-0CC47A13CBEA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/FE3370BB-1F07-E811-BDC6-0CC47A13D3A8.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/3CE9CDF4-A406-E811-AB38-0242AC1C0500.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/DE877A59-C606-E811-B0FA-0242AC1C0500.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/9AA3D093-2A0D-E811-B913-0242AC1C0502.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/BEFBA0AD-1E0D-E811-A22B-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/AC62F58E-2A0D-E811-B7B4-AC1F6B1AEF94.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/42D0F529-160A-E811-ADC0-0242AC1C0502.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/EE5D3A20-150A-E811-9D50-0242AC1C0502.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/F6EA7D3B-170A-E811-BDC3-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/661F857C-3E0A-E811-A1FC-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/3833D37F-3E0A-E811-B50F-0242AC1C0502.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/34000F59-1A0A-E811-BEC1-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/28BCD8F2-1A0A-E811-A99D-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/4CD39B6E-6E0A-E811-BAFB-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/7E92D5F1-000B-E811-B4CB-A0369F83627E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/56159F27-E909-E811-87C8-0025905C4262.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/42FA2EEF-E809-E811-893A-0025904C6416.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/326851F3-310A-E811-9410-0025904C6568.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/80644F00-320A-E811-A5B7-0025904C66A4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/242B26BA-120B-E811-9CE4-001E677926F8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/AC9C12CF-120B-E811-9FB7-A4BF01125578.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/E8659111-7E0B-E811-8A86-A4BF010F0F2A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/E64A7731-8B0B-E811-AE85-001E67396FCC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/686E63C0-9C0B-E811-8C59-001E673973C8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/60206A63-9E0B-E811-825B-001E67E71BDC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/3C9DB9E4-9C0B-E811-A304-A4BF0112BE48.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/3C6D0FEF-DA0B-E811-A82B-A4BF0112BDDA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/68332548-B10B-E811-83E0-A4BF01125740.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/A600F092-9F0B-E811-802E-001E67397D05.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/0CEE7C4E-AE0B-E811-BAFE-A4BF0112BD7C.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/48AE93FC-AB0B-E811-ACB7-001E67E6F864.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/4061E2F3-AB0B-E811-9AFB-A4BF0115A0C0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/869CAC37-B30B-E811-9579-A4BF011259E0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/5A180A6D-D00B-E811-A083-A4BF010F10EA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/548607ED-D60B-E811-9F39-A4BF0108B60A.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/D8924162-D30B-E811-8377-A4BF01125AF8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/4228E666-C60B-E811-9850-A4BF0112E0A0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/36AC10C3-DB0B-E811-8E50-A4BF010F104E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/7460F7E8-D20B-E811-A897-001E67E6F4CC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/D4C460DE-DC0B-E811-8F45-001E677924AE.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/E2009672-E20B-E811-BDF2-001E67396E64.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/EC992228-DF0B-E811-BC06-A4BF01125DCE.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/F4E98665-DB0B-E811-A40F-A4BF01125608.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/C827BC3C-E50B-E811-B541-A4BF0108B732.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/FCB88D4B-E50B-E811-83D8-A4BF0108B5BA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/F859EA86-DD0B-E811-AEE2-A4BF01125780.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/041397CC-E40B-E811-8CB8-A4BF0112BCCA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/CCAF02A6-E50B-E811-9DCF-A4BF0112DC34.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/5CF42ADC-D50B-E811-AF13-001E67E71408.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/BA731A17-E20B-E811-A499-A4BF01125A30.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/5881F287-DE0B-E811-84C2-A4BF0112BBF8.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/B4ED2161-C70B-E811-B496-002590A80DE0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/226C3D5D-E60B-E811-8366-002590A80DE0.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/90CB63E9-E30B-E811-8439-002590A88802.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/805F0EED-E30B-E811-BA96-A4BF01125770.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/FC28ECC6-FA0B-E811-8492-002590200B20.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/3839710A-F00B-E811-A8C0-A4BF01125608.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/34A61560-AF0C-E811-979D-001E67792598.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/CE8DB7FA-690C-E811-BCD6-FA163E7B3281.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/288EA8B7-6B0C-E811-BF34-FA163EFD9F31.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/E8946EB2-6B0C-E811-A0F2-FA163E195CEE.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/22A457B9-1B0F-E811-A698-0242AC1C0500.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/36E24D99-570F-E811-A602-0242AC1C0500.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/F6460361-2D10-E811-81E0-0CC47A57CCF4.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/A2DE75B9-4110-E811-8252-7CD30AD096BE.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/F229C7D9-1C0F-E811-9CCE-0025905A48EC.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/089C0B2A-3110-E811-A8DD-141877410316.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/AA9F7994-220F-E811-8C31-001E67792588.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/D61FA7A6-310F-E811-B40E-A4BF0112F51E.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/3AE8720C-380F-E811-BFDE-001E67E6F616.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/96952E61-0910-E811-8126-A4BF0112BCFA.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/2A0A3539-2C10-E811-823B-B083FED04276.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/C4807946-2910-E811-9FF1-24BE05C618F1.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/969864C5-990F-E811-B2C7-00266CFFCAA4.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/C437BD5E-1C0F-E811-B1BC-FA163EE35DD9.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/AA5D0786-990F-E811-878B-FA163EEE1ACF.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/962657E4-2412-E811-AB2F-0025905B8582.root',
'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/8CEA3971-580F-E811-80E6-008CFAC941E0.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10_ext1-v1/80000/020A1FA7-570F-E811-988C-34E6D7E05F0E.root',
] )




























