import os
import boto3

class S3_Object:

    storage_client = boto3.client('s3')

    def __init__(self, bucket='impressar-files'):
        self.bucket_name = bucket

    def upload(self, filename, path):
        try:
            path = os.path.abspath(path)
            self.storage_client.upload_file(path + '/' + filename, self.bucket_name, filename)
            print('Done')
        except Exception as ex:
            print('wtf s3')
            print(ex)

    def download(self, filename):
        try:
            self.storage_client.download_file(filename, self.bucket_name, filename)
            print('Downloaded at the home directory')
        except Exception as ex:
            print('wtf s3')
            print(ex)



