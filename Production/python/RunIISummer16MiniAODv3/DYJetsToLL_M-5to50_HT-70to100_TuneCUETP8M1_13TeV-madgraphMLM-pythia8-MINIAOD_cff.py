import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F247A4FA-56EA-E811-947A-24BE05CE4D91.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/52C63F37-46EA-E811-9530-24BE05C63721.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/5897EB68-46EA-E811-93F3-506B4BB166CE.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/5E3529D5-48EA-E811-A400-5065F381A2F1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4480F845-46EA-E811-ABC1-24BE05C62611.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/42483B5A-47EA-E811-820B-24BE05C4D821.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/48C742D6-48EA-E811-BCD5-5065F381A2F1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/ECA8BD8A-48EA-E811-92D8-5065F3818271.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/74854402-4AEA-E811-8D4C-506B4BB16026.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3CD7EC2F-4BEA-E811-AB3D-24BE05C6D711.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B644CEE7-4CEA-E811-A21F-24BE05C48831.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/1A9C5902-50EA-E811-A9AE-24BE05BDAE61.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/64112377-48EA-E811-98D5-5065F3818271.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/7A5319AF-49EA-E811-8C90-24BE05C4D821.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/9CEC40F7-55EA-E811-9646-24BE05CEDCF1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A0FC4452-4CEA-E811-92B2-506B4BB166AE.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/1C35E4B4-54EA-E811-8704-5065F3812201.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/8AD8139F-56EA-E811-8F41-24BE05CE2D41.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/EA797706-58EA-E811-9785-5065F37D7121.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DC8AC1F0-57EA-E811-AC70-5065F3816291.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/701C9872-48EA-E811-A988-24BE05C3B8B1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A6FCD26B-58EA-E811-95DB-24BE05BDAE61.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/026F8D54-5AEA-E811-91CC-24BE05CE2D41.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E80D2C33-4EEA-E811-837D-E0071B7A8590.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4853F93C-59EA-E811-AD21-24BE05C44B91.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4AA62848-5BEA-E811-9BAC-5065F3812201.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/82404E6B-4AEA-E811-97D7-24BE05C4D821.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/5CB4722A-4BEA-E811-A9DA-24BE05C4D821.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3A7789FF-4AEA-E811-A91A-E0071B791111.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B8531AD2-5FEA-E811-A578-24BE05CEDCF1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/883994F1-4CEA-E811-9E4D-E0071B791111.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E655D85E-4EEA-E811-8F02-E0071B791111.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/C46C94F6-55EA-E811-B49B-506B4BB166B6.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/56B4BD50-4EEA-E811-ADA8-506B4BB16016.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/30E60A64-64EA-E811-9F59-5065F37D7121.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D85078F3-63EA-E811-995E-24BE05BDCEF1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/64AD6FF0-63EA-E811-AB93-24BE05BDCEF1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DADBEE5C-60EA-E811-B870-506B4BB16AB6.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/8AD581A8-64EA-E811-9DB0-24BE05CE5D21.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/6C5EB671-56EA-E811-AB96-E0071B7A8560.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/348744ED-60EA-E811-A8CC-506B4BB166AE.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/FA2D9EFA-64EA-E811-8683-24BE05CE5D21.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/38F9D60F-54EA-E811-81DB-24BE05CEEDE1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/324634EC-5AEA-E811-BCE6-E0071B7AC710.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D84FBD70-52EA-E811-89ED-5065F381F1C1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/58CDE134-5DEA-E811-8978-E0071B7A58B0.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/AAFA4B14-67EA-E811-9441-EC0D9A847EAA.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/52E78FA5-57EA-E811-880F-24BE05CECB81.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/1CCFDEAB-5AEA-E811-A2FE-506B4BB16016.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/24BF48A1-5DEA-E811-A7AA-506B4BB16016.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F0A5D003-6BEA-E811-8FAA-506B4BB166CE.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3AA4738A-5DEA-E811-A026-24BE05CECB81.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A41B9F4F-7CEA-E811-A59C-24BE05C48831.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/422E12EB-7BEA-E811-81D0-24BE05C6D711.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A88A3643-60EA-E811-A8E6-5065F381F1C1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4C310FAC-65EA-E811-821D-506B4BB16016.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/9C70FEDF-6CEA-E811-ABB7-506B4BB16016.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/708CE7D6-60EA-E811-BE0F-EC0D9A82262E.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/CCF039C0-6EEA-E811-B9EE-24BE05CEEDE1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B433DE61-4EEA-E811-9AA4-5065F37D9171.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/EA14E561-4EEA-E811-BF5F-5065F37D9171.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D24151F0-5CEA-E811-88AC-E0071B6CAD10.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/16250434-71EA-E811-8CF5-E0071B791111.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/44C44CA8-73EA-E811-ABF5-24BE05C4D821.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/66EDC0FB-6AEA-E811-ADD4-EC0D9A82262E.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/AEAAF622-68EA-E811-8192-E0071B7A5650.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B4EDA442-6FEA-E811-9DAB-E0071B7A5650.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/90BC8E62-6AEA-E811-A024-E0071B7A5650.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D07CE5B1-6EEA-E811-9B5D-24BE05C64601.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/223E4896-64EA-E811-870A-24BE05C4D8C1.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/369FAAD7-78EA-E811-A331-24BE05C64601.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/502677A5-79EA-E811-AB7A-24BE05C64601.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F4415D0D-62EA-E811-8195-24BE05C48821.root',
'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/50C31834-FCEA-E811-A1E9-E0071B7AC770.root',
] )