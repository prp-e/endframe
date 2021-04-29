import boto3
import config
import os
import sys 
import time

directory = sys.argv[1]
initial_list = os.listdir(directory) 
cloud_list = []

s3_client = boto3.resource('s3', endpoint_url = config.S3_ENDPOINT, aws_access_key_id = config.S3_ACCESS_KEY, aws_secret_access_key = config.S3_SECRET_KEY)
s3_client_secondary = boto3.client('s3', endpoint_url = config.S3_ENDPOINT, aws_access_key_id = config.S3_ACCESS_KEY, aws_secret_access_key = config.S3_SECRET_KEY)
mybucket = s3_client.Bucket(config.S3_BUCKET_NAME)

while True:
    """ Messing around with the cloud """
    temp_cloud_list = mybucket.objects.all()
    temp_list = os.listdir(directory)
    
    for obj in temp_cloud_list:
        cloud_list.append(obj.key)

    for item in cloud_list:
        if item not in initial_list:
            """ Synchronizing with the cloud, downloading the file """ 
            print(f"{item} is on the cloud, but not on the local filesystem.")
            s3_client_secondary.download_file(config.S3_BUCKET_NAME, item, item)
            print(f"{item} downloaded successfully.")

    for item in temp_list:
        if item not in initial_list:
            """ File addition detection """ 
            print(f'New item {item} found, adding to the database!')
            initial_list.append(item)
            print("Database updated successfully.")

    for item in initial_list:
        if item not in temp_list:
            """ File deletion detection """
            print(f"Deletion of {item} detected")
            initial_list.remove(item)
            print("Database updated successfully")
    
    time.sleep(15)
