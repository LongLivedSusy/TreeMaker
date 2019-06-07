#!/bin/env python
import os, glob
from optparse import OptionParser
import socket
import commands

# to be run at DESY

def create_processed_filelist():
    os.system("ls /pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v*/ > finished_ntuples.dat")


def file_has_been_processed(campaign, aod_file, file_count, processed_files, filename, debug = False):

    output_file_name = "%s.%s_%s_RA2AnalysisTree.root" % (campaign, aod_file.replace("_cff.py", ""), file_count)
   
    if output_file_name in processed_files:
        return True
    else:
        return False


def main(campaign, processed_files, debug = False):

    # read processed files
    processed_files_string = ""
    with open(processed_files, "r") as fin:
        processed_files_string = fin.read()
    processed_files = set(processed_files_string.split("\n"))

    print "%s/*AOD_cff.py" % campaign

    aod_filelists = sorted(glob.glob("%s/*AOD_cff.py" % campaign))
    
    for i_aod_file, aod_file in enumerate(aod_filelists):
       
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

                filename = file_contents[i].split("'")[1]
                if file_has_been_processed(campaign.split("/")[-1], aod_file.split("/")[-1], file_count, processed_files, filename, debug = debug):
                    file_contents[i] = "#" + file_contents[i]
                else:
                    file_contents[i] = file_contents[i]

                file_count += 1


        with open(aod_file, "w") as fout:
            fout.write("\n".join(file_contents) + "\n")
        
        print "%s written!" % aod_file
        

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--create_processed_filelist", dest="create_processed_filelist", action="store_true")
    parser.add_option("--campaign", dest="campaign", default="all")
    parser.add_option("--processed_files", dest="processed_files", default="finished_ntuples.dat")
    parser.add_option("--debug", dest="debug", action="store_true")
    (options, args) = parser.parse_args()

    if options.create_processed_filelist:
        create_processed_filelist()
    elif options.campaign and options.processed_files:

        if "naf-" in socket.gethostname():
            print "Running on NAF, we can update the already processed file list. Just wait a sec..."
            create_processed_filelist()
            print "OK"

        if options.campaign == "all":
            campaigns = glob.glob("../python/Run201*") + ["../python/RunIIFall17MiniAODv2"] + ["../python/Summer16"]
            print "Using campaigns:", campaigns
        else:
            campaigns = options.campaign.split(",")

        for campaign in campaigns:
            main("../python/" + campaign, options.processed_files, debug = options.debug)

    else:
        print "Run with e.g.\n ./check_already_processed_files.py --campaign RunIIFall17MiniAODv2 --processed_files finished_ntuples.dat \n"
        print "Can also run with multiple campaigns separated by commas."
