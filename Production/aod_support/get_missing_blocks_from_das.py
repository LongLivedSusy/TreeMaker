#!/bin/env python
from dbs.apis.dbsClient import DbsApi
from optparse import OptionParser
import commands
import time
import os

# Run before:
# voms-proxy-init -voms cms:/cms -valid 192:00
# source /cvmfs/cms.cern.ch/crab3/crab.sh

def get_all_blocks(check_sites_immediately = True):

    dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')

    status, output = commands.getstatusoutput("grep '.root' ../python/Run201*/*AOD*py | grep -v '#'")
    pending_aods = output.split("\n")

    aodblocks = {}
    blocks = []

    print "pending_aods:", len(pending_aods)

    for i, pending_aod in enumerate(pending_aods):   

        pending_aod = pending_aod.split(":")[1].split(",")[0]

        cffname = pending_aod.split("'")[0]    
        filename = pending_aod.split("'")[1]

        status, output = commands.getstatusoutput("grep '%s' missing_blocks_with_aods" % pending_aod)
        if status == 0:
            block = output.split(",: ")[-1]
        else:
            print "querying", pending_aod
            output = dbs.listBlocks(logical_file_name = filename )
            block = output[0]['block_name']
            os.system("echo '%s,: %s' >> missing_blocks_with_aods" % (pending_aod, block))

        blocks.append(block)
        aodblocks[pending_aod] = block

        #status, output = commands.getstatusoutput("grep '%s' missing_blocks_nonavailable.*.rucio" % block)
        #if status == 0:
        #    print "Should be there:", pending_aod

        if True:            
            desypath = "/pnfs/desy.de/cms/tier2" + pending_aod.replace("'", "")
            if os.path.exists(desypath):
                #print "There:", pending_aod
                targetpath = "/afs/desy.de/user/k/kutznerv/dust/%s/" % '/'.join(desypath.replace('/pnfs/desy.de/cms/tier2/store/', 'store/').split('/')[:-1])
                cmd = "mkdir -p %s && cp %s %s" % (targetpath, desypath, targetpath)
                os.system("echo '%s' >> copy_to_dust" % cmd)

    if False:
        with open("missing_blocks_with_aods", "w") as outfile:
            for aod in aodblocks:
                outfile.write(aod + ': ' + aodblocks[aod] + '\n')

    if True:
        unique_blocks = list(set(blocks))
        #print "blocks", blocks
        #print "unique_blocks", unique_blocks
        print len(blocks), len(unique_blocks)

        with open("missing_blocks_perfile.oct20", "w") as outfile:
            for unique_block in unique_blocks:
                outfile.write(unique_block + '\n')


def get_block_sites():

    with open("missing_blocks_perfile.oct20", "r") as infile:
        blocks = infile.read()
        blocks = blocks.split('\n')

        for i_block, block in enumerate(blocks):

            if block == "": continue

            if i_block%20 == 0:
                print i_block

            status, output = commands.getstatusoutput('grep %s missing_blocks_sites_wholelist.oct20' % block)
            if status == 0:
                continue


            print block

            status, output = commands.getstatusoutput('dasgoclient --query="site block=%s"' % block)
            if status != 0:
                print "Something wrong"
                print output
                quit()

            sites = output.split("\n")
            outstring = block + ": " + ",".join(sites)
            os.system("echo %s >> missing_blocks_sites_wholelist.oct20" % outstring)

            #if i_block>0 and i_block%15==0:
            #    print "Sleeping"
            #    time.sleep(60)
    

def check_block_availability():

    blocks_sites_nonavailable = []

    with open("missing_blocks_sites_wholelist.oct20", "r") as infile:
        blocks = infile.read().split("\n")
        for line in blocks:

            if line == "": continue
            block = line.split(":")[0]
            sites = line.split(":")[1].split(",")

            #status, output = commands.getstatusoutput("grep '%s' missing_blocks_perfile.june1" % block)
            #if status != 0:
            #    continue

            block_only_on_tape = True
            for site in sites:
                if "Tape" not in site and "T2_BR_SPRACE" not in site:
                    block_only_on_tape = False
                    break

            block_only_at_desy = True
            for site in sites:
                if "Tape" not in site and "DESY" not in site and "Testing" not in site and "testing" not in site and "T2_BR_SPRACE" not in site:
                    print "block elsewhere:", block
                    block_only_on_tape = False
                    break

            if block_only_on_tape and block_only_at_desy:
                blocks_sites_nonavailable.append(block)
                print block

    with open("missing_blocks_nonavailable.june1", "w") as outfile:
        outfile.write("\n".join(blocks_sites_nonavailable))

    with open("missing_blocks_nonavailable.june1.rucio", "w") as outfile:
        for block in blocks_sites_nonavailable:
            outfile.write("rucio add-rule --ask-approval --lifetime 691200 cms:%s 1 T2_DE_DESY\n" % block)



def free_copied_blocks():

    print "Checking for unused blocks"

    with open("missing_blocks_nonavailable", "r") as infile:
        blocks = infile.read().split("\n")
        for line in blocks:

            line = line.replace("rucio add-rule --ask-approval --lifetime 900000 ", "")
            line = line.replace(" 1 T2_DE_DESY", "")
            block = line
            status, output = commands.getstatusoutput("grep '%s' missing_blocks_perfile" % block)
            if status != 0:
                print "FREE: %s" % block


get_all_blocks()
#get_block_sites()  
#check_block_availability()
#free_copied_blocks()

