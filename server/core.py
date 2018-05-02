import os
import boto3

storage_client = boto3.client('s3')
bucket_name = 'impressar-files'
path = os.path.abspath('../Test-models/test.obj')
filename = 'test.obj'

def core():
    try:
        storage_client.upload_file(path, bucket_name, filename)
        print('Done')
    except Exception as ex:
        print('wtf s3')
        print(ex)



