# Import the boto3 library, which provides an interface to interact with AWS services
import boto3
import os

# Define the name for the key pair
my_key_pair = 'boto3 keys'

# Define the file name for the private key file.
file_name = 'new-key-from-boto3.pem'

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Create a new key pair and retrieve the response
response = ec2.create_key_pair(
    KeyName=my_key_pair,
)

# Open the private key file in write mode and write the key material to it
with open(file_name, 'w') as f:
    f.write(response['KeyMaterial'])

# Change the permissions of the private key file to make it only readable by the owner
os.chmod(file_name, 0o400)
