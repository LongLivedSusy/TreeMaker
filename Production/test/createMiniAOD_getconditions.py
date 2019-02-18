#!/bin/env python
import os
import glob
import commands

for datastream in ["MET", "SingleElectron", "SingleMuon", "JetHT"]:
    input_files = glob.glob("../python/Run2018*/%s_cff.py" % datastream)

    for ifile in sorted(input_files):

        print ifile

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

        def get_aod_dataset(child_datasets, production):
            output = []
            for item in child_datasets.split("\n"):
                if "/AOD" in item and production in item:                  
                    if not "pilot" in item:
                        output.append(item)
            return output

        # promptreco_rereco_identifier is something like 17Sep2018, PromptReco etc:
        if "Run201" in cff_folder:
            promptreco_rereco_identifier = cff_folder.split("-")[1] + "-" + cff_folder.split("-")[2]
        elif "MiniAOD" in cff_folder:
            promptreco_rereco_identifier = cff_folder.split("MiniAOD")[0]
        else:
            promptreco_rereco_identifier = cff_folder

        print "promptreco_rereco_identifier", promptreco_rereco_identifier

        complete_output = get_aod_dataset(child_datasets, promptreco_rereco_identifier)
        complete_output = list(set(complete_output))

        print "complete_output", complete_output

        # seems to be a problem with the automatic DAS query for this one...:
        if len(complete_output) == 0 and "Run2018B" in aod_file_name and "MET" in aod_file_name:
            complete_output = ["/MET/Run2018B-PromptReco-v1/AOD", "/MET/Run2018B-PromptReco-v2/AOD"]
        
        # check site availability:
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
                
        # create python configuration if sample is available:
        all_filenames = ""
        for item in complete_output:
            status, filenames = commands.getstatusoutput('dasgoclient -query="file dataset=%s"' % item)
            if len(filenames) == 0:
                raw_input("### file list empty, this should not happen: %s" % item)
            all_filenames += "\n" + filenames
        
        # Create a function called "chunks" with two arguments, l and n:
        def chunks(l, n):
            # For item i in a range that is a length of l,
            for i in range(0, len(l), n):
                # Create an index range for l of n items:
                yield l[i:i+n]
        
        chunks = list(chunks(all_filenames.split("\n"), 254))

        pyfilename = cff_folder + "/" + cff_filename.split("_")[0] + "AOD_cff.py"

        with open(pyfilename, "w+") as fout:
            header = """import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
"""
   
            fout.write(header)
   
            for chunk in chunks:
                fout.write("readFiles.extend( [\n")
                for ifile in chunk:
                    if ifile != "":
                        fout.write("'%s',\n" % ifile)
                fout.write("] )\n")
                
        print pyfilename, "written!"
        print "++++++++++++++++++++++++++++++++++++++++++++++++"
        