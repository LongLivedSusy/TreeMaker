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

print duplicates
print len(duplicates)

with open('dupes.txt', 'w') as f:
    f.write(str(duplicates))

raw_input("remove %s dupes?" % len(duplicates))

#print "Creating directory for files using old naming scheme"
#for username in get_userlist():
#    cmd = "eval `scram unsetenv -sh`; gfal-mkdir srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/duplicates_ProductionRun2v3" % username
#    status, output = commands.getstatusoutput(cmd)
#    if status == 17:
#        print "Folder exists, that's fine"

prodfolders = [
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/duplicates_ProductionRun2v3",
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/duplicates_ProductionRun2v3_2",
           #"/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/old_ProductionRun2v3",
           "/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v3",
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

print "Creating directory for files using old naming scheme"
for prodfolder in prodfolders:
    cmd = "eval `scram unsetenv -sh`; gfal-mkdir srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s" % prodfolder.replace("ProductionRun2v3", "duplicates_ProductionRun2v3")
    status, output = commands.getstatusoutput(cmd)
    if status == 17:
        print "Folder exists, that's fine"

raw_input("ok finished creating folders.")

print "Moving files to different folder..."

for i_file_name, file_name in enumerate(duplicates):

    if ".root" not in file_name:
        continue

    print "%s / %s" % (i_file_name, len(duplicates))

    folders = duplicates[file_name][1:]

    for folder in folders:
        file_to_be_deleted = folder + "/" + file_name
        cmd = "eval `scram unsetenv -sh`; gfal-rename srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s" % (file_to_be_deleted, file_to_be_deleted.replace("ProductionRun2v3", "duplicates_ProductionRun2v3"))
        print cmd
        status, output = commands.getstatusoutput(cmd)
        print output
