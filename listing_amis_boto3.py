# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3.
ec2 = boto3.client('ec2')

# Describe images owned by 'amazon' to retrieve information about Amazon Machine Images (AMIs)
response = ec2.describe_images(Owners=['self'])

# Loop through each image in the response
for image in response['Images']:
    # Print various image information: Image ID, Creation Date, and Name
    print(
        image['ImageId'],
        image['CreationDate'],
        image['Name']
    )

