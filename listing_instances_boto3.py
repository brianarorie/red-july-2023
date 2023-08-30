# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Describe instances to retrieve information about running instances
response = ec2.describe_instances()

# Loop through each reservation containing instances.
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        # Print various instance information: Instance ID, Type, Image ID, VPC ID, Subnet ID, and State
        print(
            instance['InstanceId'],
            instance['InstanceType'],
            instance['ImageId'],
            instance['VpcId'],
            instance['SubnetId'],
            instance['State']['Name']
        )

        # Check if instance has tags and print the instance's "Name" tag value
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    print(tag['Value'])

        # Print each security group ID associated with the instance
        for sg in instance['SecurityGroups']:
            print(sg['GroupId'])

        # Print the public IP address if available
        if 'PublicIpAddress' in instance:
            print(instance['PublicIpAddress'])

        # Print the key name used to launch the instance
        if 'KeyName' in instance:
            print(instance['KeyName'])

        # Print the instance profile ID and ARN if an instance profile is associated
        if 'IamInstanceProfile' in instance:
            print(instance['IamInstanceProfile']['Id'], instance['IamInstanceProfile']['Arn'])
        
        
        