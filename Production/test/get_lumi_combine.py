#!/bin/env python
import glob
import os
import commands
from natsort import natsorted, ns
import sys

get_json(years = ["2016"], datastreams = ["MET", "SingleElectron", "SingleMuon"]):

    json_cleaning = True

    for year in years:
        for datastream in datastreams:
        
            print "Doing datastream Run%s_%s" % (year, datastream)
        
            combined_json = {}
            filelist = sorted(glob.glob("output_lumi/*Run%s*%s*json" % (year, datastream)))
            
            for i_ifile, ifile in enumerate(filelist):	
                if i_ifile % 100 == 0:
                     sys.stderr.write("%s/%s\n" % (i_ifile, len(filelist)))
                idict = ""
                with open(ifile, "r") as fin:
                    idict = fin.read()
                idict = eval(idict) 
                for run in idict:
                    if run not in combined_json:
                        combined_json[run] = []
                    combined_json[run] += idict[run]
                    combined_json[run] = natsorted(combined_json[run])
            
                    if json_cleaning:
                        #test for overlap:
                        indices_to_be_deleted = []
                        if len(combined_json[run])>1:
                            for i in range(1, len(combined_json[run])):
                                
                                if combined_json[run][i-1][1] >= combined_json[run][i][1]:
                                    #print "overlap", combined_json[run][i-1], combined_json[run][i]
                                    #print "removing", combined_json[run][i]
                                    indices_to_be_deleted.append(i)
                                elif combined_json[run][i-1][1] >= combined_json[run][i][0]:
                                    #print "overlap", combined_json[run][i-1], combined_json[run][i]
                                    combined_json[run][i-1][1] = combined_json[run][i][1]
                                    indices_to_be_deleted.append(i)
                                    #print "removing", combined_json[run][i], "keeping", combined_json[run][i-1]
                        
                        cleaned_list = []
                        for i in range(len(combined_json[run])):
                            if i not in indices_to_be_deleted:
                                cleaned_list.append(combined_json[run][i])
              
                        combined_json[run] = cleaned_list
            
            #if json_cleaning:
            #    # compact lumisections:
            #    combined_json_compacted = []
            #    for i in range(len(combined_json[run])):
            #        if len(combined_json_compacted) == 0:
            #            combined_json_compacted.append()
            
            combined_json_text = str(combined_json).replace("'", '"')
            filename = "Run%s_%s.json" % (year, datastream)
        
            with open(filename, "w") as fout:
                fout.write(combined_json_text)
        
                print "%s written" % filename
      
    