import boto3

#access to the bucket
BUCKET_NAME=''
ACCESS_KEY=''
SECRET_KEY=''
SESSION_TOKEN='

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, aws_session_token=SESSION_TOKEN)

key="dataset.aes"

#download file
try:
    s3.Bucket(BUCKET_NAME).download_file(key, key)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
