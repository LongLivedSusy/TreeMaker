#!/bin/env python
import os
from optparse import OptionParser
import commands
import collections
import glob
import time

# loop over multiple AOD input files and process them one-by-one instead of loading all files
# files are copied directly after each file has been processed

def runcmd(cmd):
    print cmd
    status, output = commands.getstatusoutput(cmd)
    print output
    return status, output


def check_dcache_if_file_exists(outpath, outfile, userlist):

    print "\nCheck if output file already exists in a user folder..."
    username = outpath.split("/store/user/")[1].split("/")[0]

    for user in userlist:

        cmd = "xrdfs root://dcache-cms-xrootd.desy.de/ stat %s/%s.root" % (outpath.replace("srm://dcache-se-cms.desy.de", ""), outfile)
        cmd = cmd.replace("/%s/" % username, "/%s/" % user)

        # check if output file already exists for user
        status, output = runcmd(cmd)
        if status == 0:
            print "outfile file already exists on dcache."
            return True
            break

    return False


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option('--outpath', dest='outpath')
    parser.add_option('--arguments', dest='arguments')
    (options, args) = parser.parse_args()
       
    job_return_status = 0

    # cleanup
    runcmd("rm info_* *root")

    print "run cmsRun the first time. The exit code 78 is expected:"
    cmd = "cmsRun runMakeTreeFromMiniAOD_cfg.py %s" % options.arguments
    status, output = runcmd(cmd)

    aod_files = []
    with open("info_aodfilenames", "r") as fin:
        aod_files = fin.read().replace("\n", "").split(",")
    print "Will loop over files:", str(aod_files)

    outfile_general = ""
    with open("info_outfilename", "r") as fin:
        outfile_general = fin.read().split("\n")[0]

    # get dcache user directories:
    status, userlist = runcmd("curl http://www.desy.de/~kutznerv/ntuple-production/userlist")
    userlist = userlist.replace("\n", "").split(",")

    numstart = int(options.arguments.split("nstart=")[-1].split()[0])
    print "numstart", numstart

    for i_file, aod_file in enumerate(aod_files):
       
        # construct output file name from input AOD file:
        # example: /store/data/Run2018C/EGamma/AOD/17Sep2018-v1/100001/6300647F-B9D5-3348-B8BF-71F26C664BA5.root
        
        aodfile_uuid = aod_file.split("/")[-2] + "-" + aod_file.split("/")[-1].replace(".root", "")
        outfile = "_".join(outfile_general.split("_")[:-2]) + "_" + aodfile_uuid + "_RA2AnalysisTree"
        
        print "\n\nDoing input file:", aod_file
        print "CMSSW arguments:", options.arguments
        print "Output file:", outfile
        print "Output path:", options.outpath

        runcmd("echo %s > info_aods" % aod_file)

        if check_dcache_if_file_exists(options.outpath, outfile, userlist):
            continue
           
        print "\nLocate the corresponding miniAODs..."
        runcmd('cp $CMSSW_BASE/src/TreeMaker/Production/test/catalogue*.dat .')
        runcmd('cp "$CMSSW_BASE/src/TreeMaker/Production/test/get_miniAOD_filenames_from_catalogue.py" .')
        runcmd('chmod +x get_miniAOD_filenames_from_catalogue.py')
        cmd = './get_miniAOD_filenames_from_catalogue.py --infile=%s' % aod_file
        status, output = runcmd(cmd)

        if status == 123:
            print "Lumisection was masked (empty JSON)"
            print "Creating empty ROOT file..."
            os.system("echo masked > %s.root" % outfile)
        elif status != 0:
            job_return_status = status
            print "error while getting miniAOD file name..."
            continue
          
        print "run cmsRun the second time to run with miniaod.root in sidecar:"
        runcmd("echo %s > info_outfilename" % outfile)
        cmd = "cmsRun runMakeTreeFromMiniAOD_cfg.py %s" % options.arguments
        status, output = runcmd(cmd)
        
        if status != 0:
            job_return_status = status
            runcmd("rm %s.root" % outfile)
            continue
        
        print "run test script to check if output file has a tracks collection:"
        runcmd('cp "$CMSSW_BASE/src/TreeMaker/Production/test/check_if_tracks_present.py" .')
        runcmd('chmod +x check_if_tracks_present.py')
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

    #gfal-copy -n 1 file://%s/%s.root %s/%s.root
    find $PWD -type f -name "*.root" -maxdepth 1 | awk '{print "file://"$0}' > files.txt
    gfal-copy -n 1 -f --from-file files.txt %s/
    exit $?
    """ % (os.getcwd(), outfile, options.outpath, outfile, options.outpath)

    with open("script_gfalcopy", "w+") as fout:
        fout.write(shell_script)
    runcmd("chmod +x script_gfalcopy")

    for i in range(4):
        status, output = runcmd("./script_gfalcopy")
        if status != 0:
            job_return_status = status
        if status == 0 or status == 17:
            # status code 17: file exists
            break
        print "Copy failed, retry in 60s"
        time.sleep(400)

    print "rm *.root"
    runcmd("rm *.root")

    quit(job_return_status)
