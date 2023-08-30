# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the VPC where the route table will be created
vpc_id = 'vpc-0a11a920a7685f904'

# Create an EC2 client instance using boto3.
ec2 = boto3.client('ec2')

# Create a route table within the specified VPC
route_table = ec2.create_route_table(VpcId=vpc_id)

# Print the ID of the newly created route table
print(route_table['RouteTable']['RouteTableId'])

