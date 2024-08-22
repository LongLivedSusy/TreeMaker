#!/bin/env python
import os
import glob
import commands

aod_scenarios = {
                 #"Summer16": ["Summer16", "Summer16"],
                 #"Fall17":   ["Fall17", "Fall17"],
                 #"Autumn18":  ["Autumn18", "Autumn18"],
                 #"Run2016A":  ["re2016A", "2016MiniAODv3AOD"],
                 #"Run2016B":  ["re2016B", "2016MiniAODv3AOD"],
                 #"Run2016C":  ["re2016C", "2016MiniAODv3AOD"],
                 #"Run2016D":  ["re2016D", "2016MiniAODv3AOD"],
                 #"Run2016E":  ["re2016E", "2016MiniAODv3AOD"],
                 #"Run2016F":  ["re2016F", "2016MiniAODv3AOD"],
                 #"Run2016G":  ["re2016G", "2016MiniAODv3AOD"],
                 #"Run2016H":  ["re2016H", "2016MiniAODv3AOD"],
                 #"Run2017B":  ["re2017B", "2017ReReco31MarAOD"],
                 #"Run2017C":  ["re2017C", "2017ReReco31MarAOD"],
                 #"Run2017D":  ["re2017D", "2017ReReco31MarAOD"],
                 #"Run2017E":  ["re2017E", "2017ReReco31MarAOD"],
                 #"Run2017F":  ["re2017F", "2017ReReco31MarAOD"],
                 #"Run2018A": ["re2018A", "2018ReReco17SepAOD"],
                 #"Run2018B": ["re2018B", "2018ReReco17SepAOD"],
                 #"Run2018C": ["re2018C", "2018ReReco17SepAOD"],                
                 #"Run2018D": ["2018D", "2018PromptRecoAOD"],
                 #"Run2018D": ["2018D", "2018PromptRecoAOD"],
                 "Summer16": ["RunIISummer16MiniAODv3Fast", "RunIIFall17"]
                } 


for campaign in [
                 #"Summer16",
                 #"RunIIFall17MiniAODv2",
                 "RunIISummer16MiniAODv3Fast",
                 #"RunIIAutumn18MiniAOD",
                 #"Run2016B-17Jul2018_ver*",
                 #"Run2016C-17Jul2018-v1",
                 #"Run2016D-17Jul2018-v1",
                 #"Run2016E-17Jul2018-v1",
                 #"Run2016F-17Jul2018-v1",
                 #"Run2016G-17Jul2018-v1",
                 #"Run2016H-17Jul2018-v*",
                 #"Run2017B-31Mar2018-v1",
                 #"Run2017C-31Mar2018-v1",
                 #"Run2017D-31Mar2018-v1",
                 #"Run2017E-31Mar2018-v1",
                 #"Run2017F-31Mar2018-v1",
                 #"Run2018A-17Sep2018-v1",
                 #"Run2018B-17Sep2018-v1",
                 #"Run2018C-17Sep2018-v1",
                 #"Run2018D-PromptReco*",
                ]:

    flist = {}
    flist["samples"] = []
   
    folders = glob.glob("../python/%s" % campaign)

    pyfilename = ""

    for folder in folders:

        for aod_scenario in aod_scenarios:
            if aod_scenario in folder:
                pyfilename = aod_scenarios[aod_scenario][0]
                flist["scenario"] = aod_scenarios[aod_scenario][1]
                break

        label = folder.split("/")[-1]

        datastreams = []
        if "Run201" in label:
            datastreams = ["MET", "SingleElectron", "SingleMuon", "JetHT"]
        else:
            streams = glob.glob("%s/*AOD*_cff.py" % folder)
            for stream in streams:
                datastreams.append( stream.split("/")[-1].replace("_cff.py", "") )

        #print "datastreams", datastreams

        for datastream in datastreams:
            filelists = glob.glob("%s/%s_cff.py" % (folder, datastream))
            for filelist in sorted(filelists):

                # check for Fall17 pileup conditions:
                use_Fall17nowrongPU = False
                if campaign == "RunIIFall17MiniAODv2":
                    status, output = commands.getstatusoutput('grep -L "/PU2017" %s' % filelist)
                    if ".py" in output:
                        use_Fall17nowrongPU = True

                if "SMS" in filelist and "LLChipm" not in filelist: continue
                if "Stealth" in filelist: continue
                if "RPV" in filelist: continue
                if not use_Fall17nowrongPU: continue
                #if use_Fall17nowrongPU: continue

                flist["samples"].append( label + "." + filelist.split("/")[-1].replace("_cff.py", "") )
 
    flist["samples"] = list(set(flist["samples"]))
    for i in range(len(flist["samples"])):
        flist["samples"][i] = [ flist["samples"][i] ]

    flist["samples"] = sorted(flist["samples"])

    contents = "flist = %s" % str(flist).replace(" ", "\n").replace("[[", "[\n[").replace("]]", "]\n]")

    print contents  

    pyfilename = "../test/condorSub/dict_%s-AOD.py" % pyfilename.replace("Run", "")

    with open(pyfilename, "w+") as fout:

        fout.write(contents)                  
        print pyfilename, "written!"
        print "++++++++++++++++++++++++++++++++++++++++++++++++"
