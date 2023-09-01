# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the CIDR block for the subnet
cidr_block = '12.0.2.0/24'

# Define the ID of the VPC where the subnet will be created
vpc_id = 'vpc-0a11a920a7685f904'

<<<<<<< HEAD
# Create an EC2 client instance using boto3.
=======
# Create an EC2 client instance using boto3
>>>>>>> cf88ee0a63858174119b2ea0f4ce59326e091a88
ec2 = boto3.client('ec2')

# Create a subnet within the specified VPC and with the given CIDR block
subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

# Print the ID of the newly created subnet
print(subnet["Subnet"]["SubnetId"])
