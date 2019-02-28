#!/bin/env python
import os
from optparse import OptionParser
import commands
import collections
import glob
import time

parser = OptionParser()
parser.add_option('--outpath', dest='outpath')
parser.add_option('--arguments', dest='arguments')
(options, args) = parser.parse_args()

def runcmd(cmd):
    print cmd
    status, output = commands.getstatusoutput(cmd)
    print output
    return status, output
    
job_return_status = 0

# cleanup
os.system("rm info_*")

# run cmsRun the first time to get infos
cmd = "cmsRun runMakeTreeFromMiniAOD_cfg.py %s" % options.arguments
status, output = runcmd(cmd)

aod_files = []
with open("info_aodfilenames", "r") as fin:
    aod_files = fin.read().replace("\n", "").split(",")
print "Will loop over files:", str(aod_files)

outfile_general = ""
with open("info_outfilename", "r") as fin:
    outfile_general = fin.read().split("\n")[0]

numstart = int(options.arguments.split("nstart=")[-1].split()[0])
print "numstart", numstart

for i_file, aod_file in enumerate(aod_files):
   
    file_number = (numstart * len(aod_files)) + i_file
    outfile = "_".join(outfile_general.split("_")[:-2]) + "_" + str(file_number) + "_RA2AnalysisTree"
    
    print "Doing input file:", aod_file
    print "CMSSW arguments:", options.arguments
    print "Output file:", outfile
    print "Output path:", options.outpath

    os.system("echo %s > info_aods" % aod_file)

    print "check if output file already exists:"
    cmd = "xrdfs root://dcache-cms-xrootd.desy.de/ stat %s/%s.root" % (options.outpath.replace("srm://dcache-se-cms.desy.de", ""), outfile)
    status, output = runcmd(cmd)

    if status == 0:
        print "outfile file already exists on dcache."
        continue
        
    # locate the corresponding miniAODs... come to papa
    os.system('cp "$CMSSW_BASE/src/TreeMaker/Production/test/get_miniAOD.py" .')
    os.system('chmod +x get_miniAOD.py')
    cmd = './get_miniAOD.py --infile=%s' % aod_file
    status, output = runcmd(cmd)

    if status == 123:
      print "empty union json, ignoring lumisection"
      continue
      
    # run cmsRun the second time to run with miniaod.root in sidecar
    os.system("echo %s > info_outfilename" % outfile)
    cmd = "cmsRun runMakeTreeFromMiniAOD_cfg.py %s" % options.arguments
    status, output = runcmd(cmd)
    
    if status != 0:
        job_return_status = status
        continue
    
    # run test script to check if output file has a tracks collection:
    os.system('cp "$CMSSW_BASE/src/TreeMaker/Production/test/check_if_tracks_present.py" .')
    os.system('chmod +x check_if_tracks_present.py')
    cmd = 'python check_if_tracks_present.py'
    status, output = runcmd(cmd)
    
    if status != 0:
        job_return_status = status
       
    # copy output (retry 10 times if failed):
    shell_script = """
    #!/bin/bash
    echo "prepare gfal tools"
    if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh" ]; then
        . /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh
    fi        

    gfal-copy -n 1 file://%s/%s.root %s/%s.root
    exit($?)
    """ % (os.getcwd(), outfile, options.outpath, outfile)

    with open("script_gfalcopy", "w+") as fout:
        fout.write(shell_script)
    os.sytem("chmod +x shell_script")

    for i in range(10):
        status, output = runcmd("./script_gfalcopy")
        job_return_status = status
        if status == 0:
            break
        print "Copy failed, retry in 60s"
        
        time.sleep(60)

    print "rm %s.root" % outfile
    os.system("rm %s.root" % outfile)

    print "\n\n============next file=============\n\n"

quit(job_return_status)

