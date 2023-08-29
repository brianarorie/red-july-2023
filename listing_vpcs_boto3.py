# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define a function to get VPC information based on filters
def get_vpc_information(client, filter=[]):
    response = ec2.describe_vpcs(Filters=filter)
    for vpc in response['Vpcs']:
        # Print VPC information: VPC ID, CIDR block, and whether it's the default VPC
        print(vpc['VpcId'], vpc['CidrBlock'], vpc['IsDefault'])

# Define a function to get the name of a VPC based on filters
def get_vpc_name(client, filter=[]):
    response = ec2.describe_vpcs(Filters=filter)
    for vpc in response['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if 'Name' == tag['Key']:
                    # Print the value of the "Name" tag for the VPC
                    print(tag['Value'])

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Define filters for VPC description
Filters = [{'Name': 'isDefault', 'Values': ['true',]}]
