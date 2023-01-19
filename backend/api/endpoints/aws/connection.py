import boto3
from .aws_key import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
# 해당 모듈은 버켓 보안을 위해 .gitignore 에 추가되어 있습니다. 추가 문의는 팀 리더에게 해주세요.
AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY #임시구동용

class Connect:
    def __init__(self):
        self.client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

    def __enter__(self):
        return self 

    def connect(self):
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...