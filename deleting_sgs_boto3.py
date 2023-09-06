import boto3

security_group = 'sg-0cbbe32ca4b5f411e'

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId=security_group,
)

print(response)

.
