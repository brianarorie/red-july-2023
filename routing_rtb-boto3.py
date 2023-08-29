# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the route table and the ID of the Internet Gateway for the route
route_table_id = 'rtb-0f2bc90920ba6b0eb'
internet_gateway_id = 'igw-0d021e0f489d215f0'

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Create a route in the specified route table to route traffic to the Internet Gateway
ec2.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway_id, RouteTableId=route_table_id)
