import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017C/MET/AOD/17Nov2017-v1/60000/A8097BD0-30DE-E711-BF49-0CC47A4F1D16.root',
#       '/store/data/Run2017C/MET/AOD/17Nov2017-v1/60000/2C6BFB86-C6E5-E711-B043-5C260AFFFCA1.root',
#       '/store/data/Run2017C/MET/AOD/17Nov2017-v1/60000/E826607E-30E4-E711-85E3-7845C4FC3B0C.root',
#       '/store/data/Run2017C/MET/AOD/17Nov2017-v1/70001/F4323328-DDED-E711-8C3A-003048F348B6.root',
#       '/store/data/Run2017C/MET/AOD/17Nov2017-v1/50000/AE1EDF14-4EE4-E711-97C6-02163E012915.root',
#       '/store/data/Run2017C/MET/AOD/17Nov2017-v1/50000/12FDE457-61E1-E711-8A97-02163E01A752.root',
#       '/store/data/Run2017C/MET/AOD/17Nov2017-v1/60000/7C7A3C0A-ECE2-E711-8B20-441EA1615FA0.root',
] )
