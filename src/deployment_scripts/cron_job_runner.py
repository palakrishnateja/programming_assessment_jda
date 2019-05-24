#!/usr/local/bin/python3
from crontab import CronTab
import os
import getpass


class createCronJob():
    '''
    Name : createCronJob
    Descripion: This class creates a new job to run a python script every "x"mins passed as the inputs for the inputuser or current user by default
    '''
    def __init__(self,user_name=None):
        '''
        Contructor takes username as input if entered else current username by default
        '''
        if user_name is not None:
            self.user_name = createCronJob.get_user_name()
        else:
            self.user_name = user_name
    
    @staticmethod
    def get_user_name():
        '''
        Name : get_user_name
        Descritpion: This is a static method that returns the current user
        '''
        return getpass.getuser()
    
    def create_new_cron_job(self,py_file,schedule_to_run_every_in_mins):
        '''
        Name    : create_new_cron_job
        Input   : py_file - python script to be run,
                  schedule_to_run_every_in_mins - time in mins for which the job is to be run every time  
        Ouptput : job object - the new cron job object created on the machine
        Description: This method creates a new cron job that runs the input python script every "X" mins provided in the input
                  and returns the details of the job as object
        '''
        try:
            cron = CronTab(user=self.user_name)
            cmd  = '/usr/local/bin/python3 {pythonfile}'.format(pythonfile = py_file)
            cmt  = 'This job runs {pythonfile} script every 5mins which downloads images from urls provided in input txt file and saves it to local directory'.format(pythonfile = py_file)
            print('cmd-',cmd)
            print('cmt-',cmt)
            cron.remove_all()
            job  = cron.new(command=cmd , comment=cmt)  
            job.minute.every(schedule_to_run_every_in_mins)
            cron.write()
            print('cron job for user:{usr} created succesfully'.format(usr=self.user_name))
            return job
        except Exception as e:
            print('cron job creation for user:{usr} failed with error - {err}'.format(err=e,usr=self.user_name))
    
    
    def enable_cron_job(self,job):
        '''
        Name    : enable_cron_job
        Input   : job - job which has to be enabled
        Ouptput : None
        Description: This function enable the input job if not enable already
        '''
        try:
            if not job.is_enabled():
                job.enable()
                print('cron job is enabled successfully') 
            else:
                print('job is enabled already')
            return True
        except Exception as e:
            print('enabling cron job failed with error - {err}'.format(err=e))
            return False
            

#Driver Program
if __name__ == '__main__':
    #input parameters
    user_name = input('Create cron job for username(leave blank to create for current user by default)-')
    python_file = os.path.join(os.path.dirname(os.path.abspath(__file__))+os.sep+'..'+os.sep+'image_downloader.py')
    schedule_job_every_in_mins = 5
    
    #create cron job class instance
    cron_job_obj = createCronJob(user_name)
    
    #if python file exists ,then schedule cron job
    if os.path.isfile(python_file):
        cronjob = cron_job_obj.create_new_cron_job(python_file,schedule_job_every_in_mins)
        if cronjob:
            if cron_job_obj.enable_cron_job(cronjob):
                print('cron job is created,enabled and is running!!')
    else:
        print('{pyfile} doesnot exits or invalid !!'.format(pyfile = python_file))
    