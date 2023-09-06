# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Delete a key pair using the specified key name.
response = ec2.delete_key_pair(
    KeyName='boto3 keys',  # Name of the key pair to delete
)

# Print the response after deleting the key pair
print(response)
