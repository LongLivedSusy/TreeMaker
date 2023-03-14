#!/bin/env python
import os, sys, glob
from ROOT import *
import datetime as dt
import commands
from collections import OrderedDict 
from optparse import OptionParser
import time
import datetime
from time import gmtime, strftime
import uuid
import json
from GridEngineTools import runParallel

def get_userlist():
    userlist = []
    hub_folders = glob.glob("/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/")
    for hub_folder in hub_folders:
        userlist.append(hub_folder.split("/")[-3])
    return userlist


def get_all_files():

    #all_files = []
    #for username in get_userlist():
    #    print "Checking for files of %s..." % username
    #    all_files += glob.glob("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3*/*.root" % username)
    #all_files += glob.glob("/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/ProductionRun2v3_akshansh/*.root")
    #return all_files

    return glob.glob("/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v3*/*.root")


d = {}
duplicates = {}

for ifile in get_all_files():
    
    foldername = "/".join(ifile.split("/")[:-1])
    filename = ifile.split("/")[-1]

    if filename in d:
        d[filename].append(foldername)
        print d[filename]
        duplicates[filename] = list(set(d[filename]))
    else:
        d[filename] = [foldername]

print len(duplicates)

with open('dupes.txt', 'w') as f:
    f.write(str(duplicates))

quit()

raw_input("remove %s dupes?" % len(duplicates))

#print "Creating directory for files using old naming scheme"
#for username in get_userlist():
#    cmd = "eval `scram unsetenv -sh`; gfal-mkdir srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/duplicates_ProductionRun2v3" % username
#    status, output = commands.getstatusoutput(cmd)
#    if status == 17:
#        print "Folder exists, that's fine"

prodfolders = [
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/duplicates_ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/duplicates_ProductionRun2v3_2",
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/old_ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v3_jarieger",
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v3_jsonneve",
           #"/pnfs/desy.de/cms/tier2/store/user/spak/NtupleHub/ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/ssekmen/NtupleHub/ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/tokramer/NtupleHub/ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/duplicates_ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/duplicates_ProductionRun2v3_2",
           #"/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/duplicates_ProductionRun2v3_akshansh",
           #"/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/missingHeaderInfo_ProductionRun2v3",
           "/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/ProductionRun2v3_akshansh",
           #"/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/ProductionRun2v3_vormwald",
           #"/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/ProductionRun2v3",
          ]

#srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=

print "Creating directory for files using old naming scheme"
for prodfolder in prodfolders:
    cmd = "eval `scram unsetenv -sh`; gfal-mkdir srm://dcache-se-cms.desy.de%s" % prodfolder.replace("ProductionRun2v3", "duplicates_ProductionRun2v3")
    status, output = commands.getstatusoutput(cmd)
    if status == 17:
        print "Folder exists, that's fine"

raw_input("ok finished creating folders.")

print "Moving files to different folder..."

cmds = []

for i_file_name, file_name in enumerate(duplicates):

    if ".root" not in file_name:
        continue

    print "%s / %s" % (i_file_name, len(duplicates))

    #folders = duplicates[file_name][1:]
    #len_before = len(folders)   
    #contains_restored = False
    #contains_sms2 = False
    #for folder in folders:
    #    if "SMS2" in folder:
    #
    #if len(folders) == len_before:
    
    folders = duplicates[file_name]

    keep_index = -1
    for i_folder, folder in enumerate(folders):
        if "Run201" in file_name and "restored" in folder:
            keep_index = i_folder
            break
        if "SMS" in file_name and "SMS2" not in folder:
            keep_index = i_folder
            break

    if keep_index != -1:
        del folders[keep_index]
    else:
        folders = duplicates[file_name][1:]
    
    # move files from remaining folders
    for i_folder, folder in enumerate(folders):
        file_to_be_deleted = folder + "/" + file_name

        #if i_folder==0:
        #targetpath = file_to_be_deleted.replace("ProductionRun2v3", "duplicates_ProductionRun2v3")
        targetpath = "/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/duplicates_ProductionRun2v3/%s" % file_to_be_deleted.split("/")[-1]
        if i_folder>0:
            #targetpath = file_to_be_deleted.replace("ProductionRun2v3", "duplicates_ProductionRun2v3").replace(".root", "_%s.root" % i_folder)
            targetpath = targetpath.replace(".root", "_%s.root" % i_folder)
        #cmd = "eval `scram unsetenv -sh`; gfal-rename srm://dcache-se-cms.desy.de%s srm://dcache-se-cms.desy.de%s" % (file_to_be_deleted, targetpath)
        cmd = "gfal-rename srm://dcache-se-cms.desy.de%s srm://dcache-se-cms.desy.de%s" % (file_to_be_deleted, targetpath)
        #print cmd
        #raw_input()
        #status, output = commands.getstatusoutput(cmd)
        #print output
        cmds.append(cmd)

runParallel(cmds, "multi", ncores_percentage=1.0)
