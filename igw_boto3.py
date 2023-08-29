# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Create an Internet Gateway (IGW)
igw = ec2.create_internet_gateway()

# Print the ID of the newly created Internet Gateway
print(igw['InternetGateway']['InternetGatewayId'])