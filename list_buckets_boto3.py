# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an S3 client instance using boto3
s3 = boto3.client('s3')

# List buckets to retrieve information about S3 buckets
response = s3.list_buckets()

# Access the list of buckets from the response
buckets = response['Buckets']

# Loop through each bucket in the list
for bucket in buckets:
    # Print the bucket name and its creation date
    print(bucket["Name"], bucket["CreationDate"])
