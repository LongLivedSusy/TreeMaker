#!/bin/env python
import os, glob
from GridEngineTools import runParallel

commands = []

for datastream in ["MET", "SingleElectron", "SingleMuon", "JetHT"]:
    for period in ["2016B", "2016C", "2016D", "2016E", "2016F", "2016G", "2016H"]:

        if datastream == "JetHT":
            commands.append("./get_lumi.py /pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v2/Run%s*%s* %s_%s.json" % (period, datastream, period, datastream))
        else:
            commands.append("./get_lumi.py /pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/Production2016v2/Run%s*%s* %s_%s.json" % (period, datastream, period, datastream))

print commands

runParallel(commands, "grid", dontCheckOnJobs=True)

