# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

<<<<<<< HEAD
# Create an EC2 client instance using boto3.
=======
# Create an EC2 client instance using boto3
>>>>>>> cf88ee0a63858174119b2ea0f4ce59326e091a88
ec2 = boto3.client('ec2')

# Create a VPC (Virtual Private Cloud) in AWS with the specified CIDR block
vpc = ec2.create_vpc(CidrBlock='12.0.2.0/24')

# Print the VPC ID of the newly created VPC
print(vpc['Vpc']['VpcId'])
