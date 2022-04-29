import os, sys
from glob import glob

test = True


isfast = True


if isfast: 
    #minilist = glob('/nfs/dust/cms/user/beinsam/LongLiveTheChi/Production/AttemptPhase1/CMSSW_10_6_20/src/fast*_miniAODSIM.root')
    minilist = glob('/pnfs/desy.de/cms/tier2/store/user/sbein/CommonSamples/RadiativeMu_2018Fast/v3/*_inMINIAODSIM.root')
    alreadyglob = ''.join(glob('*.root'))
    scenario = 'Autumn18sig'
else: 
    minilist = glob('/nfs/dust/cms/user/beinsam/LongLiveTheChi/Production/AttemptPhase1/CMSSW_10_2_25/src/full2018_step3_inMINIAODSIM.root')
    alreadyglob = ''.join(glob('*.root'))
    scenario = 'Autumn18sig'

print 'len(alreadyglob)', len(alreadyglob)

for ijob, minifile in enumerate(minilist):
    outname = minifile.split('/')[-1].split('_inMINIAOD')[0]
    if outname in alreadyglob:
        print 'we got this one already', outname
        continue
    else: print outname, 'will be new'


    command = 'cmsRun runMakeTreeFromMiniAOD_cfg.py outfile='+outname+' dataset=file:'+minifile+' scenario='+scenario+' numevents=-1'

    if not isfast: command = command.replace('Fastsig','')
    if not (ijob+1)%10==0: command+=' &'
    print command
    if len(glob('*'+outname+'*'))>0: 
        print 'continuing past', glob('*'+outname+'*')[0]
        continue
    if not test: os.system(command)


#Summer16MiniAODv3Fastsig
