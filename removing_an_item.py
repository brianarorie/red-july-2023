import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Music')

response =table.delete_item(
        Key={
        'title': 'More Than Enough',
        'year': 2020
        }
    )
    
print("Item Deleted",response)    
    