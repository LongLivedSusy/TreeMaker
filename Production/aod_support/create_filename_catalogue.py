#!/bin/env python
from dbs.apis.dbsClient import DbsApi
from optparse import OptionParser
import commands
import time
import os

# Run before:
# voms-proxy-init -voms cms:/cms -valid 192:00
# source /cvmfs/cms.cern.ch/crab3/crab.sh
#
# run e.g.
#
# ./get_miniaod_filenames_from_dbs.py --campaign Run2018A --treemaker_path ~/treemaker/CMSSW_10_2_7/src/TreeMaker/

dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')

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
       ("EGamma" in i_File and "Run2018A" in i_File and "/MINIAOD/17Sep2018-v2/" in dataset) or \
       ("EGamma" in i_File and "Run2018B" in i_File and "/MINIAOD/26Sep2018-v1/" in dataset) or \
       ("EGamma" in i_File and "Run2018C" in i_File and "/MINIAOD/17Sep2018-v1/" in dataset) or \
       ("EGamma" in i_File and "Run2018D" in i_File and "/MINIAOD/22Jan2019-v2/" in dataset) or \
       ("Run2018A" in i_File and "/MINIAOD/17Sep2018-v1/" in dataset) or \
       ("Run2018B" in i_File and "/MINIAOD/17Sep2018-v1/" in dataset) or \
       ("Run2018C" in i_File and "/MINIAOD/17Sep2018-v1/" in dataset) or \
       ("Run2018D" in i_File and "/MINIAOD/PromptReco-v1/" in dataset) or \
       ("Run2018D" in i_File and "/MINIAOD/PromptReco-v2/" in dataset) or \
       ("RunIISummer16DR80Premix" in i_File and "/MINIAODSIM/PUMoriond17_94X" in dataset) or \
       ("RunIISummer16DR80Premix" in i_File and "/MINIAODSIM/PUMoriond17_longlived_94X_mcRun2_asymptotic_v3-v2" in dataset) or \
       ("Summer16" in i_File and "/RunIISummer16MiniAODv2/" in dataset) or \
       ("RunIIFall17" in i_File and "/RunIIFall17MiniAODv2/" in dataset) or \
       ("RunIIAutumn18" in i_File and "/RunIIAutumn18MiniAOD/" in dataset):
        return True
    else:
        return False


def do_queries(aod_file_name, campaign, debug = True):

    miniaod_filenames = []

    # first check children for miniAODs:
    print "do children", aod_file_name
    children = dbs.listFileChildren(logical_file_name = aod_file_name )
    if debug: print "children", children

    # children: is a list of dicts

    if children and len(children)>0:  
        child_filenames = [x["child_logical_file_name"] for x in children]
        for child in child_filenames:
            if dataset_is_correct_miniAOD(aod_file_name, child):
                
                # veto RunIISummer16MiniAODv3 for Summer16 campaign (DTrack analysis uses RunIISummer16MiniAODv2)
                if "Summer16" in campaign and campaign != "RunIISummer16MiniAODv3" and campaign != "Summer16v3Fast":
                    if "RunIISummer16MiniAODv2" not in child:
                        continue
                
                miniaod_filenames.append(child)

    # if no matches have been found, check children of parent files for matching miniAODs:
    if len(miniaod_filenames) == 0:
        parents = dbs.listFileParents(logical_file_name = aod_file_name )
        if debug: print "parents", parents
        if parents and len(parents)>0:
            parents_filenames = parents[0]["parent_logical_file_name"]

            if isinstance(parents_filenames, str): parents_filenames = [parents_filenames]

            for parent_filename in parents_filenames:
                cousins = dbs.listFileChildren(logical_file_name = parent_filename )
                if cousins and len(cousins)>0:
                    if debug: print "cousins", cousins
                    if not cousins or not len(cousins)>0 or not "child_logical_file_name" in cousins[0]: return False
                    cousins_filenames = cousins[0]["child_logical_file_name"]       
                    for cousin in cousins_filenames:
                        if dataset_is_correct_miniAOD(aod_file_name, cousin):
                            miniaod_filenames.append(cousin)

    miniaod_filenames = list(set(miniaod_filenames))

    return miniaod_filenames


def main(treemaker_path, campaign, debug, outfile = "", check_if_already_queried = False):
    
    # check for VOMS proxy:
    status, file_names_string = commands.getstatusoutput("voms-proxy-info -exists")
    if status != 0:
        print "No VOMS proxy"
        return
        
    if outfile == "":
        outfile = campaign

    status, file_names_string = commands.getstatusoutput("grep '.root' %s/Production/python/%s*/*AOD*py | grep '#' -v " % (treemaker_path, campaign))
    if status != 0:
        print file_names_string
        return

    file_names = []
    all_file_names = file_names_string.split("\n")
    for i in range(len(all_file_names)):
        if "QCD_Pt" in all_file_names[i]: continue
        if "RPV_" in all_file_names[i]: continue
        if "StealthS" in all_file_names[i]: continue
        #if "SMS" in all_file_names[i]: continue

        file_names.append( all_file_names[i].split("'")[1] )

    print "Total # of files: %s" % len(file_names)
    print "First file in list: %s" % file_names[0]   

    output = ""
    for i, aod_file_name in enumerate(file_names):

        #if (i % 100 == 0 and i > 0) or debug:
        print "%s / %s done" % (i, len(file_names))

        # check if we already have the info:
        if check_if_already_queried:
            # this can take some time when grepping large file name catalogues
            status, ignore = commands.getstatusoutput("grep %s ../test/catalogue*.dat" % (aod_file_name))
            if status == 0: 
                print "already there", aod_file_name
                continue

        file_has_issues = False

        miniaod_filenames = False
        try:
            #print "aod_file_name", aod_file_name
            miniaod_filenames = do_queries(aod_file_name, campaign, debug)
            #print "miniaod_filenames", miniaod_filenames
        except Exception as e:
            print "Got error with file (# %s)" % i, aod_file_name
            print str(e)
            file_has_issues = True
            continue
            
    	#if not miniaod_filenames:
     	#    print "Got error with file (# %s)" % i, aod_file_name
        #    file_has_issues = True

        #if file_has_issues:
        #    os.system("echo %s >> files_with_issues_ext90.%s" % (aod_file_name, outfile))
        #    continue

        output = "[%s]\n%s\n" % (aod_file_name, "\n".join(miniaod_filenames))
        print output

        if i % 1000 == 0 and i > 0:
            print "Pausing..."
            time.sleep(200)
            print "Resuming..."
        
    fout = open("../test/catalogue_%s.dat" % outfile, "a")
    fout.write(output)
    fout.close()
 

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option('--campaign', dest = 'campaign', default = "all")
    parser.add_option('--treemaker_path', dest = 'treemaker_path', default = "~/dust/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/")
    parser.add_option('--debug', action = "store_true", dest = 'debug')
    (options, args) = parser.parse_args()

    if options.campaign == "all":
        for campaign in [
                          "Run2016B-17Jul2018_ver1-v1",
                          "Run2016B-17Jul2018_ver2-v1",
                          "Run2016B-17Jul2018_ver2-v2",
                          "Run2016C-17Jul2018-v1",
                          "Run2016D-17Jul2018-v1",
                          "Run2016E-17Jul2018-v1",
                          "Run2016F-17Jul2018-v1",
                          "Run2016G-17Jul2018-v1",
                          "Run2016H-17Jul2018-v1",
                          "Run2016H-17Jul2018-v2",
                          "Run2017B-31Mar2018-v1",
                          "Run2017C-31Mar2018-v1",
                          "Run2017D-31Mar2018-v1",
                          "Run2017E-31Mar2018-v1",
                          "Run2017F-31Mar2018-v1",
                          "Run2018D-PromptReco-v2",
                          "Run2018A-17Sep2018-v1",
                          "Run2018B-17Sep2018-v1",
                          "Run2018C-17Sep2018-v1",
                          "Run2018D-PromptReco-v1",
        ]:
            main(options.treemaker_path, campaign, options.debug)
        
    else:
        main(options.treemaker_path, options.campaign, options.debug)


