#!/bin/env python
from optparse import OptionParser
import commands
import time
import os

def get_all_blocks():

    print "get all blocks"

    # Run before:
    # voms-proxy-init -voms cms:/cms -valid 192:00
    # source /cvmfs/cms.cern.ch/crab3/crab.sh

    from dbs.apis.dbsClient import DbsApi    
    dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')

    status, output = commands.getstatusoutput("grep '.root' ../python/Run201*/*AOD*py | grep -v '#'")
    pending_aods = output.split("\n")

    #pending_aods = []
    #status, output = commands.getstatusoutput("grep '.root' ../python/RunIIFall17FS/PMSSM_set_2_LL_1_*AOD*py | grep -v '#'")
    #pending_aods += output.split("\n")
    #status, output = commands.getstatusoutput("grep '.root' ../python/RunIIFall17FS/PMSSM_set_2_LL_2_*AOD*py | grep -v '#'")
    #pending_aods += output.split("\n")

    # load custom filelist:
    #pending_aods = []
    #with open("missing_files_dbs_check_all_uniq.dat", "r") as fin:
    #    pending_aods = fin.read().split("\n")[:-1]

    aodblocks = {}
    blocks = []

    print "pending_aods:", len(pending_aods)

    for i, pending_aod in enumerate(pending_aods):   

        if ":" in pending_aod:
            pending_aod = pending_aod.split(":")[1].split(",")[0]
            cffname = pending_aod.split("'")[0]    
            filename = pending_aod.split("'")[1]
        else:
            filename = pending_aod

        filename = filename.replace(" ", "")
        pending_aod = pending_aod.replace(",", "")
        pending_aod = pending_aod.replace(" ", "")

        status, output = commands.getstatusoutput("grep %s missing_blocks_with_aods" % pending_aod)
        if status == 0:
            #print "ok", i
            block = output.split(",: ")[-1]            
        else:
            print "querying", pending_aod
            output = dbs.listBlocks(logical_file_name = filename )
            block = output[0]['block_name']
            #os.system("echo '%s,: %s' >> missing_blocks_with_aods" % (pending_aod, block))
            os.system("echo '%s: %s' >> missing_blocks_with_aods" % (pending_aod, block))


        # check if requested within rucio...:
        status, output = commands.getstatusoutput("grep '%s' rucio-rules.feb24" % block.split()[-1])
        if status == 0:
            print "Requested: %s" % pending_aod
            print output
            print "******"


        # clear whitespace
        block = block.lstrip()
        block = block.replace("       ", "")
        
        #FIX
        if " " in block:
            block = block.split()[1]

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

        with open("missing_blocks_perfile.feb24", "w") as outfile:
            for unique_block in unique_blocks:
                outfile.write(unique_block + '\n')


def get_block_sites():

    print "getting sites..."

    with open("missing_blocks_perfile.feb24", "r") as infile:
        blocks = infile.read()
        blocks = blocks.split('\n')

        for i_block, block in enumerate(blocks):

            if block == "": continue
            if "/" not in block: continue

            if i_block%20 == 0:
                print i_block

            if " " in block:
                block = block.split()[1]
            print block

            status, output = commands.getstatusoutput('grep %s missing_blocks_sites_wholelist.feb24' % block)
            if status == 0:
                continue

            status, output = commands.getstatusoutput('dasgoclient --query="site block=%s"' % block)
            if status != 0:
                print "Something wrong"
                print output
                quit()

            sites = output.split("\n")
            outstring = block + ": " + ",".join(sites)
            os.system("echo %s >> missing_blocks_sites_wholelist.feb24" % outstring)

            #if i_block>0 and i_block%15==0:
            #    print "Sleeping"
            #    time.sleep(60)
    

def check_block_availability():

    blocks_sites_nonavailable = []

    with open("missing_blocks_sites_wholelist.feb24", "r") as infile:
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
                if "Tape" not in site and "T2_BR_SPRACE" not in site and "DBS" not in site and "WARNING" not in site and "Rucio" not in site:
                    block_only_on_tape = False
                    break

            #block_only_at_desy = True
            #for site in sites:
            #    if "Tape" not in site and "DESY" not in site and "Testing" not in site and "testing" not in site and "T2_BR_SPRACE" not in site and "DBS" not in site and "WARNING" not in site and "Rucio" not in site:
            #        print "block elsewhere:", block
            #        block_only_on_tape = False
            #        break

            ignore = False
            block_at_desy = False
            for site in sites:
                if "WARNING" in site or "DBS" in site:
                    block_only_on_tape = True
                    ignore = True
                if "DESY" in site:
                    block_at_desy = True

            if ignore:
                continue

            #if block_only_on_tape and block_only_at_desy:
            if block_only_on_tape:
                blocks_sites_nonavailable.append(block)
                print block

    with open("missing_blocks_nonavailable.feb24", "w") as outfile:
        outfile.write("\n".join(blocks_sites_nonavailable))

    with open("missing_blocks_nonavailable.feb24.rucio", "w") as outfile:
        for block in blocks_sites_nonavailable:
            outfile.write("rucio add-rule --ask-approval --lifetime 1209600 cms:%s 1 T2_DE_DESY\n" % block)



def free_copied_blocks():

    print "Checking for unused blocks"

    with open("missing_blocks_nonavailable.feb24", "r") as infile:
        blocks = infile.read().split("\n")
        for line in blocks:

            line = line.replace("rucio add-rule --ask-approval --lifetime 900000 ", "")
            line = line.replace(" 1 T2_DE_DESY", "")
            block = line
            status, output = commands.getstatusoutput("grep '%s' missing_blocks_perfile" % block)
            if status != 0:
                print "FREE: %s" % block


def check_rucio_rules():

    print "Checking for non-needed rucio rules"

    with open("rucio-rules.feb24", "r") as infile:
        rules = infile.read().split("\n")

    with open("missing_blocks_perfile.feb24", "r") as infile:                    #   missing_blocks_perfile.feb24.   #missing_blocks_sites_wholelist.feb24
        blocksstring = infile.read().split("\n")[:-1]
        blocks = [x.split(":")[0] for x in blocksstring]

    #print blocks
    #raw_input()

    rucioblocks = []
    for rule in rules:
        if "cms:" not in rule: continue
        rucioblock = rule.split("cms:")[1].split()[0]
        rucioblocks.append(rucioblock)

        ruleid = rule.split()[0]
        #print rucioblock, blocks[0]

        if rucioblock not in blocks:
            print "rucio delete-rule %s" % ruleid
        else:
            print "active: %s, %s" % (ruleid, rucioblock)


def check_rucio_rules_sizeblocks():

    if False:
        with open("rucio-rules.feb24", "r") as infile:
            rules = infile.read().split("\n")

        for rule in rules:
            if "cms:" not in rule: continue
            rucioblock = rule.split("cms:")[1].split()[0]
            status, output = commands.getstatusoutput("grep %s missing_blocks_perfile.feb24" % rucioblock)
            #status, output = commands.getstatusoutput("grep %s missing_blocks_nonavailable.feb24.rucio" % rucioblock)
            print rucioblock, output
            if status!=0:
                print output


    with open("missing_blocks_perfile.feb24", "r") as infile:
        rules = infile.read().split("\n")

    for rule in rules:
        if "/" not in rule: continue
        rucioblock = rule
        status, output = commands.getstatusoutput("grep %s rucio-rules.feb24" % rucioblock)
        if status!=0:
            #print "rucio add-rule --ask-approval --lifetime 1209600 cms:%s 1 T2_DE_DESY" % rucioblock
            print rucioblock

get_all_blocks()
get_block_sites()
check_block_availability()
#free_copied_blocks()
check_rucio_rules()
#check_rucio_rules_sizeblocks()
