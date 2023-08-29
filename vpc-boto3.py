# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Create a VPC (Virtual Private Cloud) in AWS with the specified CIDR block
vpc = ec2.create_vpc(CidrBlock='12.0.2.0/24')

# Print the VPC ID of the newly created VPC
print(vpc['Vpc']['VpcId'])
