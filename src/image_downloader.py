#!/usr/local/bin/python3
from urllib import parse,request
import os
import logging
import time
import datetime


def get_image_name_from_url(img_url):
    '''
    Name    : get_image_name_from_url
    Input   : img_url - url of the image to be downloaded
    Ouptput : basename of the file
    Description: This function takes an image url as input and returns the basename of the file from the url
    '''
    imgpath = parse.urlsplit(img_url)
    return os.path.basename(imgpath.path)
    
def download_image_to_path(image_url,output_path,output_img_name):
    '''
    Name   :  download_image_to_path
    Input  :  image_url - url to download,
              output_path - path to save download images,
              output_img_name - name of image to be saved
    Ouptput : True - if download is success
              False - if download fails
    Description: This function takes url from which the image is to be downloaded, output location to save the image and image name as inputs and returns True if download is success else returns False in case of failure
    '''
    success_flag = True
    try:
        img_location = os.path.join(output_path,output_img_name)
        request.urlretrieve(image_url,img_location)
        logging.info('Image {imgname} downloaded successfully from {image_url}'.format(imgname = output_img_name,image_url = image_url))
    except Exception as e:
        logging.warning("{image_url} failed with error-{err}".format(image_url = image_url, err=e))
        success_flag = False
    return success_flag

def process_img_urls(img_urls_list,output_dir):
    '''
    Name    : process_img_urls
    Input   : img_urls_list - urls list pointer ,
              output_dir - outputfile saving location
    Ouptput : warnings_cnt 
    Description: This function takes each url from the urls list ,tries to download the image and registers all the info and errors occured as warnings in the log file and returns total warnings that occurred in case of any download failure
    '''
    #keep track of no of warnings
    warnings_cnt=0
    #process each url
    for image_url in img_urls_list:   
        #remove new line characters if any after url
        image_url = image_url.strip()
        #get image name from url
        imgname = get_image_name_from_url(image_url)
        #download and save the image to given output path
        dwnld_img_status = download_image_to_path(image_url,output_dir,imgname)
                    
        #log any errors or warnings
        if not dwnld_img_status:
            warnings_cnt+=1
    return warnings_cnt
        
def download_images_from_file(input_text_file,log_file):
    '''
    Name    : download_images_from_file
    Input   : input_text_file - urls list pointerinput text file to be processed,
              log_file - file used for logging
    Ouptput : none 
    Description: This function process opens text file and process each url to download the images and logs details of info,warnings and errors during the process.
    '''
    
    #start logging
    start_msg = '*****File Processing started at {t}*****'.format(t=datetime.datetime.now())
    logging.info(start_msg)
    print(start_msg)
    
    ###BASES cases###
    #check for valid file
    if not os.path.isfile(input_text_file):
        logging.error("{inputfile} is not found".format(inputfile = input_text_file))
        print('Program has failed because of invalid {inputfile}.Check {logfile} for details'.format(inputfile = input_text_file,logfile = log_file))
        return
        
    #check if empty file
    if not os.path.getsize(input_text_file):
        logging.warning('{inputfile} is empty'.format(inputfile = input_text_file))
        print('Program has completed with warnings. Check {logfile} for details'.format(logfile = log_file))
        return
    
    #PROCESS THE CONTENTS OF FILE    
    try:
        #open the text file
        with open(input_text_file) as image_file_urls:            
            #set ouptput location
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'downloaded_images')
            
            if not os.path.isdir(output_dir):
                os.mkdir(output_dir)
                
            #process img urls and count any warings or failures occured in the process
            warnings_cnt = process_img_urls(image_file_urls,output_dir)
            
            if warnings_cnt:
                print('Program has completed with {wrn_cnt} warnings.\nDownloaded Images are saved in path - {output_dir}.\nCheck {logfile} for additional details'.format(wrn_cnt = warnings_cnt,output_dir = output_dir,logfile = log_file))
            else:
                print('Program has completed successfully.\nDownloaded Images are saved in path {output_dir}.\nCheck {logfile} for additional details'.format(output_dir = output_dir,logfile = log_file))
            
    except Exception as e:
        #catch exceptions
        logging.error("Error occurred- {error} - while processing {inputfile} ".format(error = e,inputfile=input_text_file))
        print('Program has failed due to {error}.Check {logfile} for more details.'.format(error=e,logfile = log_file))
    

#Driver Program
def main():
    inputtfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),'sample_urls.txt') #input('Input Text File-')
    logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.splitext(os.path.basename(inputtfile))[0]+'_log.log')
    start = time.time()
    logging.basicConfig(filename=logfile,filemode='a',format='%(asctime)s %(levelname)s %(funcName)s %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
    download_images_from_file(input_text_file=inputtfile,log_file=logfile)
    duration = time.time() - start
    completion_msg = '*****File Processing completed in {duration} secs at {t}*****\n'.format(duration = round(duration,2),t=datetime.datetime.now())
    logging.info(completion_msg)
    logging.shutdown()
    print(completion_msg)
    

if __name__ == '__main__':
    main()