# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Create a new security group
response = ec2.create_security_group(
    Description='boto3 security group',  # Description of the security group
    GroupName='boto3 sg',  # Name of the security group
    VpcId='vpc-05a6ffcfdb9a2e04d',  # ID of the VPC where the security group will be created
)

# Print the ID of the newly created security group
print(response['GroupId'])

