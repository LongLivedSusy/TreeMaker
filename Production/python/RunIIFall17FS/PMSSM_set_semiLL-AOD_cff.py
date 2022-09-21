import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_1.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_2.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_3.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_4.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_5.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_6.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_7.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_8.root',
       'file:///pnfs/desy.de/cms/tier2/store/user/mmrowiet/SUS-RunIIFall17FS_PMSSM_set_semiLL/pMSSM_Fall17FS_set_semiLL/RunIIFall17FS_AODSIM/220908_161731/0000/SUS-RunIIFall17FS_set_semiLL_10.root',
] )
