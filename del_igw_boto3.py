# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the Internet Gateway to be deleted
internet_gateway_id = 'igw-0d021e0f489d215f0'

<<<<<<< HEAD
# Create an EC2 client instance using boto3.
=======
# Create an EC2 client instance using boto3
>>>>>>> cf88ee0a63858174119b2ea0f4ce59326e091a88
ec2 = boto3.client('ec2')

# Delete the specified Internet Gateway
ec2.delete_internet_gateway(InternetGatewayId=internet_gateway_id)