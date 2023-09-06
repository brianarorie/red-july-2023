# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Describe instance types to retrieve information about available instance types
response = ec2.describe_instance_types(
    Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'true',
            ]
        },
]

)

# Access the list of instance types from the response.
instance_types = response['InstanceTypes']

# Loop through each instance type and print its name
for instance_type in instance_types:
    print(instance_type['InstanceType'],instance_type['FreeTierEligible'])

    