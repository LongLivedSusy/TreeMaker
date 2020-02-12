#!/bin/env python
from  __builtin__ import any as b_any
import os, glob
from optparse import OptionParser
import socket
import commands

# to be run at DESY

def create_processed_filelist():
    os.system("ls /pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v3/ > finished_ntuples.dat")


def file_has_been_processed(campaign, processed_uuids, aod_file, debug = False):
        
    aodfile_uuid = aod_file.split("/")[-2] + "-" + aod_file.split("/")[-1].replace(".root", "")        

    if aodfile_uuid in processed_uuids:
        return True
    else:
        return False


def main(campaign, processed_files, debug = False, comment_already_processed_files = True):

    # read processed files
    processed_files_string = ""
    with open(processed_files, "r") as fin:
        processed_files_string = fin.read()
    processed_files = list(set(processed_files_string.split("\n")))

    for i in range(len(processed_files)):
        if len(processed_files[i].split("_"))>1:
            processed_files[i] = processed_files[i].split("_")[-2]

    processed_uuids = processed_files

    print "%s/*AOD_cff.py" % campaign

    aod_filelists = sorted(glob.glob("%s/*AOD_cff.py" % campaign))
    
    for i_aod_file, aod_file in enumerate(aod_filelists):

        #FIXME
        if "DYJetsToLL_M-5to50_HT" in aod_file: continue
       
        print "Checking %s/%s (%s)..." % (i_aod_file, len(aod_filelists), aod_file)

        file_contents = ""
        with open(aod_file, "r") as fin:
            file_contents = fin.read() 

        # check if file is in processed_files        
        file_contents = file_contents.split("\n")
        file_count = 0
        for i in range(len(file_contents)):
            ignore_file = False
            if ".root" in file_contents[i]:

                # remove old hashes...
                if "#" in file_contents[i]:
                    file_contents[i] = file_contents[i].replace("#", "")
                
                if comment_already_processed_files:
                    filename = file_contents[i].split("'")[1]
                    if file_has_been_processed(campaign.split("/")[-1], processed_uuids, filename):
                        file_contents[i] = "#" + file_contents[i]
                    else:
                        file_contents[i] = file_contents[i]
                    file_count += 1

        with open(aod_file, "w") as fout:
            fout.write("\n".join(file_contents))
        
        print "%s written!" % aod_file
        

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--update_filelist", dest="update_filelist", action="store_true")
    parser.add_option("--campaign", dest="campaign", default="all")
    parser.add_option("--processed_files", dest="processed_files", default="finished_ntuples.dat")
    parser.add_option("--debug", dest="debug", action="store_true")
    (options, args) = parser.parse_args()

    if options.update_filelist or not os.path.exists(os.getcwd() + "/" + options.processed_files):
        create_processed_filelist()

    if options.campaign and options.processed_files:
        if options.campaign == "all":
            campaigns = glob.glob("../python/Run201*") + ["../python/RunIIFall17MiniAODv2"] + ["../python/Summer16"] + ["../python/RunIISummer16MiniAODv3"]
            print "Using campaigns:", campaigns
        else:
            campaigns = options.campaign.split(",")

        for campaign in campaigns:
            main("../python/" + campaign, options.processed_files, debug = options.debug)

    else:
        print "Run with e.g.\n ./check_already_processed_files.py --campaign RunIIFall17MiniAODv2 --processed_files finished_ntuples.dat \n"
        print "Can also run with multiple campaigns separated by commas."
