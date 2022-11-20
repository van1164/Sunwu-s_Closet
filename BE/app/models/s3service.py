import boto3
import logging
import os
from botocore.exceptions import ClientError
class s3service:
    def __init__(self):
        self.access_key = os.environ["ACCESS_KEY"]
        self.secret_key = os.environ["SECRET_KEY"]
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )
        self.bucket_name = "swfestcloset"
    def upload_file(self, file):
        # filename 테스트 후 이름 바꾸기
        try:
            res=self.client.upload_fileobj(file.read(),self.bucket_name,file.filename)
            print(res)
        except ClientError as e:
            logging.error("e")
            raise
        return res