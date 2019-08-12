#!/bin/env python
from ROOT import * 
import os, glob
from optparse import OptionParser
import commands
import multiprocessing 

def get_all_processed_files(dcache_user):

    print "Getting file list from Desy pnfs..."
    return glob.glob("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3/*root" % dcache_user)


def rename_file(original_file_name, message, dryrun):

    print message

    file_name = original_file_name

    folder = "/".join(file_name.split("/")[:-1])
    file_name_without_index = "_".join(original_file_name.split("_")[:-2])

    dataset = file_name_without_index.split("/")[-1]
    datatream = dataset.split(".")[1].split("AOD")[0]
    identifier = dataset.split(".")[0]

    # check if file name follows naming scheme
    running_index = original_file_name.split("_")[-2]
    if "-" in running_index:
        print "Already renamed:", original_file_name
        return

    # get run, lumi, event number of first event in tree:
    tree = TChain("TreeMaker2/PreSelection")
    tree.Add(file_name)
    RunNum = -1
    LumiBlockNum = -1
    EvtNum = -1
    for event in tree:
        RunNum = event.RunNum
        LumiBlockNum = event.LumiBlockNum
        EvtNum = event.EvtNum
        break

    cmd = 'edmPickEvents.py "/%s/%s/AOD" %s:%s:%s' % (datatream, identifier, RunNum, LumiBlockNum, EvtNum)
    print cmd
    status, output = commands.getstatusoutput(cmd)
    print output
    if status != 0:
        print "Error with running edmPickEvents"
        quit()

    aod_file_name = ""
    for line in output.split("\n"):
        if "inputFiles" in line:
            try:
                aod_file_name =  line.split("/")[7] + "-" + line.split("/")[8].replace(".root", "")
                break
            except:
                print "edmPickEvent issue with:", original_file_name
                return

    if len(aod_file_name)>0:
        updated_file_name = file_name_without_index +"_%s_RA2AnalysisTree.root" % aod_file_name
    else:
        print "Error with running edmPickEvents"
        quit()

    cmd = "gfal-rename srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s" % (original_file_name, updated_file_name)
    print cmd
    os.system("echo '%s' >> rename.log" % cmd)
    # also save script to revert all changes:
    cmd_revert = "gfal-rename srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s" % (updated_file_name, original_file_name)
    os.system("echo '%s' >> rename-revert.sh" % cmd_revert)

    if options.dryrun:
        return

    status, output = commands.getstatusoutput(cmd)
    os.system("echo '%s' >> rename.log" % output)
    os.system("echo '============' >> rename.log")
    print output
    if status == 17:
        print "File exists, moving to duplicates directory..."
        cmd = "gfal-rename srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s" % (original_file_name, updated_file_name.replace("ProductionRun2v3", "ProductionRun2v3_duplicates"))
        status, output = commands.getstatusoutput(cmd)
        os.system("echo '%s' >> rename.log" % cmd)
        os.system("echo '%s' >> rename.log" % output)
        os.system("echo '============' >> rename.log")
        print output
    elif status != 0:
        print "Error with gfal-rename"
        os.system("echo 'ERROR' >> rename.log")
       

def rename_file_wrapper(parameters):

    rename_file(parameters[0], parameters[1], parameters[2])
       

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--username", dest="username")
    parser.add_option("--threads", dest="threads", default=5)
    parser.add_option("--dryrun", dest="dryrun", action="store_true")
    (options, args) = parser.parse_args()

    # check username:
    if not options.username:
        print "No DCache/CERN username given, use --username to specify it"
        quit()

    # check proxy
    status, output = commands.getstatusoutput("voms-proxy-info")
    for line in output.split("\n"):
        if "not found" in line:
            print "Proxy not found! Run:\nvoms-proxy-init -voms cms:/cms -valid 192:00"
            quit()

    # create directory for duplicates:
    cmd = "gfal-mkdir srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3_duplicates" % options.username
    status, output = commands.getstatusoutput(cmd)
    if status == 17:
        print "Folder exists, that's fine"
    
    # loop over all files and rename them:
    pool = multiprocessing.Pool(int(options.threads))
    parameters = []
    files = get_all_processed_files(options.username)
    n_files = len(files)

    for i_file, file_name in enumerate(files):

        # Only data for now!
        if "Run201" not in file_name: continue

        message = "%s / %s" % (i_file, n_files)
        parameters.append([file_name, message, options.dryrun])

    print pool.map(rename_file_wrapper, parameters) 
