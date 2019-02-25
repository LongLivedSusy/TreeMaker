import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E24F15C8-7711-E811-AB1F-02163E019FC3.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8E6AD1F4-7711-E811-8BD1-FA163E8A43A3.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/C4466C93-9F11-E811-9244-02163E01A153.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/1A4DB8EE-E111-E811-A382-FA163E24328E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/4EE14308-9D11-E811-846F-FA163EE8681C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8CC9CCAA-6E11-E811-94CA-FA163E5B9932.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/2EE025A0-9E11-E811-84B2-FA163E564EBD.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/601CFEE5-1112-E811-99BC-FA163EE4EA01.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/6058D709-BB11-E811-AE6E-FA163E4465CD.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/4A67E11B-A111-E811-A7A5-FA163E6B593C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/D64FCB3E-8E11-E811-BCA1-02163E01A106.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/20A19604-C111-E811-944E-02163E01A035.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/2CF801AF-C511-E811-BFCC-FA163ECAA680.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/242A07C1-1012-E811-BB21-FA163EFA3E0C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/5608CEC1-1012-E811-9B54-FA163EA546EE.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A4A6FBE4-1912-E811-9DBB-FA163E3BDB32.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8EDC8FA5-3112-E811-8711-FA163E759AE3.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/92E79801-2C12-E811-BF56-FA163E38093C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/026F5855-1212-E811-83D4-FA163E065965.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/94EEEAAF-3612-E811-8AC1-FA163E90AA3E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/B05140E8-3D12-E811-9506-FA163E8A2E19.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/1CB3BF71-4E12-E811-9975-FA163EBE9168.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E8EA9819-3812-E811-B981-FA163E684D4D.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/008C0272-4E12-E811-A5E6-FA163ED6DA01.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/5876AEDF-6A12-E811-A6AF-FA163E199215.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/264BE8CD-3112-E811-9573-02163E019FBD.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/AEE6FC70-4C12-E811-AF3D-02163E01A097.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A05DA675-2B12-E811-844A-FA163E4E9B1E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/2AA27BB2-3612-E811-83CE-FA163E9233DE.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/04B7A7E6-5F12-E811-8552-FA163EB14104.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/9E78B0F0-5F12-E811-ABB9-FA163E735076.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/D8F4E1A4-FB11-E811-A06E-FA163EFACD4B.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/3E21B9EF-7312-E811-BA33-FA163E4B7072.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/0AB541E6-4E12-E811-A482-FA163E37E0B0.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8E9502DB-7A12-E811-A64A-02163E01A0E8.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/AC4D2D77-6F12-E811-9B67-FA163E13FDEA.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/3C7A8A29-5812-E811-B15B-FA163E06735E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/10DCDFA5-6412-E811-B4F8-FA163E4C8771.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FE0BAE17-6612-E811-A5CD-FA163EFB3309.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E605839F-4F12-E811-BEAD-02163E019EB6.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/447F2C0E-8312-E811-AB7C-FA163EDD7137.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/54A96F9F-7E12-E811-A49C-FA163E44A4FF.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/78F50D73-6F12-E811-9A36-FA163EDFB877.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/84310860-4F12-E811-BABC-02163E013D69.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E0AD2617-8312-E811-9B36-FA163EDB8733.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/22A762A9-6A12-E811-A3C1-FA163EFDB548.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/70166D35-FE11-E811-BED8-02163E01542A.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/06221FF3-7312-E811-8249-FA163E160041.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/48B57F3C-5912-E811-9643-FA163EEACBFD.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E68D1514-6612-E811-9C70-02163E00C4E3.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/345E4517-8312-E811-9692-02163E01A01D.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E46B4BD1-4B12-E811-89BB-FA163E2EC4ED.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/9A8929E8-4B12-E811-A2B6-FA163EEBA34C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/DCAB65F0-3E12-E811-AC21-02163E01A15C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FCC4CA0B-C112-E811-82C7-FA163EF73313.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F4788E49-CD12-E811-B356-FA163E082D80.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F61B2808-C112-E811-8976-FA163EBE4188.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F02DE129-5D12-E811-8BE4-FA163ED8E79E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/0C8C1EDA-C712-E811-A502-FA163E119D19.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/AA19B0AD-7312-E811-A4E2-FA163EDA6ADD.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A0859345-CD12-E811-A446-FA163EA285DD.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8E9E2400-AD12-E811-8602-FA163E63FC68.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A66B183C-7F12-E811-85CA-FA163E2D8677.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/08641D69-CF12-E811-B63D-FA163E254513.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/70417F67-3813-E811-89FC-FA163E54BF1C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8AFFB3A7-EB12-E811-8691-00266CFFCCBC.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/B6268BE3-A411-E811-B5E5-02163E01A441.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/9EA36449-7411-E811-B674-02163E011BD8.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/920D69F2-A411-E811-9B11-02163E01A473.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/564682BB-E311-E811-8700-02163E01A327.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/56B34994-BD11-E811-99FD-02163E014235.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/182251F8-B211-E811-AFB1-02163E01A6A7.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FA45C377-C511-E811-82A8-02163E01A288.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/CC72CFED-B211-E811-A07A-02163E01A2E9.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/3EA86B6B-C411-E811-B7D7-02163E013716.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/62310066-C411-E811-9E68-02163E0133B3.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/587BC512-B311-E811-B597-02163E01A27D.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8E16C723-D911-E811-AA48-02163E01A72C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/1287398D-BD11-E811-80FB-02163E01353B.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/205FD3C1-E011-E811-9DE0-02163E01A68C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/2040CDA8-D811-E811-9B20-02163E019E47.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/1029F794-E911-E811-BD31-02163E0117FF.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/AA76D4A9-1412-E811-8E7E-02163E01234F.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/6E4758C9-1312-E811-9C8A-02163E012400.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/968E3541-1812-E811-B3E2-02163E01A2B5.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FEF9E5BD-E011-E811-9697-02163E011D63.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8CFE1A60-1712-E811-B700-02163E011E9F.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/86CE67BE-1A12-E811-A17F-02163E011920.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/32F24BCB-1312-E811-AF00-02163E019BF1.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/9AA6B6FC-2312-E811-8F84-02163E01430A.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/0443FC28-0112-E811-A90A-02163E012A30.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/0E385352-1812-E811-814E-02163E01A5C0.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/22AC2355-1712-E811-88F6-02163E019BE9.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/EC68CE5A-1712-E811-9643-02163E01A4BC.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/829F98A3-1412-E811-9227-02163E019B50.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/40BD5DC7-1312-E811-91DD-02163E019E47.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/C01B21A2-1412-E811-BA3A-02163E019CA8.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/7AB6F671-1A12-E811-98BD-02163E01A68C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/34F9AA14-2612-E811-8033-02163E01A409.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/4E26149E-1412-E811-90BE-02163E01A305.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/384FE3CB-1312-E811-A7DD-02163E01353B.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/3460D721-2612-E811-9E00-02163E01A1C6.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/CE7B2EFE-2312-E811-841C-02163E01A32C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F6F42808-2412-E811-919A-02163E0118BD.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/5AC27A72-1D12-E811-A805-02163E011B6F.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/30E48D01-2412-E811-B75A-02163E0117FF.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/80DF4017-4C12-E811-BE9C-02163E01A3DE.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/CC50708E-5B12-E811-8922-02163E0138D8.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/66175124-7512-E811-A848-02163E01440E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/AE084781-CF12-E811-A84F-02163E011AFB.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/DE95F9EA-6E12-E811-9643-02163E019D0D.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/B8E92FFF-6912-E811-A471-02163E019B22.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/B484DE70-1712-E811-B540-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/860B8413-0312-E811-A920-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/02770854-1F12-E811-B102-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/56826DF5-1312-E811-B3A4-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FEA9F01C-1C12-E811-BF4B-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F63FFF40-1A12-E811-8D5D-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/160E2D5D-1912-E811-BF5C-0242AC1C0503.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/4CA9D891-1712-E811-8E4D-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/A25DE3C4-1A12-E811-9888-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E2E234CC-1A12-E811-8AF4-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/02E8D849-FC11-E811-BC03-0242AC1C0505.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/9EF0EA8B-2112-E811-B2F0-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/20525196-1812-E811-8100-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/04D239B4-1712-E811-B457-0242AC1C0506.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/6E6F4FA4-FB11-E811-9684-44A84225C629.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/6003AA0F-3212-E811-83E2-14187763663C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F0E01C11-3212-E811-B015-002590D60166.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/9610EC04-3012-E811-BE11-002590D60062.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/D88A9EED-2812-E811-A313-A4BF0112DD8C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/C6E12C18-FE11-E811-AACB-001E677923A0.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FE08A59F-0812-E811-A164-A4BF0112DF14.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/CA0DFA8E-E411-E811-85A9-A4BF0112BD74.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/90F1D5FD-1712-E811-A099-001E67792650.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/6266CFDE-DD11-E811-BFDE-001E67792720.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/76FA4806-2112-E811-A3A8-A4BF0112BC7A.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/2037BDB9-3512-E811-B3C7-A4BF010F0F08.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8C6404E4-E911-E811-BCC8-A4BF01125600.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/0896EAEE-1D12-E811-A5DC-A4BF01125788.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/403D4B26-3812-E811-A0A6-001E6739723D.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/245A21A7-2612-E811-9D20-001E67792526.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/D44A12BA-2212-E811-97EE-A4BF0108B7E2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/94D5A423-5912-E811-8741-A4BF01158CF8.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/42BCF6C0-5212-E811-B220-A4BF01158D38.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/70167715-2812-E811-B5E4-001E67792740.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/80380856-5612-E811-ADE2-A4BF011255B8.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/120F2D64-2912-E811-98C5-002590A3C978.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/6633B4D4-1D12-E811-8D5C-A0369FC51394.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/ECF68A1D-1412-E811-A505-A0369FC52358.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FEBB1424-D511-E811-9AD1-0025904C669C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/5A818D25-D511-E811-9CDD-0025904C6564.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/B42EB023-D511-E811-8292-0025905D1D52.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/3AC518D0-E911-E811-BADD-0025904C68DE.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/24ED402D-D511-E811-85CA-0CC47AF9B1EA.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/68E807D9-0E12-E811-ADAF-0025904C641E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/58CDED0C-1B12-E811-B949-0025904C51FE.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/60D28030-D511-E811-821F-3417EBE64C7B.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/70D8B8B2-2C12-E811-8EC3-0CC47A78A408.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/286897DB-B412-E811-8A7A-0025905B8564.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/DC433059-1412-E811-9E0C-0025905B856C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/10D9F080-1C12-E811-B558-0CC47A4C8EC6.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8883C0AD-D511-E811-B42F-002590DE6C9A.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/96FCF99D-C313-E811-AFBE-0025905C53F2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/0AF2FFD6-0D12-E811-8617-6C3BE5B5B340.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FAB242BC-D511-E811-B603-0025901FB0CE.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/D0BB7D65-0312-E811-927C-28924A33AFD2.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/2A825858-D312-E811-A2DF-FA163EAC4CED.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/98541551-CE12-E811-BF54-FA163EF62619.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/E23577AB-7312-E811-8AF9-FA163E68024E.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F2AFC02C-8312-E811-8126-FA163EDBDDE7.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/BE9FBF85-D312-E811-A943-FA163E22945C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/04073A65-0813-E811-A361-02163E014FBC.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/C4359C60-2A13-E811-865B-FA163EC5E04C.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/460DC708-F412-E811-B8E7-FA163E1448D1.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/88EF7028-3813-E811-9BFE-FA163E1AC414.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F29FCF5E-1513-E811-AA77-02163E01433B.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/FE758067-1513-E811-A4AE-02163E013906.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/F2D9312C-D511-E811-ABE1-A0369F83628A.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/BC82D335-D511-E811-8DFB-AC1F6B1AF1CE.root',
'/store/mc/RunIIFall17DRPremix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/94X_mc2017_realistic_v10-v1/40000/8CB67787-1212-E811-B520-D8D385FF36D8.root',
] )