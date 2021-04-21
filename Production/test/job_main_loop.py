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


def check_dcache_if_file_exists(outpath, outfile):

    userlist = ["aksingh", "spak", "jarieger", "tokramer", "ssekmen", "jsonneve", "sbein", "vkutzner", "vormwald", "ynissan"]

    print "\nCheck if output file already exists in a user folder..."
    username = outpath.split("/store/user/")[1].split("/")[0]

    for user in userlist:

        cmd = "xrdfs root://dcache-cms-xrootd.desy.de/ stat %sProductionRun2v3/%s.root" % (outpath.replace("srm://dcache-se-cms.desy.de", ""), outfile)
        if user == "vkutzner":
            cmd = "xrdfs root://dcache-cms-xrootd.desy.de/ stat %sProductionRun2v3_akshansh/%s.root" % (outpath.replace("srm://dcache-se-cms.desy.de", ""), outfile)
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

        if check_dcache_if_file_exists(options.outpath, options.arguments.split("inputFilesConfig=")[-1].split()[0] + outfile):
            continue
          
        # copy all necessary files manually:
        print "Copy AOD file..."
        status, output = runcmd("xrdcp root://xrootd-cms.infn.it/%s ./" % aod_file.replace("\n", ""))
        if status == 0:
            runcmd("echo %s > info_aods" % aod_file.split("/")[-1])
            aod_file = aod_file.split("/")[-1]
        else:
            runcmd("echo %s > info_aods" % aod_file)
           
        print "\nLocate the corresponding miniAODs..."
        runcmd('cp $CMSSW_BASE/src/TreeMaker/Production/test/catalogue*.dat .')
        runcmd('cp "$CMSSW_BASE/src/TreeMaker/Production/test/get_miniAOD_filenames_from_catalogue.py" .')
        runcmd('chmod +x get_miniAOD_filenames_from_catalogue.py')
        cmd = './get_miniAOD_filenames_from_catalogue.py --infile=%s' % aod_file
        status, output = runcmd(cmd)

        if status == 123:
            print "Lumisection was masked (empty JSON)"
            runcmd("rm *.root")
            continue
        elif status != 0:
            job_return_status = status
            print "error while getting miniAOD file name..."
            runcmd("rm *.root")
            continue
        
        # copy all necessary files manually:
        print "Copy miniAOD file(s)..."
        with open("info_miniaods", "r") as fin:
            miniaod_list = fin.read().split(",")
        for i, miniaod in enumerate(miniaod_list):
            status, output = runcmd("xrdcp root://xrootd-cms.infn.it/%s ./" % miniaod.replace("\n", ""))
            if status == 0:
                miniaod_list[i] = miniaod_list[i].split("/")[-1]
            
        # update miniAOD file list
        with open("info_miniaods", "w") as fin:
            fin.write(",".join(miniaod_list))
        
        print "run cmsRun the second time to run with miniaod.root in sidecar:"
        runcmd("echo %s > info_outfilename" % outfile)
        cmd = "cmsRun runMakeTreeFromMiniAOD_cfg.py %s" % options.arguments
        status, output = runcmd(cmd)
        
        if status != 0:
            job_return_status = status
            runcmd("rm *.root")
            continue
        else:
            print "Success!"
        
        print "run test script to check if output file has a tracks collection:"
        runcmd('cp "$CMSSW_BASE/src/TreeMaker/Production/test/check_if_tracks_present.py" .')
        runcmd('chmod +x check_if_tracks_present.py')
        cmd = 'python check_if_tracks_present.py'
        status, output = runcmd(cmd)
        
        if status != 0:
            job_return_status = status
            
        complete_outfile = options.arguments.split("inputFilesConfig=")[-1].split()[0] + outfile    
        
        # copy output:
        shell_script = """
        #!/bin/bash
        echo "prepare gfal tools"
        if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh" ]; then
            . /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh
        fi        
        
        find $PWD -type f -name "*RA2AnalysisTree.root" -maxdepth 1 | awk '{print "file://"$0}' > files.txt
        gfal-copy -n 1 -f --from-file files.txt %s/
        exit $?
        """ % (options.outpath)
                
        with open("script_gfalcopy", "w+") as fout:
            fout.write(shell_script)
        runcmd("chmod +x script_gfalcopy")
        job_return_status, output = runcmd("./script_gfalcopy")
        runcmd("rm *.root")

    quit(job_return_status)
