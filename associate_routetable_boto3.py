# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the route table and the subnet for association
route_table_id = 'rtb-0f2bc90920ba6b0eb'
subnet_id = 'subnet-064802d15c9fe01aa'

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Associate the specified route table with the specified subnet
association = ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)

# Print the ID of the association
print(association['AssociationId'])

