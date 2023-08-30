import boto3

ec2 = boto3.client('ec2')

def start_instance(client, instance_id):
    response = ec2.start_instances(
        InstanceIds=[
        instance_id,
        ],
    )
    
    print(instance_id, 'started')
    
    #.
