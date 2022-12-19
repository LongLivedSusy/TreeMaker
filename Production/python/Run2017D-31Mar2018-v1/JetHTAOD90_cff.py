import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/20000/BC8285F7-19CD-E711-88FD-B4E10FA31EFB.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/40001/04EA12F0-D3CE-E711-8044-001E67792890.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/20001/E22AD101-2CCE-E711-AFBA-00266CFFCB7C.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/20000/B01D04D4-D9CD-E711-BCA1-0025905C54C4.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/40000/CA21E355-A7CC-E711-B72E-0025904C5180.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/40000/D6508B43-8BCC-E711-B179-00266CFEFE1C.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/40000/CC919E93-87CC-E711-96F9-008CFAF28DCE.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/40000/D6508B43-8BCC-E711-B179-00266CFEFE1C.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/20000/A0E6B720-C2CC-E711-89D1-0025905C2CA4.root',
       '/store/data/Run2017D/JetHT/AOD/17Nov2017-v1/40000/A811DC81-73CC-E711-BAE5-0025905C53F2.root',
] )
