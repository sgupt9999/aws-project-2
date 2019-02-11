#!/usr/local/bin/python3.6

import boto3
import sys
import urllib.request
import shutil
from zipfile import ZipFile
from os import listdir
from os.path import join


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


def create_index_html_file_test():
## Create index.html document
	file = open('./index.html','w')
	file.write('<!DOCTYPE html>\n')
	file.write('<html lang="en">\n')
	file.write('\n')
	file.write('\n')
	file.write('	<head>\n')
	file.write('\n')
	file.write('\n')
	file.write('		<!-- required meta tags -->\n')
	file.write('		<meta charset="utf-8">\n')
	file.write('		<meta http-equip="X-UA-Compatible" conent="IE=edge">\n')
	file.write('		<meta name="viewport" content="width=device-width, initial-scale=1">\n\n')
	file.write('		<!-- title -->\n')
	file.write('		<title>CMEI Systems Inc.</title>\n\n')
	file.write('		<!-- favicon -->\n')
	file.write('		<link rel="shortcut icon" href="img/favicon.ico">\n')
	file.write('		<!-- google fonts -->\n')
	file.write('		<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Condensed:300,300i,400,400i,700,700i">\n')
	file.write('		<!-- fontawesome -->\n')
	file.write('		<link rel="stylesheet" href="css/font-awesome/css/font-awesome.min.css">\n')
	file.write('		<!-- bootstrap CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/bootstrap/bootstrap.min.css">\n')
	file.write('		<!-- style CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/style.css">\n\n')
	file.write('\n')
	file.write('\n')
	file.write('	</head>\n')
	file.write('\n')
	file.write('\n')
	file.write('	<body>\n')
	file.write('\n')
	file.write('\n')
	file.write('		<h1>BS Grid System Examples</h1>\n')
	file.write('		<h3>1 Column</h3>\n')
	file.write('		<div class="container">')
	file.write('\n')
	file.write('		<div class="row">')
	file.write('\n')
	file.write('		<div class="col-md-12 col-1">')
	file.write('\n')
	file.write('			Content 1')
	file.write('\n')
	file.write('		</div>\n')
	file.write('\n')
	file.write('		</div>\n')
	file.write('\n')
	file.write('		</div>\n')
	file.write('\n')
	file.write('		<h3>2 Columns</h3>\n')
	file.write('		<div class="container">')
	file.write('\n')
	file.write('		<div class="row">')
	file.write('\n')
	file.write('		<div class="col-md-6 col-1">')
	file.write('\n')
	file.write('			Content 1')
	file.write('\n')
	file.write('		</div>\n')
	file.write('		<div class="col-md-6 col-2">')
	file.write('\n')
	file.write('			Content 2')
	file.write('\n')
	file.write('		</div>\n')
	file.write('\n')
	file.write('		</div>\n')
	file.write('\n')
	file.write('		</div>\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('		<h1>Welcome to CMEI Systems</h1>\n')
	file.write('		<i class="fa fa-laptop"></i>\n')
	file.write('		<i class="fa fa-camera fa-5x"></i>\n')
	file.write('		<!-- jQuery -->\n')
	file.write('		<script src="js/jquery.js"></script>\n') ## jquery needs to come before custom.js and bootstrap
	file.write('		<!-- bootstrap JS -->\n') 
	file.write('		<script src="js/bootstrap/bootstrap.min.js"></script>\n') 
	file.write('		<!-- custom JS -->\n')
	file.write('		<script src="js/custom.js"></script>\n')
	file.write('\n')
	file.write('\n')
	file.write('	</body>\n')
	file.write('\n')
	file.write('\n')
	file.write('</html>\n')
	file.close()

def create_style_css_file_old():
## Create style.css file
	file = open('./style.css','w')
	file.write('/*=======================================================================================\n')
	file.write('                                         	DEFAULT VALUES                               \n')
	file.write('\n\n')
	file.write('                                       Font Family       :Roboto Condensed             \n\n')
	file.write('                                       Greenish Blue     :#34c6d3 (Buttons, Icons, Links, Lines & Backgrounds              \n')
	file.write('                                       Steel Gray        :#41464b (Headings)             \n')
	file.write('                                       Blue Bayoux       :#64707b (Paragraphs)           \n')
	file.write('                                       White             :#fff (Text with Black Backgrounds \n')
	file.write('                                       Black             :#000                           \n')
	file.write('\n\n\n')
	file.write('=======================================================================================*/\n')
	file.write('body {\n')
	file.write('	font-family: "Roboto Condensed", sans-serif;\n\n')
	file.write('}\n')
	file.write('/* CSS - Just for Grid Examples */\n')
	file.write('.col-1 {background-color: red;}\n')
	file.write('.col-2 {background-color: green;}\n')
	file.write('.col-3 {background-color: blue;}\n')
	file.write('.col-4 {background-color: yellow;}\n')
	file.close()


def create_index_html_file():
## Create index.html document
	file = open('./index.html','w')
	file.write('<!DOCTYPE html>\n')
	file.write('<html lang="en">\n')
	file.write('\n')
	file.write('\n')
	file.write('	<head>\n')
	file.write('\n')
	file.write('\n')
	file.write('		<!-- required meta tags -->\n')
	file.write('		<meta charset="utf-8">\n')
	file.write('		<meta http-equip="X-UA-Compatible" conent="IE=edge">\n')
	file.write('		<meta name="viewport" content="width=device-width, initial-scale=1">\n\n')
	file.write('		<!-- title -->\n')
	file.write('		<title>CMEI Systems Inc.</title>\n\n')
	file.write('		<!-- favicon -->\n')
	file.write('		<link rel="shortcut icon" href="img/favicon.ico">\n')
	file.write('		<!-- google fonts -->\n')
	file.write('		<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Condensed:300,300i,400,400i,700,700i">\n')
	file.write('		<!-- fontawesome -->\n')
	file.write('		<link rel="stylesheet" href="css/font-awesome/css/font-awesome.min.css">\n')
	file.write('		<!-- bootstrap CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/bootstrap/bootstrap.min.css">\n')
	file.write('		<!-- animate CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/animate/animate.css">\n')
	file.write('		<!-- style CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/style.css">\n\n')
	file.write('\n')
	file.write('\n')
	file.write('	</head>\n')
	file.write('\n')
	file.write('\n')
	file.write('	<body>\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('\n')
	file.write('		<!-- Home -->\n')
	file.write('		<section id="home">\n')
	file.write('			<div id="home-cover" class="bg-parallax animated fadeIn">\n')
	file.write('				<div id="home-content-box">\n')
	file.write('					<div id="home-content-box-inner" class="text-center">\n')
	file.write('						<div id="home-heading" class="animated zoomIn">\n')
	file.write('							<h3>Watch Out <br> The Modern Responsive Website!<h3>\n')
	file.write('						</div>\n')
	file.write('						<div id="home-btn" class="animated zoomIn">\n')
	file.write('							<a class="btn btn-lg btn-general btn-white" href="#work" roles="button"\n')
	file.write('							title="View Our Work">View Our Work</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('				</div>\n')
	file.write('			</div>\n')
	file.write('		</section>\n')
	file.write('		<br><br><br><br><br><br><br><br>br><br><br><br><br><br><br><br>')
	file.write('		<!-- jQuery -->\n')
	file.write('		<script src="js/jquery.js"></script>\n') ## jquery needs to come before custom.js and bootstrap
	file.write('		<!-- bootstrap JS -->\n') 
	file.write('		<script src="js/bootstrap/bootstrap.min.js"></script>\n') 
	file.write('		<!-- custom JS -->\n')
	file.write('		<script src="js/custom.js"></script>\n')
	file.write('\n')
	file.write('\n')
	file.write('	</body>\n')
	file.write('\n')
	file.write('\n')
	file.write('</html>\n')
	file.close()

def create_style_css_file():
## Create style.css file
	file = open('./style.css','w')
	file.write('/*=======================================================================================\n')
	file.write('                                         	DEFAULT VALUES                               \n')
	file.write('\n\n')
	file.write('                                       Font Family       :Roboto Condensed             \n\n')
	file.write('                                       Greenish Blue     :#34c6d3 (Buttons, Icons, Links, Lines & Backgrounds              \n')
	file.write('                                       Steel Gray        :#41464b (Headings)             \n')
	file.write('                                       Blue Bayoux       :#64707b (Paragraphs)           \n')
	file.write('                                       White             :#fff (Text with Black Backgrounds \n')
	file.write('                                       Black             :#000                           \n')
	file.write('\n\n\n')
	file.write('=======================================================================================*/\n')
	file.write('/* General CSS */\n\n')
	file.write('html, body {\n')
	file.write('	height: 100%;\n')
	file.write('}\n\n')	
	file.write('body {\n')
	file.write('	font-family: "Roboto Condensed", sans-serif;\n\n')
	file.write('}\n')
	file.write('h3 {\n')
	file.write('	text-transform: uppercase;\n')
	file.write('}\n')
	file.write('/*==============================================================\n')
	file.write('				HOME				    \n')
	file.write('==============================================================*/\n')
	file.write('#home {\n')
	file.write('	height: 100%;\n')
	file.write('}\n\n')
	file.write('#home-cover {\n')
	file.write('	height: 100%;\n')
	file.write('	background-image: url("../img/bg-home.jpg");\n')
	file.write('}\n')
	file.write('#home-content-box {\n')
	file.write('	width: 100%;\n')
	file.write('	height: 100%;\n')
	file.write('	display:table;\n')
	file.write('}\n')
	file.write('#home-content-box-inner {\n')
	file.write('	display: table-cell;\n')
	file.write('	vertical-align: middle;\n')
	file.write('}\n')
	file.write('#home-heading h3 {\n')
	file.write('	color: #fff;\n')
	file.write('	font-size: 55px;\n')
	file.write('	font-weight: 700;\n')
	file.write('	margin: 20px 0 20px 0;\n')
	file.write('}\n')
	file.write('/*==============================================================\n')
	file.write('				PARALLAX (Generic)		    \n')
	file.write('==============================================================*/\n')
	file.write('.bg-parallax {\n')
	file.write('	background-repeat: no-repeat;\n')
	file.write('	background-size: cover;\n')
	file.write('	background-position: center;\n')
	file.write('	background-attachment: fixed;\n') ##This is to provide parallax affect
	file.write('}\n')
	file.write('/*==============================================================\n')
	file.write('				BUTTONS (Generic)		    \n')
	file.write('==============================================================*/\n')
	file.write('.btn-general {\n')
	file.write('	border-width: 2px;\n')
	file.write('	border-radius: 0;\n')
	file.write('	padding: 12px 26px 12px 26px;\n')
	file.write('	font-size: 16px;\n')
	file.write('	font-weight: 400;\n')
	file.write('	text-transform: uppercase;\n')
	file.write('}\n')
	file.write('.btn-white {\n')
	file.write('	border-color: #fff;\n')
	file.write('	color: #fff;\n')
	file.write('}\n')
	file.write('.btn-white:hover, .btn-white:focus {\n')
	file.write('	background-color: #fff;\n')
	file.write('	color: #41464b;\n')
	file.write('}\n')
	file.write('/*==============================================================\n')
	file.write('				ANIMATE				    \n')
	file.write('==============================================================*/\n')
	file.write('#home-cover, #home-heading, #home-btn {;\n')
	file.write('	animation-duration: .5s;\n')
	file.write('}\n')
	file.write('#home-cover {\n')
	file.write('	animation-delay: .1s;\n')
	file.write('}\n')
	file.write('#home-heading {\n')
	file.write('	animation-delay: .5s;\n')
	file.write('}\n')
	file.write('#home-btn {\n')
	file.write('	animation-delay: 1s;\n')
	file.write('}\n')
	file.close()
	

def upload_file(bucket,object,file_name):
## Upload file to S3
	content = open(file_name,'rb')
	s3 = boto3.client('s3')
	#if file_name == 'index.html':
	if file_name.split('.')[-1] == 'html': ## if the file name ends in html then make the context text/html
	## if index.html specify the contenttype and make it public
		#s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/html',ACL='public-read')
		s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/html')
	#elif file_name == 'style.css':
	elif file_name.split('.')[-1] == 'css':
		#s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/css',ACL='public-read')
		s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/css')
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


# Start of User inputs

bucket_name = 'cmei-website-bucket'
bucket_name_img = 'cmei-website-image-bucket'
download_web_list = [['https://code.jquery.com/jquery-3.3.1.js','jquery.js'],\
		     ['https://fontawesome.com/v4.7.0/assets/font-awesome-4.7.0.zip','font-awesome.zip'],\
		     ['https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip','bootstrap-3.3.7-dist.zip'],
		     ['https://raw.github.com/daneden/animate.css/master/animate.css','animate.css']] ## Download these files from the web
upload_web_files = [['jquery.js','js/jquery.js'],['animate.css','css/animate/animate.css']]
upload_other_files = [['index.html','index.html'],['style.css','css/style.css']]

# End of User inputs


create_index_html_file()
create_style_css_file()
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
copy_objects(bucket_name_img,bucket_name)
download_web_files(download_web_list)
for file in upload_web_files:
	upload_file(bucket_name,file[1],file[0])
unzip_upload_fontawesome(bucket_name)
unzip_upload_bootstrap(bucket_name)
create_index_html_file()
create_style_css_file()
for file in upload_other_files:
	upload_file(bucket_name,file[1],file[0])





