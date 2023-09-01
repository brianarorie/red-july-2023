# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the route table to be deleted
route_table_id = 'rtb-0e06a5967c8e6e56e'

<<<<<<< HEAD
# Create an EC2 client instance using boto3.
=======
# Create an EC2 client instance using boto3
>>>>>>> cf88ee0a63858174119b2ea0f4ce59326e091a88
ec2 = boto3.client('ec2')

# Delete the specified route table
ec2.delete_route_table(RouteTableId=route_table_id)