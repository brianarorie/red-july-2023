 # Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Describe security groups to retrieve information about security groups
response = ec2.describe_security_groups()

# Loop through each security group in the response
for sg in response['SecurityGroups']:
    # Print various security group information: Group ID, VPC ID, Group Name, and Description
    print(sg['GroupId'], sg['VpcId'], sg['GroupName'], sg['Description'])
    
    # Loop through each IP permission in the security group
    for permission in sg['IpPermissions']:
        # Check and print FromPort if available
        if 'FromPort' in permission:
            print(permission['FromPort'])

        # Check and print IP protocol if available
        if 'IpProtocol' in permission:
            print(permission['IpProtocol'])
        
        # Check and print ToPort if available
        if 'ToPort' in permission:
            print(permission['ToPort'])
            
        # Loop through IP ranges if available and print CIDR IP
        if 'IpRanges' in permission:
            for iprange in permission['IpRanges']:
                print(iprange['CidrIp'])
            
