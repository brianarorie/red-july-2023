#Importing Boto3 To Interact With AWS Resources
import boto3
#This Specifies The Resource
dynamodb = boto3.client('dynamodb')
#This Specifies The Table I Want To Delete
table_name = 'Music'
#This Deletes The DynamoDB Table
response = dynamodb.delete_table(TableName=table_name)
#This Prints Out The Results
print("Table deletion response:", response)
