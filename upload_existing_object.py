import boto3

s3 = boto3.client('s3')

with open("Testtext.txt" , 'rb') as f:
    s3.put_object(Bucket="brorie-boto3" , Key="Testtext.txt" , Body=f, ContentType="text/plain")