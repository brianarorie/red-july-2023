# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the VPC and the ID of the Internet Gateway for detachment
vpc_id = 'vpc-0a11a920a7685f904'
internet_gateway_id = 'igw-0d021e0f489d215f0'

<<<<<<< HEAD
# Create an EC2 client instance using boto3.
=======
# Create an EC2 client instance using boto3
>>>>>>> cf88ee0a63858174119b2ea0f4ce59326e091a88
ec2 = boto3.client('ec2')

# Detach the specified Internet Gateway from the specified VPC
ec2.detach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)

