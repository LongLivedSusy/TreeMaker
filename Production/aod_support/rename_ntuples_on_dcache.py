#!/bin/env python
from ROOT import * 
import os, glob
from optparse import OptionParser
import commands

def get_all_processed_files(dcache_user):

    print "Getting file list from Desy pnfs..."

    return glob.glob("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3/*root" % dcache_user)


def rename_file(original_file_name, verbose):

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

    folder = "/".join(file_name.split("/")[:-1])
    file_name_without_index = "_".join(original_file_name.split("_")[:-2])
    updated_file_name = file_name_without_index +"_%s_%s_%s_RA2AnalysisTree.root" % (RunNum, LumiBlockNum, EvtNum)

    if verbose:
        print "%s --> %s" % (original_file_name, updated_file_name)

    cmd = "gfal-rename srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=%s" % (original_file_name, updated_file_name)
    print cmd
    status, output = commands.getstatusoutput(cmd)
    print output
    if status != 0:
        print "Error"
        quit()
    
       
if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--verbose", dest="verbose", action="store_true")
    parser.add_option("--username", dest="username", default="vkutzner")
    (options, args) = parser.parse_args()

    files = get_all_processed_files(options.username)

    for file_name in files:
        rename_file(file_name, options.verbose)
        break


