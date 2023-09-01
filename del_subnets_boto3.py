# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the subnet to be deleted
subnet_id = 'subnet-064802d15c9fe01aa'

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Delete the specified subnet
ec2.delete_subnet(SubnetId=subnet_id)
