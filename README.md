# programming_assessment_jda
Code repository for JDA programming assessment

PROJECT DETAILS
******************************************************************************************************************************
PROBLEM STATEMENT :
******************************************************************************************************************************
This project is developed to answer the following requirement
"Given a plaintext file containing URLs, one per line, like
	http://mywebserver.com/images/271947.jpg
	http://mywebserver.com/images/24174.jpg
Write a python script that takes this plaintext file as an argument and downloads all images, storing them on the local hard disk.  Imagine this code will be used in important live systems, modified later on by other developers, and so on.

In a deployment scenario this script needs to be deployed to multiple Debian machines, scheduled to run every five minutes. The downloaded images should be served via http on each server.

Provide an example deployment or instructions with your solution."

******************************************************************************************************************************
PREREQUISITES :
******************************************************************************************************************************
1) This code repo is developed for python3.x preferably 3.7.x
2) python3 should be available in location - /usr/local/bin/python3
3) requirements.txt is created for python 3.x

******************************************************************************************************************************
THIS PROJECT CONTAINS THE FOLLOWING FILES/DIRECTORIES
******************************************************************************************************************************
1) git_cloner.py 
	- This script helps to clone the git repository of all the code to a 'git_code_repo' directory in the path on the machine where it is run.
2) requirements.txt 
	- This contains all the necessary python modules with versions required to run the python scripts.

3) src directory: 
	1) image_downloader.py:
		- This script takes a text file <<input_txt_file.txt>> containing urls as input.
		- It creates a log file <<input_txt_file_log.log>> of the same name as input txt file with an extension of 		     .log if not available already or else just appends to the existing log file.
		- It creates a directory (downloaded_images) in the current location if not available already.
		- The urls from input_txt_file.txt are read and the files are downloaded to downloaded_images directory.
		- All the details of image downloads are logged in the input_txt_file_log.log file.
		- This script handles the edges cases like empty file,invalid file path,huge files with millions of links and overwrites  if the file of the same name exists and also for duplicate links.
	    NOTE: The script doesn't fail if any error occurs while downloading the image from url. 
    	          Instead ,it downloads all the possible images and any errors occured are registered as warnings in the log                     file.
	2) sample_urls.txt:
		- Sample input text file with image urls
	3) deployment_scripts directory:
		1) cron_job_runner.py
			- This script creates a cron job for scheduling the image_downloader.py to run every "X" mins(X is time in mins) on the machine where it is run.
		2) http_server_launcher.py
			- This script starts a httpserver that serves the images downloaded in downloaded_images directory at                           http://hostname:portno
			- The server runs forever until it is killed.
			- The server can be killed through keyboard interrup short key(ctrl+c).
		3) deployment_steps.txt
			- This text file has the idea of how one can deploy this code in any Debian machine.
		4) start.sh
			- This is a shell script that helps to set up all the steps mentioned in deployment_steps.txt
4) steps_to_run_this_program:
	- This file lists all the steps that need to be followed to run this project.
5) demo directory:
	- This directory contains all the screenshots of the project when one follows the steps mentioned in steps_to_run_this_program file.
