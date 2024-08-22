#!/bin/env python
import os, sys
import glob
import commands

print_stats = 1
more = 0

for path in [
             "~/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/test/condorSub",
             "~/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/test/condorSub",
            ]:

    print path

    if print_stats:

        status, output = commands.getstatusoutput("ls %s/ |grep .condor |wc -l" % path)
        print "jobfiles\t", output

        status, output = commands.getstatusoutput("ls %s/ |grep stdout |wc -l" % path)
        print "Logfiles\t", output

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep Doing {} + |wc -l" % path)
        print "Doing files:\t", output

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'XrdAdaptor::RequestManager::requestFailure' {} + |wc -l" % path)
        print "XrdAdaptor::RequestManager::requestFailure\t", output

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'Failed to open the file' {} + |wc -l" % path)
        print "Failed to open the file\t", output

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'The secondary file is not an ancestor of the primary file' {} + |wc -l" % path)
        print "Ancestor problem!\t", output

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'miniAOD error' {} + |wc -l" % path)
        print "miniAOD error\t", output

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'Assertion' {} + |wc -l" % path)
        print "Assertion\t", output

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'Copying' {} + |wc -l" % path)
        print "Copying\t", output

    if more:

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'Failed to open the file' {} + | grep '/AOD/'" % path)
        output_lines = output.split("\n")

        status, output = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'Could not open file' {} + | grep -v 'Failed to open the file' | grep '/AOD/'" % path)
        output_lines += output.split("\n")

        datasets_with_fileopenerrors = {}

        for output_line in output_lines:

            try:
                dataset = output_line.split("test/condorSub/")[1].split("AOD")[0]
                if not dataset in datasets_with_fileopenerrors:
                    datasets_with_fileopenerrors[dataset] = 1
                else:
                    datasets_with_fileopenerrors[dataset] += 1

            except:
                continue


        for dataset in sorted(datasets_with_fileopenerrors.keys()):

            # look if files from this dataset have been copied? e.g.:
            # Copying 79639126 bytes file:///srv/RunIIAutumn18FS.PMSSM_set_1_LL_TuneCP2_13TeV-pythia8-AOD2_30000-D37763C4-529E-744D-ACAD-E8A9554ED02A_RA2AnalysisTree.root => srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/ProductionRun2v3//RunIIAutumn18FS.PMSSM_set_1_LL_TuneCP2_13TeV-pythia8-AOD2_30000-D37763C4-529E-744D-ACAD-E8A9554ED02A_RA2AnalysisTree.root

            status, n_copied = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep 'Copying' {} + |grep %s |wc -l " % (path, dataset))
            status, n_total = commands.getstatusoutput("find %s/ -type f -name '*.stdout' -exec grep Doing {} + |grep %s |wc -l " % (path, dataset))
            
            print("  ||o||  %s: n_total=%s \t n_error=%s \t n_copied=%s" % (dataset, n_total, datasets_with_fileopenerrors[dataset], n_copied))
