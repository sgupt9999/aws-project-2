#!/usr/local/bin/python3.6

import boto3
import sys
import uuid

def create_bucket_name(bucket_prefix):
## Create a random bucket name with a given prefix
	print(current_region)
	return ''.join([bucket_prefix,str(uuid.uuid4())])

def create_temp_file(size, file_name,file_content):
	random_file_name = ''.join([str(uuid.uuid4().hex[:6]),file_name])
	with open(random_file_name,'w') as f:
		f.write(str(file_content) * size)
	return random_file_name

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
							

def create_basic_structure(bucket):
# Create a basic file structure for the website
	client = boto3.client('s3')
	response = client.put_object(Bucket=bucket,ACL='public-read',Key='index.html')
	response = client.put_object(Bucket=bucket,Key='css/style.css')
	client.put_object(Bucket=bucket,Key='js/custom.js')
	print('Basic website structure completed')

def upload_new_files(bucket):
## Upload the new files for the website
	client = boto3.resource('s3')
	client.Object(bucket,'index.html').upload_file('./index.html')
	s3 = boto3.client("s3")
	src_key = 'index.html'
	src_bucket = bucket
	s3.copy_object(Key=src_key, Bucket=src_bucket,
               CopySource={"Bucket": src_bucket, "Key": src_key},
               Metadata={"Content-Type": "text/html"},
               MetadataDirective="REPLACE")

def upload_new_files2(bucket):
	content = open('./index.html','rb')
	s3 = boto3.client('s3')
	s3.put_object(Bucket=bucket,Key='index.html',Body=content,Metadata={'Content-Type':'text/html'})

def create_index():
## Create index.html document
	file = open('./index.html','w')
	file.write('<!DOCTYPE html>\n')
	file.write('<html>\n')
	file.write('	<head>\n')
	file.write('	</head>\n')
	file.write('	<body>\n')
	file.write('		<h1>Welcome to CMEI Systems 222222</h1>\n')
	file.write('	</body>\n')
	file.write('</html>\n')
	file.close()

# User inputs
bucket_name = 'cmei-website-bucket'
bucket_name_img = 'cmei-website-image-bucket'


create_index()
upload_new_files2(bucket_name)

exit(1)
session = boto3.session.Session()
current_region = session.region_name
client = boto3.client('s3')

if not bucket_exists(bucket_name):
# Create the bucket one time
	response = client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':current_region})
	waiter = client.get_waiter('bucket_exists')
	try:
        	waiter.wait(Bucket=bucket_name)
	except:
        	print('Bucket failed to create. Exiting the script')
        	exit(1)
	print('Bucket %s successfully created'%bucket_name)
else:
	print('The %s bucket already exists'%bucket_name)

create_basic_structure(bucket_name)
copy_objects(bucket_name_img,bucket_name)
create_index()





