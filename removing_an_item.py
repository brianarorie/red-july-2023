#This Is To Interact With The AWS Resource
import boto3
#Specifies The Resources Being Utilized
dynamodb = boto3.resource('dynamodb')
#This Specifies The Table I Want To Delete The Item From
table = dynamodb.Table('Music')
#This Stores The Primary Key,Sort Key & Values That Determine Which Items to Delete
response =table.delete_item(
        Key={
        'title': 'More Than Enough',
        'year': 2020
        }
    )
#Prints Out The Response Upon Successful Deletion    
print("Item Deleted",response)    
    
    
    