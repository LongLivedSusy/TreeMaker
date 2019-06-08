from jobSubmitterTM import jobSubmitterTM
import os

def submitJobs():  
    mySubmitter = jobSubmitterTM()
    mySubmitter.run()
    
if __name__=="__main__":
    
    print "Updating condor submission scripts..."
    os.system("cd ..; ./update_custom_submission_scripts.sh; cd condorSub")
    
    submitJobs()
