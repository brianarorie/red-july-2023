import boto3

ec2 = boto3.client('ec2')

def terminate_instance(client, instance_id):
    response = ec2.terminate_instances(
        InstanceIds=[
        instance_id,
        ],
    )
    
    print(instance_id, 'terminated')
    
    #.
