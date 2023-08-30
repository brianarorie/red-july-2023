# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3.
ec2 = boto3.client('ec2')

# Create an image (snapshot) of a specific EC2 instance
response = ec2.create_image(
    InstanceId='i-032f4a7941029e9d8',  # Specify the ID of the instance to create an image from
    Name='my insta',  # Specify a name for the created image
)

# Print the ID of the newly created image
print(response['ImageId'])
