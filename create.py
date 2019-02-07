#!/usr/local/bin/python3.6

import boto3
import sys
import urllib.request
import shutil


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


def create_index_html_file():
## Create index.html document
	file = open('./index.html','w')
	file.write('<!DOCTYPE html>\n')
	file.write('<html lang="en">\n')
	file.write('	<head>\n')
	file.write('		<!-- required meta tags -->\n')
	file.write('		<meta charset="utf-8">\n')
	file.write('		<meta http-equip="X-UA-Compatible" conent="IE=edge">\n')
	file.write('		<meta name="viewport" content="width=device-width, initial-scale=1">\n\n')
	file.write('		<!-- title -->\n')
	file.write('		<title>CMEI Systems Inc.</title>\n\n')
	file.write('		<!-- favicon -->\n')
	file.write('		<link rel="shortcut icon" href="img/favicon.ico">\n')
	file.write('		<!-- google fonts -->\n')
	file.write('		<link href="https://fonts.googleapis.com/css?family=Roboto+Condensed:300,300i,400,400i,700,700i" rel="stylesheet">\n')
	file.write('		<!-- style CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/style.css">\n\n')
	file.write('	</head>\n')
	file.write('	<body>\n')
	file.write('		<h1>Welcome to CMEI Systems</h1>\n')
	file.write('		<!-- jQuery -->\n')
	file.write('		<script src="js/jquery.js"></script>\n') ## jquery needs to come before custom.js
	file.write('		<!-- custom JS -->\n')
	file.write('		<script src="js/custom.js"></script>\n')
	file.write('	</body>\n')
	file.write('</html>\n')
	file.close()

def create_style_css_file():
## Create style.css file
	file = open('./style.css','w')
	file.write('/*=====================================================================================\n')
	file.write('                                         	DEFAULT VALUES                               \n')
	file.write('\n\n')
	file.write('                                       Font Family:        Roboto Condensed              \n')
	file.write('\n\n\n')
	file.write('=====================================================================================*/\n')
	file.write('body {\n')
	file.write('	font-family: "Roboto Condensed", sans-serif;\n\n')
	file.write('}\n')
	file.close()
	

def upload_file(bucket,object,file_name):
## Upload file to S3
	content = open(file_name,'rb')
	s3 = boto3.client('s3')
	if file_name == 'index.html':
	## if index.html specify the contenttype and make it public
		s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/html',ACL='public-read')
	elif file_name == 'style.css':
		s3.put_object(Bucket=bucket,Key=object,Body=content,ContentType='text/css',ACL='public-read')
	else:
		s3.put_object(Bucket=bucket,Key=object,Body=content)
		

# Start of User inputs

bucket_name = 'cmei-website-bucket'
bucket_name_img = 'cmei-website-image-bucket'
download_web_list = [['https://code.jquery.com/jquery-3.3.1.js','jquery.js']] ## Download these files from the web
upload_web_files = [['jquery.js','js/jquery.js']]
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
	print('Bucket %s successfully created'%bucket_name)
else:
	print('The %s bucket already exists'%bucket_name)

create_basic_structure(bucket_name)
copy_objects(bucket_name_img,bucket_name)
download_web_files(download_web_list)
for file in upload_web_files:
	upload_file(bucket_name,file[1],file[0])
create_index_html_file()
create_style_css_file()
for file in upload_other_files:
	upload_file(bucket_name,file[1],file[0])





