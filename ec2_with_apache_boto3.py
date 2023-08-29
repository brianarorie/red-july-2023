# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define a function to create an EC2 instance with the provided parameters
def create_instance(client, ami_id, security_group, key_pair_id, user_data=None):
    # Run an EC2 instance with the specified parameters
    response = client.run_instances(
        ImageId=ami_id,  # ID of the Amazon Machine Image (AMI) to use
        InstanceType='t2.micro',  # Instance type (size)
        KeyName=key_pair_id,  # Name of the key pair to use for SSH access
        MaxCount=1,  # Number of instances to launch (maximum)
        MinCount=1,  # Number of instances to launch (minimum)
        SecurityGroupIds=[
            security_group,  # List of security group IDs to associate with the instance
        ],
        UserData=user_data  # User data script to run when the instance starts
    )

    # Print the ID of the newly launched instance
    print(response['Instances'][0]['InstanceId'])

# Define the AMI ID, key pair ID, security group ID, and user data script
ami_id = 'ami-09e67e426f25ce0d7'
key_pair_id = 'boto3 keys'
security_group = 'sg-0cbbe32ca4b5f411e'

user_data = '''#!/bin/bash
apt update -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Call the create_instance function to launch an instance with the provided parameters
create_instance(ec2, ami_id, security_group, key_pair_id, user_data)
