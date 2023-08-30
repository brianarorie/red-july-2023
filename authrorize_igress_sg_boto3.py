# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the security group ID.
security_group_id = 'sg-0cbbe32ca4b5f411e'

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Authorize ingress (incoming) traffic to the specified security group
response = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,  # ID of the security group to modify
    IpPermissions=[  # List of IP permissions to add
        {
            'FromPort': 22,  # Allow incoming traffic on port 22 (SSH)
            'IpProtocol': 'tcp',  # TCP protocol
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',  # Allow all IP addresses (open to the world)
                },
            ],
            'ToPort': 22,  # Allow incoming traffic up to port 22
        },
        {
            'FromPort': 80,  # Allow incoming traffic on port 80 (HTTP)
            'IpProtocol': 'tcp',  # TCP protocol
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',  # Allow all IP addresses (open to the world)
                },
            ],
            'ToPort': 80,  # Allow incoming traffic up to port 80
        },
    ],
)

# Print the response from the authorization operation
print(response)
