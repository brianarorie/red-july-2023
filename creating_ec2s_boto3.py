# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the AMI ID, key pair ID, and security group ID
ami_id = 'ami-08d701b1d715c35f9'
key_pair_id = 'boto3 keys'
security_group = 'sg-0cbbe32ca4b5f411e'

# Create an EC2 client instance using boto3.
ec2 = boto3.client('ec2')

# Run an EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,  # ID of the Amazon Machine Image (AMI) to use
    InstanceType='t2.micro',  # Instance type (size)
    KeyName=key_pair_id,  # Name of the key pair to use for SSH access
    MaxCount=1,  # Number of instances to launch (maximum)
    MinCount=1,  # Number of instances to launch (minimum)
    SecurityGroupIds=[
        security_group,  # List of security group IDs to associate with the instance
    ],
)

# Print the ID of the newly launched instance
print(response['Instances'][0]['InstanceId'])