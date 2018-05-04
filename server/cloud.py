import os
import boto3

class Cloud:

    storage_client = boto3.client('s3')

    def __init__(self, filename, bucket, path='../Test-models/'):
        self.bucket_name = bucket
        self.filename = filename
        self.path = os.path.abspath(path) + '/' +self.filename

    def upload(self):
        try:
            self.storage_client.upload_file(self.path, self.bucket_name, self.filename)
            print('Done')
        except Exception as ex:
            print('wtf s3')
            print(ex)



