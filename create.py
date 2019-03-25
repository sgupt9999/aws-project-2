#!/usr/local/bin/python3.6
### This script creates AWs S3 hosted website

import boto3
import sys
import urllib.request
import shutil
from zipfile import ZipFile
from os import listdir
from os.path import join
from index import create_index_html_file
from style import create_style_css_file


def bucket_exists(bucket):
## check if this bucket already exists
	client = boto3.client('s3')
	response = client.list_buckets()
	for bucket2 in response['Buckets']:
		if bucket2['Name'] == bucket:
			return True
	return False

def list_objects(bucket):
## List all the objects and size in a given bucket
	client = boto3.client('s3')
	response = client.list_objects_v2(Bucket=bucket)
	if 'Contents' in response.keys():
		for object in response['Contents']:
			print(object['Key'],'---------',object['Size'])
	else:
		print('The %s bucket has no objects'%bucket)

def delete_objects(bucket):
## Delete all objects in a given bucket
	client = boto3.client('s3')
	response = client.list_objects_v2(Bucket=bucket)
	if 'Contents' in response.keys():
		for object in response['Contents']:
			print('Deleting ',object['Key'])
			resonse_delete = client.delete_object(Bucket=bucket,Key=object['Key'])
	else:
		print('The %s bucket has no objects'%bucket)

def copy_objects(bucket_src,bucket_dst):
## Copy all objects from source to destination bucket
	client_src = boto3.client('s3')
	response_src = client_src.list_objects_v2(Bucket=bucket_src)
	if 'Contents' in response_src.keys():
		client_dst = boto3.client('s3')
		for object in response_src['Contents']:
			client_dst.copy_object(Bucket=bucket_dst,CopySource={'Bucket':bucket_src,'Key':object['Key']}, \
						Key=object['Key'])
			print('Copied object %s'%object['Key'])
	else:
		print('The %s bucket is empty'%bucket_src)
							
def download_web_files(list_files):
## Download the files from the web
## list_files is a list of lists with 2 elements, the download location and the name of the saved file
        for file in list_files:
                with urllib.request.urlopen(file[0]) as response, open(file[1], 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)

def create_basic_structure(bucket):
## Create a basic file structure for the website
## Create index.html and 2 folders css and js
	client = boto3.client('s3')
	response = client.put_object(Bucket=bucket,ACL='public-read',Key='index.html')
	response = client.put_object(Bucket=bucket,Key='css/style.css')
	client.put_object(Bucket=bucket,Key='js/custom.js')
	print('Basic website structure completed')



def create_custom_js_file():
## Create custom.js file
	file = open('./custom.js','w')
	file.write('/*=======================================================================================\n')
	file.write('                                         	SERVICES                                     \n')
	file.write('=======================================================================================*/\n')
	file.write('$(function() {\n')
	file.write('	// animate on scroll\n')
	file.write('	new WOW().init();\n')
	file.write('});\n')
	file.write('/*=======================================================================================\n')
	file.write('                                         	WORK                                     \n')
	file.write('=======================================================================================*/\n')
	file.write('$(function() {\n')
	file.write('	// popup and gallrry feature\n')
	file.write('	$("#work").magnificPopup({\n')
	file.write('		delegate: \'a\', //child item selector, by clicking on it popup will open\n')
	file.write('		type: \'image\',\n')
	file.write('		gallery: {\n')
	file.write('			enabled: true\n')
	file.write('		}\n')
	file.write('	});\n')
	file.write('});\n')


def upload_file(bucket,object,file_name):
### Upload file_name to bucket and save as object
	content = open(file_name,'rb')
	s3 = boto3.client('s3')
	if file_name.split('.')[-1] == 'html': ## if the file name ends in html then make the context text/html
		s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/html')
	elif file_name.split('.')[-1] == 'css':
		s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/css')
	elif file_name.split('.')[-1] == 'js':
		s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='application/javascript')
	else:
		s3.put_object(Bucket=bucket,Key=object,Body=content)
		
def unzip_upload_fontawesome(bucket):
## This file has multiple sub-folders and all these need to be uploaded to S3
## Creating a separate function just for font-awesome
	with ZipFile('font-awesome.zip','r') as zip:
		zip.extractall()
	## Copy all files from the css and fonts sub-folder of the unzipped folder to S3
	mypath = './font-awesome-4.7.0/css'
	for file in listdir(mypath):
		upload_file(bucket,'css/font-awesome/css/'+str(file),join(mypath,file))
	mypath = './font-awesome-4.7.0/fonts'
	for file in listdir(mypath):
		upload_file(bucket,'css/font-awesome/fonts/'+str(file),join(mypath,file))

def unzip_upload_bootstrap(bucket):
## This file has multiple sub-folders and all these need to be uploaded to S3
## Creating a separate function just for bootstrap
	with ZipFile('bootstrap-3.3.7-dist.zip','r') as zip:
		zip.extractall()
	## Copy bootstrap.min files from css and js sub-folders to S3
	mypath = './bootstrap-3.3.7-dist/css/bootstrap.min.css'
	upload_file(bucket,'css/bootstrap/bootstrap.min.css',mypath)
	mypath = './bootstrap-3.3.7-dist/js/bootstrap.min.js'
	upload_file(bucket,'js/bootstrap/bootstrap.min.js',mypath)

def unzip_upload_wow(bucket):
## This file is needed so that animations only show when the user scrolls to that page
	with ZipFile('master.zip','r') as zip:
		zip.extractall()
	## Copy wow.min.js
	mypath = './WOW-master/dist/wow.min.js'
	upload_file(bucket,'js/wow/wow.min.js',mypath)


def unzip_upload_magnific(bucket):
## This file is needed so for gallery effect
	with ZipFile('master2.zip','r') as zip:
		zip.extractall()
	## Copy wow.min.js
	mypath = './Magnific-Popup-master/dist/magnific-popup.css'
	upload_file(bucket,'css/magnific-popup/magnific-popup.css',mypath)
	mypath = './Magnific-Popup-master/dist/jquery.magnific-popup.min.js'
	upload_file(bucket,'js/magnific-popup/jquery.magnific-popup.min.js',mypath)

##########################################################################################
### Start of User inputs
##########################################################################################

bucket_name = 'cmei-website-bucket9999'
bucket_name_img = 'cmei-website-image-bucket'
download_web_list = [['https://code.jquery.com/jquery-3.3.1.js','jquery.js'],\
		     ['https://fontawesome.com/v4.7.0/assets/font-awesome-4.7.0.zip','font-awesome.zip'],\
		     ['https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip','bootstrap-3.3.7-dist.zip'],
		     ['https://raw.github.com/daneden/animate.css/master/animate.css','animate.css'],
		     ['https://github.com/matthieua/WOW/archive/master.zip','master.zip'],
		     ['https://github.com/dimsemenov/Magnific-Popup/archive/master.zip','master2.zip']] ## Download these files from the web
upload_web_files = [['jquery.js','js/jquery.js'],['animate.css','css/animate/animate.css']]
upload_other_files = [['index.html','index.html'],['style.css','css/style.css'],['custom.js','js/custom.js']]

short=0 ### if just want to test the small changes, then make this 1

##########################################################################################
### End of User inputs
##########################################################################################


if short == 1:
	#download_web_files(download_web_list)
	#unzip_upload_magnific(bucket_name)
	create_index_html_file()
	create_style_css_file()
	create_custom_js_file()
	for file in upload_other_files:
		upload_file(bucket_name,file[1],file[0])

	exit(1)


if not bucket_exists(bucket_name):
# Create the bucket one time and make it host a static web site

	session = boto3.session.Session()
	current_region = session.region_name
	client = boto3.client('s3')

	response = client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':current_region})
	waiter = client.get_waiter('bucket_exists')
	try:
        	waiter.wait(Bucket=bucket_name)
	except:
        	print('Bucket failed to create. Exiting the script')
        	exit(1)
	website_cofiguration = {'IndexDocument': {'Suffix':'index.html'}}
	client.put_bucket_website(Bucket=bucket_name,WebsiteConfiguration=website_cofiguration)
	bucket_policy = '{ \
    			"Version": "2012-10-17", \
    			"Statement": [ \
        		{ \
            		"Effect": "Allow", \
            		"Principal": "*", \
            		"Action": "s3:GetObject", \
            		"Resource": "arn:aws:s3:::' + str(bucket_name) + '/*" \
        		} \
    				 ]\
			}'
	client.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)
	print('Bucket %s successfully created'%bucket_name)
else:
	print('The %s bucket already exists'%bucket_name)

#create_basic_structure(bucket_name)
copy_objects(bucket_name_img,bucket_name) ### copy objects from image bucket(which has been pre-populated) to the main website bucket
download_web_files(download_web_list)
for file in upload_web_files:
	upload_file(bucket_name,file[1],file[0])
unzip_upload_fontawesome(bucket_name)
unzip_upload_bootstrap(bucket_name)
unzip_upload_wow(bucket_name)
unzip_upload_magnific(bucket_name)
create_index_html_file()
create_style_css_file()
create_custom_js_file()
for file in upload_other_files:
	upload_file(bucket_name,file[1],file[0])





