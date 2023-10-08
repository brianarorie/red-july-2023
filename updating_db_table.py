import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Music')

ue = 'SET age = :val1'
eav = ':val1: 24'
                 
response = table.update_item(
    Key={
        'artist': 'Halle'
    },
    UpdateExpression=ue,
    ExpressionAttributeValues=eav
)

print('Item Updated')

#This Is A Project I Started To Do To Learn It Is Not Complete Yet