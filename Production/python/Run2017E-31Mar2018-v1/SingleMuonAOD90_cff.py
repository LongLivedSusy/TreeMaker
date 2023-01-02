import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60001/EC905558-AEDD-E711-A09B-02163E01423A.root',
       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/70001/5CDACC9C-76DC-E711-A93B-0025907DE22C.root',
       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60001/1CDD54E1-64DC-E711-A523-02163E01419D.root',
       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60002/88D0A662-95DD-E711-A3AC-02163E019BCF.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60001/109DA2EF-5EDC-E711-B058-02163E0118D2.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60011/749199F3-FADD-E711-B37F-02163E014221.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/50004/3262F369-52DC-E711-97EB-001E67DDC119.root',
       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60000/08C9ECAF-26DC-E711-AEE0-02163E014675.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60001/A27606BB-7CDD-E711-A051-02163E0128E2.root',
       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/50002/EC660FBC-C5E1-E711-8507-0CC47A5FBE35.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60001/8AC1DC3A-7BDD-E711-AB3C-008CFA197B54.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60000/32BB13A2-05DC-E711-8BF7-02163E01462A.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60005/56C374D6-60E2-E711-971E-0025902008D0.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60004/221A900A-3EDE-E711-A1C6-02163E019CA0.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60004/2896CB97-3EDE-E711-AF04-02163E01A2F0.root',
#       '/store/data/Run2017E/SingleMuon/AOD/17Nov2017-v1/60014/04E41EC7-4CDD-E711-B23C-A4BF01013F33.root',
] )
