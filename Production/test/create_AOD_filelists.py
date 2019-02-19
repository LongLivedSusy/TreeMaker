#!/bin/env python
import os
import glob
import commands

# create AOD file lists from exisiting miniAOD file lists. Configuration:

check_dataset_availablity = False
datastreams = ["MET", "SingleElectron", "SingleMuon", "JetHT"]

#campaign = "Run2018*"
#campaign = "Run2016*"
#campaign = "Run2017*"
campaign = "Run201*"

# Some particular issues regarding DAS entries for Run2018 datasets (state from Feb 19 2019):
#
# (1) For Run2018A-17Sep2018-v1.SingleMuon, cannot find files => correct parent is /SingleMuon/Run2018A-17Sep2018-v2/AOD ("v2" instead of "v1")
#       --> solved, marked below
# (2) For Run2018B-17Sep2018-v1.MET, DAS cannot find the AOD re-reco files (only prompt reco). Use prompt reco here
#       --> solved, marked below

for datastream in datastreams:

    input_files = glob.glob("../python/%s/%s_cff.py" % (campaign, datastream))

    for ifile in sorted(input_files):

        # ignore already prepared folders:
        if "-AOD" in ifile: continue

        print "ifile", ifile

        cff_filename = ifile.split("/")[-1]
        cff_folder = "/".join( ifile.split("/")[:-1] )

        contents = ""
        aod_file_name = ""
        with open(ifile, "r") as fin:
            contents = fin.read()
        for line in contents.split("\n"):
            if "/store/" in line:
                aod_file_name = line.split("'")[1]
                break

        status, dataset = commands.getstatusoutput('dasgoclient -query="dataset file=%s"' % aod_file_name)
        status, parent_dataset = commands.getstatusoutput('dasgoclient -query="parent dataset=%s"' % dataset)
        status, child_datasets = commands.getstatusoutput('dasgoclient -query="child dataset=%s"' % parent_dataset)

        # promptreco_rereco_identifier is something like 17Sep2018, PromptReco etc:
        if "Run201" in cff_folder:
            promptreco_rereco_identifier = cff_folder.split("-")[1] + "-" + cff_folder.split("-")[2]
        elif "MiniAOD" in cff_folder:
            promptreco_rereco_identifier = cff_folder.split("MiniAOD")[0]
        else:
            promptreco_rereco_identifier = cff_folder

        #print "parents:", parent_dataset.replace("\n", ",")
        #print "childs:", child_datasets.replace("\n", ",")
        #print "select by:", promptreco_rereco_identifier

        def get_aod_dataset(child_datasets, production):
            output = []
            for item in child_datasets.split("\n"):
                if "/AOD" in item and production in item:                  
                    if not "pilot" in item:
                        output.append(item)
            return output

        # sometimes, the AOD is the parent of the miniAOD file (as in 2016):
        if "/AOD" in parent_dataset:
            complete_output = [parent_dataset]
        else:
            complete_output = get_aod_dataset(child_datasets, promptreco_rereco_identifier)

        # solve issue (1):
        if len(complete_output) == 0:
            complete_output = get_aod_dataset(child_datasets, promptreco_rereco_identifier.replace("v1", "v2"))
        # end of issue

        # solve issue (2):
        if len(complete_output) == 0 and "Run2018B" in aod_file_name and "MET" in aod_file_name:
            complete_output = ["/MET/Run2018B-PromptReco-v1/AOD", "/MET/Run2018B-PromptReco-v2/AOD"]
            cff_folder = "../python/Run2018B-PromptReco-v1v2"
        # end of issue

        # get only unique entries in list:
        complete_output = list(set(complete_output))
        print "selected AOD dataset:", complete_output

        # optional: check site availability, give warning if not available:
        if check_dataset_availablity:
            for item in complete_output:
                print item
                sample_available = False 
                status, sites = commands.getstatusoutput('dasgoclient -query="site dataset=%s"' % item)
                for line in sites.split("\n"):
                    if "MSS" not in line and "Buffer" not in line:
                        print "\t", line
                        sample_available = True
            
                if not sample_available:
                    print "### warning, sample not readily available on any site: %s" % item
                
        # create python configuration:
        all_filenames = ""
        for item in complete_output:
            status, filenames = commands.getstatusoutput('dasgoclient -query="file dataset=%s"' % item)
            if len(filenames) == 0:
                raw_input("### file list empty, this should not happen: %s" % item)
            all_filenames += "\n" + filenames
        
        # Create a function called "chunks" with two arguments, l and n:
        def dochunks(l, n):
            # For item i in a range that is a length of l,
            for i in range(0, len(l), n):
                # Create an index range for l of n items:
                yield l[i:i+n]
        
        chunks = list(dochunks(all_filenames.split("\n"), 254))

        cff_folder = cff_folder + "-AOD"
        os.system("mkdir -p %s" % cff_folder)
        os.system("echo placeholder >> %s/__init__.py" % cff_folder)

        # don't submit more than 78 chunks at once (close to 20k jobs which is the limit):
        chunks_per_submission_file = list(dochunks(chunks, 78))
        for ichunk, filechunks in enumerate(chunks_per_submission_file):

            if len(chunks_per_submission_file) == 1:
                pyfilename = cff_folder + "/" + cff_filename.split("_")[0] + "_cff.py"
            else:
                pyfilename = cff_folder + "/" + cff_filename.split("_")[0] + "%s_cff.py" % ichunk

            with open(pyfilename, "w+") as fout:
                header = """import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
"""
       
                fout.write(header)
       
                for chunk in filechunks:
                    fout.write("readFiles.extend( [\n")
                    for ifile in chunk:
                        if ifile != "":
                            fout.write("'%s',\n" % ifile)
                    fout.write("] )\n")
                    
            print pyfilename, "written!"
        print "++++++++++++++++++++++++++++++++++++++++++++++++"
        
