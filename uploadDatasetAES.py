import boto3

#access to the bucket
ACCESS_KEY=''
SECRET_KEY=''
SESSION_TOKEN=''

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, aws_session_token=SESSION_TOKEN)

fileUrl="predict.aes"

#upload file
filename= fileUrl
key=fileUrl
s3.meta.client.upload_file(filename, 'mybucket123456789123456879', key)
