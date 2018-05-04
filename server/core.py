from flask import Flask, request
from cloud import S3_Object

server = Flask(__name__)

s3_access = S3_Object()

@app.route('/gimme', methods=['POST'])
def file_request_handle():
    data = request.json
    filename = data['filename']
    s3_access.download(filename)


def run_server():
    app.run(debug=True)
    