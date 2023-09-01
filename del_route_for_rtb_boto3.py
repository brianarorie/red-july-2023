import boto3

route_table_id = 'rtb-0f2bc90920ba6b0eb'

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id)
<<<<<<< HEAD
    
    .
=======
>>>>>>> cf88ee0a63858174119b2ea0f4ce59326e091a88

