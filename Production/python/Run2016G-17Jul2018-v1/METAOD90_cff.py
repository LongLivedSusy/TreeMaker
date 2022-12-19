import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/50000/B86E9178-DB9B-E711-87E6-A4BF0112BC5E.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/10000/0C185E49-F19A-E711-937D-A4BF0112E330.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/50000/681D5D13-8F9B-E711-B19A-7845C4FC3B3F.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/50000/A017B8E1-889B-E711-9286-3417EBE649FF.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/50000/4CFCE6A6-A49B-E711-A671-484D7E8DF06B.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/90000/34692318-2D9D-E711-A047-A4BF01125AB8.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/110000/5EE40933-AF97-E711-98D4-02163E011D5B.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/110000/EAAD473F-6597-E711-88AA-02163E01257E.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/110000/5EE40933-AF97-E711-98D4-02163E011D5B.root',
       '/store/data/Run2016G/MET/AOD/07Aug17-v1/70000/BA782969-049D-E711-8D93-001E677927C2.root',
] )
