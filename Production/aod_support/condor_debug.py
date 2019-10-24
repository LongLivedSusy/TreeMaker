#!/bin/env python
import os, glob
import commands

def get_userlist():
    userlist = []
    hub_folders = glob.glob("/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/")
    for hub_folder in hub_folders:
        if "amohamed" in hub_folder: continue
        userlist.append(hub_folder.split("/")[-3])
    return userlist


def run_on_uscms(cmd, path):
    cmd = "ssh uscms 'cd %s; %s'" % (path, cmd)
    status, output = commands.getstatusoutput(cmd)
    
    if status != 0:
        print "Problem:", path, cmd
        quit()

    try:
        return int(output)
    except:
        return output


for user in get_userlist():

    cmsswver = "CMSSW_9_4_11"

    path = "/home/%s/treemaker/%s/src/TreeMaker/Production/test/condorSub" % (user, cmsswver)
    if user == "sbein":
        path = "/home/%s/ShortTrackSusy/NtupleMakerWithMiniaod/%s/src/TreeMaker/Production/test/myProduction" % (user, cmsswver)
    elif user == "aksingh":
        path = "/home/akshansh/treemaker/%s/src/TreeMaker/Production/test/condorSub" % (cmsswver)

    print "user: %s" % user    
    n_total = run_on_uscms('grep "Doing input file" *stdout | wc -l', path)
    print "  n_total:", n_total
    n_alreadydone = run_on_uscms('grep "outfile file already exists on dcache." *stdout | wc -l', path)
    print "  n_alreadydone:", n_alreadydone
    n_FileOpenError = run_on_uscms('grep "FileOpenError" *stdout | wc -l', path)
    print "  n_FileOpenError:", n_FileOpenError
    n_miniAODerror = run_on_uscms('grep "error while getting miniAOD file name" *stdout | wc -l', path)
    print "  n_miniAODerror:", n_miniAODerror
    n_success = run_on_uscms('grep "run test script" *stdout | wc -l', path)
    print "  n_success:", n_success

