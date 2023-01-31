import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50003/4E442C31-E97E-E711-9DF9-0025905A48BC.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/110001/5A014B83-0D80-E711-8DFF-0CC47A7C357A.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/70001/3016F430-AA7E-E711-9500-0025905B85CC.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/110001/7C1F8F8D-937F-E711-9EAD-0025905A60EE.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/70001/5880EC8B-F77D-E711-923C-0025905A48C0.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50000/8EFFF060-267F-E711-BD17-0CC47A4D764A.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50002/18E4D9EF-817E-E711-88A7-0CC47A78A496.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/70000/5C5C452C-AA7E-E711-9308-0CC47A7C346E.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50001/0E7C2670-B97D-E711-AFC2-1866DA7F9225.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/70000/2CF816A7-9C7E-E711-8164-0025905B85BA.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50001/300A6758-C77D-E711-96D7-0CC47A4C8E1C.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50000/02C812B4-857D-E711-84F5-0CC47A78A456.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/70000/A2683D37-647E-E711-BA88-0CC47A4D765E.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/70001/88773C9C-247E-E711-8102-0025905A609E.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50002/720320E8-C07D-E711-9470-0025905B8598.root',
       '/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50000/0A40CA37-2A7D-E711-B6BB-0025905A497A.root',
] )
