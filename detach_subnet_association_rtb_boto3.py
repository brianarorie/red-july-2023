# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define the ID of the route table to be modified
route_table_id = 'rtb-0f2bc90920ba6b0eb'

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Describe the specified route table to retrieve its associations
response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id,
    ],
)

# Iterate through associations of the route table
for association in response['RouteTables'][0]['Associations']:
    if not association['Main']:
        # Retrieve the ID of the association
        association_id = association['RouteTableAssociationId']
        
        # Print the ID of the association
        print(association_id)

        # Disassociate the route table from the subnet
        ec2.disassociate_route_table(
            AssociationId=association_id,
    )


