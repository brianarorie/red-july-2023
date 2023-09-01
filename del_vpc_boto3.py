# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the VPC to be deleted
vpc_id = 'vpc-0a11a920a7685f904'

<<<<<<< HEAD
# Create an EC2 client instance using boto3.
=======
# Create an EC2 client instance using boto3
>>>>>>> cf88ee0a63858174119b2ea0f4ce59326e091a88
ec2 = boto3.client('ec2')

# Delete the specified VPC
ec2.delete_vpc(VpcId=vpc_id)