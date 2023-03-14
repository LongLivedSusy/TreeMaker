#!/bin/env python
from  __builtin__ import any as b_any
import os, glob
from optparse import OptionParser
import socket
import Utilities.General.cmssw_das_client as das_client
import commands
import json
import GridEngineTools
import uuid
import time
from os.path import expanduser

# to be run at DESY

def create_processed_filelist():
    #os.system("find /pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v3*/ -exec readlink -e '{}' \; > finished_ntuples_fullpath.dat")
    os.system("ls /pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v3*/ > finished_ntuples.dat")


def file_has_been_processed(campaign, processed_uuids, aod_file, debug = False):
        
    aodfile_uuid = aod_file.split("/")[-2] + "-" + aod_file.split("/")[-1].replace(".root", "")        

    if aodfile_uuid in processed_uuids:
        return True
    else:
        return False


def create_dbs_cache(sample_aod_file):
    
    print "QUERYING...", sample_aod_file
    
    jsondict = das_client.get_data("dataset file=%s" % sample_aod_file)
    dataset = jsondict["data"][0]["dataset"][0]["name"]
    
    jsondict = das_client.get_data("file,run,lumi dataset=%s" % dataset)
    data = jsondict["data"]
    
    print "DONE"
    
    return data


def dbs_query_per_file(sample_aod_file):
    
    print "Querying per file...", sample_aod_file

    if "'" in sample_aod_file:
        sample_aod_file = sample_aod_file.split("'")[1]

    jsondict = das_client.get_data("lumi file=%s" % sample_aod_file)

    data = jsondict["data"]
    file_json = {}
    for i_data in data:
        run = i_data["lumi"][0]["run_number"]
        lumi = i_data["lumi"][0]["lumi_section_num"]
        if run in file_json:
            file_json[run] += [lumi]
        else:
            file_json[run] = [lumi]
 
        #test
        if len(i_data["lumi"]) > 1:
            print "warn", i_data["lumi"]
            quit()

    for run in file_json:
        file_json[run] = sorted(file_json[run])
   
    return file_json
        

#status, fnames = commands.getstatusoutput("cat yeah2.log")
#fnames = fnames.split("\n")

with open('../test/data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt') as f:
    golden16 = json.loads(f.read())
with open('../test/data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt') as f:
    golden17 = json.loads(f.read())
with open('../test/data/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt') as f:
    golden18 = json.loads(f.read())

def is_in_goldenjson(flist, filename):
    
    # for MC:
    if "Run201" not in filename:
        return True 


    
    # for Data:
    for i_flist in flist:
        for i in range(len(i_flist["file"])):
            if filename in i_flist["file"][i]["name"]:
                run = i_flist["run"][0]["run_number"]
                lumisecs = i_flist["lumi"][0]["number"]
                if not (str(run) in golden16 or str(run) in golden17 or str(run) in golden18):
                    print "NOT IN GOLDEN JSON:", filename, ", run:", str(run)
                    return False
                else:    
                    # run in golden json, check lumisections:
                    
                    lumi_golden = []
                    for golden in [golden16, golden17, golden18]:
                        if str(run) in golden:
                            lumi_golden = golden[str(run)]
                    
                    is_in_golden = False
                    for i_lumi_file in lumisecs:
                        for interval in lumi_golden:
                            if i_lumi_file >= interval[0] and i_lumi_file <= interval[1]:
                                is_in_golden = True
                                break
                    
                    if is_in_golden:
                        return True
                    else:
                        print "NOT IN GOLDEN JSON:", filename, ", run:", str(run), ", lumisecs:", lumisecs
                        return False             
                 
    print "file not found in dbs...:", filename    
    return True
    

def json_contains_subset_of_goldenjson(aodname):

    if "'" in aodname:
        aodname = aodname.split("'")[1]

    # for MC:
    if "Run201" not in aodname:
        return 1 

    # file lumi info not available
    status, output = commands.getstatusoutput("grep '%s' dbs.cache.separated" % aodname)
    output = output.split("\n")
    if status == 0:
        filejson = {}
        for line in output:
            runoutput = line.split('"run": [{"run_number": ')[1]
            runoutput = runoutput.split('}]')[0]
            run = int(runoutput)
            lumioutput = line.split('"lumi": [{"number": ')[1]
            lumioutput = lumioutput.split('}]')[0]
            lumis = eval(lumioutput)
            filejson[run] = lumis
        print "redid json:", str(filejson)
    else:
        filejson = dbs_query_per_file(aodname)
        
    if len(filejson) == 0:
        print "giving up", aodname, output
        return 3

    file_in_golden_json = False
    for run in filejson:
        if not (str(run) in golden16 or str(run) in golden17 or str(run) in golden18):
            continue

        lumi_golden = []
        for golden in [golden16, golden17, golden18]:
            if str(run) in golden:
                lumi_golden = golden[str(run)]
                break

        for lumi in filejson[run]:
            for interval in lumi_golden:
                if int(lumi) >= int(interval[0]) and int(lumi) <= int(interval[1]):
                    file_in_golden_json = True
                    break

    #print file_in_golden_json, filejson

    if file_in_golden_json:
        return 1
    else:
        return 0

    # return True if any part of the json is contained in the golden JSON

    

def main(campaign, processed_files, specific_aod_file = -1, debug = False, honor_old_hashes_lumi = True, honor_old_hashes = False, comment_already_processed_files = True, write = True, check_goldenjson = False):

    # read processed files
    processed_files_string = ""
    with open(processed_files, "r") as fin:
        processed_files_string = fin.read()
    processed_files = list(set(processed_files_string.split("\n")))

    for i in range(len(processed_files)):
        if len(processed_files[i].split("_"))>1:
            processed_files[i] = processed_files[i].split("_")[-2]

    processed_uuids = set(processed_files)

    #processed_uuids = "\n".join(processed_files)

    print "%s/*AOD*_cff.py" % campaign

    aod_filelists = sorted(glob.glob("%s/*AOD*_cff.py" % campaign))
    #aod_filelists = sorted(glob.glob("%s/*AOD91*_cff.py" % campaign))
    
    mydbs = False
        
    for i_aod_file, aod_file in enumerate(aod_filelists):

        if int(specific_aod_file) > -1 and int(specific_aod_file) != i_aod_file:
            continue

        #FIXME
        if "DYJetsToLL_M-5to50_HT" in aod_file: continue
       
        print "Checking %s/%s (%s)..." % (i_aod_file, len(aod_filelists), aod_file)

        file_contents = ""
        with open(aod_file, "r") as fin:
            file_contents = fin.read() 

        # check if file is in processed_files        
        file_contents = file_contents.split("\n")
        file_count = 0

        #dataset = ""

        for i in range(len(file_contents)):
            ignore_file = False
            if ".root" in file_contents[i]:

                # existing hashes...
                #if len([s for s in fnames if file_contents[i].split("'")[1] in s])>0:
                #    file_contents[i] = file_contents[i].replace("#", "")

                #file_contents[i] = file_contents[i].split("'")[1]
                #file_contents[i] = "    '%s'," % file_contents[i].split("'")[2]

                ##FIXME
                #if "###" in file_contents[i]:
                #    file_contents[i] = file_contents[i].replace("#", "")

                if "###" in file_contents[i]:
                    if not check_goldenjson:
                        continue
                    
                elif "##" in file_contents[i]:
                    if honor_old_hashes_lumi:
                        continue
                    else:
                        file_contents[i] = file_contents[i].replace("#", "")
                elif "#" in file_contents[i]:
                    if honor_old_hashes:
                        continue
                    else:
                        file_contents[i] = file_contents[i].replace("#", "")

                #file_contents[i] = file_contents[i].replace("#", "")

                #new
                #if dataset == "":
                #    jsondict = das_client.get_data("dataset file=%s" % file_contents[i])
                #    dataset = jsondict["data"][0]["dataset"][0]["name"]

                #if check_goldenjson and not mydbs:
                #    mydbs = create_dbs_cache(file_contents[i])
                #filejson = dbs_query_per_file(file_contents[i])
                                
                if comment_already_processed_files:
                    filename = file_contents[i].split("'")[1]
                    if file_has_been_processed(campaign.split("/")[-1], processed_uuids, filename):
                        file_contents[i] = "#" + file_contents[i]
                    #elif check_goldenjson and not is_in_goldenjson(mydbs, filename):
                    elif check_goldenjson:
                        #filejson = dbs_query_per_file(file_contents[i])
                        #if not json_contains_subset_of_goldenjson(filejson):
                        #    file_contents[i] = "##" + file_contents[i]
                        json_status = json_contains_subset_of_goldenjson(file_contents[i])
                        if json_status == 0:
                            file_contents[i] = "##" + file_contents[i]
                        elif json_status == 3:
                            file_contents[i] = file_contents[i] + " ### no run/lumi info"
                    file_count += 1
                    
        if write:
            with open(aod_file, "w") as fout:
                fout.write("\n".join(file_contents))
            print "%s written!" % aod_file
        

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--update_filelist", dest="update_filelist", action="store_true")
    parser.add_option("--campaign", dest="campaign", default="all")
    parser.add_option("--runmode", dest="runmode", default="multi")
    parser.add_option("--submit", dest="submit", action="store_true")
    parser.add_option("--processed_files", dest="processed_files", default="finished_ntuples.dat")
    parser.add_option("--specific_aod_file", dest="specific_aod_file", default=-1)    
    parser.add_option("--debug", dest="debug", action="store_true")
    (options, args) = parser.parse_args()

    if options.update_filelist or not os.path.exists(os.getcwd() + "/" + options.processed_files):
        create_processed_filelist()

    if options.submit:
        
        if options.campaign == "all":
            campaigns = glob.glob("../python/Run201*")
            #campaigns = glob.glob("../python/Run201*") + ["../python/RunIIFall17MiniAODv2"] + ["../python/Summer16"] + ["../python/RunIISummer16MiniAODv3"] + ["../python/RunIIAutumn18FS"]  + ["../python/RunIIFall17FS"]
            #campaigns = ["../python/RunIIAutumn18FS"]  + ["../python/RunIIFall17FS"]
        else:
            campaigns = glob.glob(options.campaign)
        print "Using campaigns:", campaigns
    
        homedir = expanduser("~")
    
        commands = []
        for campaign in campaigns:
            aod_filelists = sorted(glob.glob("%s/*AOD*_cff.py" % campaign))
            #aod_filelists = sorted(glob.glob("%s/*AOD91*_cff.py" % campaign))
            #aod_filelists = sorted(glob.glob("%s/*PMSSM*AOD*_cff.py" % campaign))
            for i, aod_filelist in enumerate(aod_filelists):
                
                print aod_filelist

                #FIXME
                #if "MET" in aod_filelist and "2018D" in aod_filelist:
                commands.append("HOME=%s; ./check_already_processed_files.py --campaign %s --specific_aod_file %s" % (homedir, campaign, i))

        #FIXME
        #commands = [commands[-1]]
        GridEngineTools.runParallel(commands, options.runmode, ncores_percentage=1.0)

    else:
        campaigns = options.campaign.split(",")
        for campaign in campaigns:
            main("../python/" + campaign, options.processed_files, debug = options.debug, specific_aod_file = options.specific_aod_file)

    #print "Run with e.g.\n ./check_already_processed_files.py --campaign RunIIFall17MiniAODv2 --processed_files finished_ntuples.dat \n"
    #print "Can also run with multiple campaigns separated by commas."
