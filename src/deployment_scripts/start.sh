#install all the requirements
pip3 install -r ../../requirements.txt
echo 'REQUIREMENTS ARE INSTALLED'
#create a cron job to schedule the script
echo 'CRON JOB CREATION'
/usr/local/bin/python3 ../deployment_scripts/cron_job_runner.py
#kickstart the http server
echo 'HTTP SERVER CREATION AND LAUNCH'
/usr/local/bin/python3 ../deployment_scripts/http_server_launcher.py
