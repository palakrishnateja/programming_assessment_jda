#install all the requirements
pip3 install -r ../../requirements.txt
#create a cron job to schedule the script
/usr/local/bin/python3 ../deployment_scripts/cron_job_runner.py
#kickstart the http server
/usr/local/bin/python3 ../deployment_scripts/http_server_launcher.py
