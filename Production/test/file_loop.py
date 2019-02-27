#!/bin/env python
import os
from optparse import OptionParser
import commands
import collections
import glob
import time

parser = OptionParser()
parser.add_option('--outpath', dest='outpath')
(options, args) = parser.parse_args()

def runcmd(cmd):
    print cmd
    status, output = commands.getstatusoutput(cmd)
    print output
    return status, output
    
aod_files = []
with open("info_aodfilename", "r") as fin:
    aod_files = fin.read().split(",")

job_return_status = 0

for aod_file in aod_files:
    
    # check if destination file already exists:
    
    print "check if output file already exists:"
        
    cmd = "xrdfs root://dcache-cms-xrootd.desy.de/ stat %s/$(cat info_outfilename).root" % (options.outpath.replace("srm://dcache-se-cms.desy.de", "").replace("root://dcache-cms-xrootd.desy.de/", ""))
    status, output = runcmd(cmd)

    if status == 0:
        print "outfile file already exists on dcache."
        continue
        
    # locate the corresponding miniAODs... come to papa
    os.system('cp "$CMSSW_VERSION/src/TreeMaker/Production/test/get_miniAOD.py" .')
    os.system('chmod +x get_miniAOD.py')
    cmd = './get_miniAOD.py --infile=%s' % aod_file
    status, output = runcmd(cmd)

    if status == 123:
      print "empty union json, ignoring lumisection"
      continue
      
    # run cmsRun the second time to run with miniaod.root in sidecar
    cmd = "cmsRun runMakeTreeFromMiniAOD_cfg.py $(cat info_arguments) 2>&1"
    status, output = runcmd(cmd)
    
    if status != 0:
        job_return_status = status
    
    # run test script to check if output file has a tracks collection:
    os.system('cp "$CMSSW_VERSION/src/TreeMaker/Production/test/check_if_tracks_present.py" .')
    os.system('chmod +x check_if_tracks_present.py')
    cmd = 'python check_if_tracks_present.py'
    status, output = runcmd(cmd)
    
    if status != 0:
        job_return_status = status    
        
    # copy output:
    for i in range(10):
        
        success = True
        for ifile in glob.glob("*root"):
            cmd = "xrdcp -f %s %s/%s" % (ifile, options.outpath, ifile.split("/")[-1])
            status, output = runcmd(cmd)
            if status != 0: success = False
        if success: break
        
        time.sleep(100)
    
quit(job_return_status)
    