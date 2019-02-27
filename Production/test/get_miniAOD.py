#!/bin/env python
import os
from optparse import OptionParser
import commands

parser = OptionParser()
parser.add_option('--infile', dest='infile')
parser.add_option('--outfile', dest='outfile')
parser.add_option('--nev', dest='nev')
(options, args) = parser.parse_args()

print 'locating miniAOD file(s) which match the AOD file:', options.infile

if not 'root://' in options.infile:
    options.infile = 'root://cmsxrootd.fnal.gov/' + options.infile

#first, get start / end of AOD file:
print "Running edmFileUtil to get run number / lumisec information..."
os.system("edmFileUtil %s -e > TMPFILE" % options.infile)
status, output = commands.getstatusoutput("grep '(Lumi)' TMPFILE | head -n1")
run_start = output.split()[0]
lumi_start = output.split()[1]
status, output = commands.getstatusoutput("cat TMPFILE | tail -n6 | head -n1")
run_stop = output.split()[0]
lumi_stop = output.split()[1]
aod_range = "%s:%s-%s:%s" % (run_start, lumi_start, run_stop, lumi_stop)

#get corresponding miniAOD file(s): 
miniaod_filenames = []
status, parent_filenames = commands.getstatusoutput('dasgoclient -query="parent file=/%s"' % options.infile.split("//")[-1])
for parent_filename in parent_filenames.split("\n"):
    status, children = commands.getstatusoutput('dasgoclient -query="child file=%s"' % parent_filename)
    for child in children.split("\n"):
        if "/MINIAOD/" in child and "17Sep2018-v1" in child:
            miniaod_filenames.append(child)

miniaod_filenames = list(set(miniaod_filenames))
print "miniaod_filenames", miniaod_filenames

os.system("echo %s > info_miniaods" % ",".join(miniaod_filenames))

json_content = '{"%s": [[%s, %s]]}' % (run_start, lumi_start, lumi_stop)
with open("lumisecs.json", "w") as fo:
    fo.write(json_content)


#os.system("echo %s > lumisecs.json" % json_content)
os.system("compareJSON.py --and $(cat info_jsonfilename) lumisecs.json > lumisecs_union.json")




#IGNORE

pyset = """
import FWCore.ParameterSet.Config as cms
process = cms.Process('NoSplit')
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(%s),
                            lumisToProcess = cms.untracked.VLuminosityBlockRange('%s'),
                    )
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(%s))
#process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.output = cms.OutputModule("PoolOutputModule",
    #outputCommands = cms.untracked.vstring("drop *", "keep *_*RecHits*_*_*", "keep *_*dedx*Harmonic*_*_*"),
    outputCommands = cms.untracked.vstring("keep *"),
    fileName = cms.untracked.string('%s'),
)
process.out = cms.EndPath(process.output)
""" % (",".join(miniaod_filenames), aod_range, options.nev, options.outfile)

#print pyset
#with open("pyset.py", "w") as fo:
#    fo.write(pyset)

#status, output = commands.getstatusoutput("grep 'events' TMPFILE")
#print "stats:\n", output

#print "running cmsRun..."
#status, output = commands.getstatusoutput("cmsRun pyset.py")
#print output
