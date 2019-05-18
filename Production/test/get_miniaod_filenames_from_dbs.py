#!/bin/env python
from dbs.apis.dbsClient import DbsApi
from optparse import OptionParser
import commands
import time
import os

# Run before:
# voms-proxy-init -voms cms:/cms -valid 192:00
# source /cvmfs/cms.cern.ch/crab3/crab.sh

dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')

parser = OptionParser()
parser.add_option('--campaign', dest='campaign')
parser.add_option('--treemaker_path', dest='treemaker_path')
(options, args) = parser.parse_args()

def dataset_is_correct_miniAOD(i_File, dataset):

    if ("Run2016B" in i_File and "/MINIAOD/17Jul2018_ver1-v1/" in dataset) or \
       ("Run2016B" in i_File and "/MINIAOD/17Jul2018_ver2-v1/" in dataset) or \
       ("Run2016B" in i_File and "/MINIAOD/17Jul2018_ver2-v2/" in dataset) or \
       ("Run2016C" in i_File and "/MINIAOD/17Jul2018-v1/" in dataset) or \
       ("Run2016D" in i_File and "/MINIAOD/17Jul2018-v1/" in dataset) or \
       ("Run2016E" in i_File and "/MINIAOD/17Jul2018-v1/" in dataset) or \
       ("Run2016F" in i_File and "/MINIAOD/17Jul2018-v1/" in dataset) or \
       ("Run2016G" in i_File and "/MINIAOD/17Jul2018-v1/" in dataset) or \
       ("Run2016H" in i_File and "/MINIAOD/17Jul2018-v1/" in dataset) or \
       ("Run2016H" in i_File and "/MINIAOD/17Jul2018-v2/" in dataset) or \
       ("Run2017"  in i_File and "/MINIAOD/31Mar2018-v1/" in dataset) or \
       ("Run2018A" in i_File and "/MINIAOD/17Sep2018-v1/" in dataset) or \
       ("Run2018B" in i_File and "/MINIAOD/17Sep2018-v1/" in dataset) or \
       ("Run2018C" in i_File and "/MINIAOD/17Sep2018-v1/" in dataset) or \
       ("Run2018D" in i_File and "/MINIAOD/PromptReco-v1/" in dataset) or \
       ("Run2018D" in i_File and "/MINIAOD/PromptReco-v2/" in dataset) or \
       ("Summer16" in i_File and "/RunIISummer16MiniAODv2/" in dataset) or \
       ("RunIIFall17" in i_File and "/RunIIFall17MiniAODv2/" in dataset):
        return True
    else:
        return False


def do_queries(aod_file_name):

    miniaod_filenames = []

    # first check children for miniAODs:
    children = dbs.listFileChildren(logical_file_name = aod_file_name )
    if not children or not len(children)>0 or not "child_logical_file_name" in children[0]: return False
    
    child_filenames = children[0]["child_logical_file_name"]
    for child in child_filenames:
        if dataset_is_correct_miniAOD(aod_file_name, child):
            miniaod_filenames.append(child)

    # if no matches have been found, check children of parent files for matching miniAODs:
    if len(miniaod_filenames) == 0:
        parents = dbs.listFileParents(logical_file_name = aod_file_name )

        if not parents or not len(parents)>0 or not "parent_logical_file_name" in parents[0]: return False
        parents_filenames = parents[0]["parent_logical_file_name"]

        for parent_filename in parents_filenames:
            cousins = dbs.listFileChildren(logical_file_name = parent_filename )
            if not cousins or not len(cousins)>0 or not "child_logical_file_name" in cousins[0]: return False
            cousins_filenames = cousins[0]["child_logical_file_name"]       
            for cousin in cousins_filenames:
                if dataset_is_correct_miniAOD(aod_file_name, cousin):
                    miniaod_filenames.append(cousin)

    return miniaod_filenames


def main(treemaker_path, campaign, outfile = ""):
    
    # check for VOMS proxy:
    status, file_names_string = commands.getstatusoutput("voms-proxy-info -exists")
    if status != 0:
        print "No VOMS proxy"
        return
        
    if outfile == "":
        outfile = campaign

    status, file_names_string = commands.getstatusoutput("grep '.root' %s/Production/python/%s*/*AOD*py" % (treemaker_path, campaign))
    if status != 0:
        return

    file_names = []
    all_file_names = file_names_string.split("\n")
    for i in range(len(all_file_names)):
        if "QCD_Pt" in all_file_names[i]: continue
        if "RPV_" in all_file_names[i]: continue
        if "StealthS" in all_file_names[i]: continue
        if "SMS" in all_file_names[i]: continue

        file_names.append( all_file_names[i].split("'")[1] )

    print "Total # of files: %s" % len(file_names)
    print "First file in list: %s" % file_names[0]   

    fout = open("catalogue_%s.dat" % outfile, "a")

    for i, aod_file_name in enumerate(file_names):

        if i % 100 == 0 and i > 0:
            print "%s / %s done" % (i, len(file_names))

        # check if we already have the info:
        status, ignore = commands.getstatusoutput("grep %s catalogue_%s.dat" % (aod_file_name, outfile))
        if status == 0: continue

        file_has_issues = False

        try:
            miniaod_filenames = do_queries(aod_file_name)
        except Exception as e:
            print "Got error with file (# %s)" % i, aod_file_name
            print str(e)
            file_has_issues = True
            
    	if not miniaod_filenames:
     	    print "Got error with file (# %s)" % i, aod_file_name
            file_has_issues = True

        if file_has_issues:
            os.system("echo %s >> files_with_issues.%s" % (aod_file_name, outfile))
            continue

        output = "[%s]\n%s\n" % (aod_file_name, "\n".join(miniaod_filenames))
        fout.write(output)

        if i % 100 == 0 and i > 0:
            print aod_file_name, str(miniaod_filenames)
            fout.flush()
        if i % 1000 == 0 and i > 0:
            print "Pausing..."
            time.sleep(60)
            print "Resuming..."
         
    fout.close()
 

if __name__ == "__main__":

    #treemaker_path = "~/treemaker/CMSSW_10_2_7/src/TreeMaker/"
    #campaign = "RunIIFall17"
    treemaker_path = options.treemaker_path
    campaign = options.campaign
       
    main(treemaker_path, campaign)


