from cloud import Cloud

if __name__ == '__main__':
    s3_agent = Cloud('mech-part.obj', 'impressar-files')
    s3_agent.upload()