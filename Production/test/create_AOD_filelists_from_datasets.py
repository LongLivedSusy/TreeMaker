#!/bin/env python
import os
import glob
import commands

# create AOD file lists from exisiting miniAOD file lists. Configuration:

check_dataset_availablity = True

cff_folder = "RunIIAutumn18MiniAOD"

miniaod_datastreams = [
    "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT1000to1500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT100to200_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT1500to2000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT2000toInf_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT200to300_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT300to500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT500to700_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/QCD_HT700to1000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_s-channel_4f_leptonDecays_mtop1695_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_s-channel_4f_leptonDecays_mtop1715_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_s-channel_4f_leptonDecays_mtop1735_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_s-channel_4f_leptonDecays_mtop1755_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_antitop_5f_TuneCP5_13TeV-powheg-madspin-pythia8_vtd_vts_decay/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_antitop_5f_TuneCP5_13TeV-powheg-madspin-pythia8_vtd_vts_prod/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_antitop_5f_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_eleDecays_13TeV-comphep-pythia8_TuneCP5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_muDecays_13TeV-comphep-pythia8_TuneCP5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_tauDecays_13TeV-comphep-pythia8_TuneCP5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-madspin-pythia8_vtd_vts_prod/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_t-channel_top_5f_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8_vtd_vts_decay/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_antitop_5f_inclusiveDecays_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_antitop_5f_inclusiveDecays_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_antitop_5f_inclusiveDecays_mtop1695_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_antitop_5f_inclusiveDecays_mtop1735_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_antitop_5f_inclusiveDecays_mtop1755_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_top_5f_inclusiveDecays_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_top_5f_inclusiveDecays_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_top_5f_inclusiveDecays_mtop1695_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_top_5f_inclusiveDecays_mtop1715_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_top_5f_inclusiveDecays_mtop1735_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    #"/ST_tW_top_5f_inclusiveDecays_mtop1755_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_SingleLeptFromT_genMET-80_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_SingleLeptFromTbar_genMET-80_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    "/WW_TuneCP5_PSweights_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
]

for dataset in miniaod_datastreams:

    print "Querying:", 'dasgoclient --query="parent dataset=%s"' % dataset
    status, parent_dataset = commands.getstatusoutput('dasgoclient -query="parent dataset=%s"' % dataset)
    print "Querying:", 'dasgoclient --query="child dataset=%s"' % parent_dataset
    status, child_datasets = commands.getstatusoutput('dasgoclient -query="child dataset=%s"' % parent_dataset)

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
        
        # promptreco_rereco_identifier is something like 17Sep2018, PromptReco etc:
        if "Run201" in dataset:
            promptreco_rereco_identifier = dataset.split("/")[2]
        elif "MiniAOD" in dataset:
            promptreco_rereco_identifier = dataset.split("/")[2]
        
        complete_output = get_aod_dataset(child_datasets, promptreco_rereco_identifier)

    # get only unique entries in list:
    complete_output = list(set(complete_output))
    print "selected AOD dataset:", complete_output

    # optional: check site availability, give warning if not available:
    if check_dataset_availablity:
        sample_available = False 
        for item in complete_output:
            #print item
            status, sites = commands.getstatusoutput('dasgoclient -query="site dataset=%s"' % item)
            for line in sites.split("\n"):
                if "MSS" not in line and "Buffer" not in line and "T0_CH_CERN_Export" not in line:
                    #print "\t", line
                    sample_available = True
        
            if not sample_available:
                print "### warning, sample not readily available on any site: %s" % item
                os.system('echo "%s" >> samples_not_available' % item)
                #continue
            
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

    os.system("mkdir -p %s" % cff_folder)

    # don't submit more than 78 chunks at once (close to the limit of 20k jobs for CMS Connect):
    chunks_per_submission_file = list(dochunks(chunks, 20))
    for ichunk, filechunks in enumerate(chunks_per_submission_file):

        identifier = dataset.split("/")[1]

        if len(chunks_per_submission_file) == 1:
            pyfilename = cff_folder + "/" + identifier + "-AOD_cff.py"
        else:
            pyfilename = cff_folder + "/" + identifier + "-AOD%s_cff.py" % ichunk

        with open(pyfilename, "w+") as fout:
            header = """import FWCore.ParameterSet.Config as cms

maxEvens = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFils = cms.untracked.vstring()
secFile = cms.untracked.vstring()
source  cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
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



