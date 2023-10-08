#To Interact With DynamoDb
import boto3
#To Set my Conditions
from boto3.dynamodb.conditions import Key, Attr
#This Sets The Resource I Want To Use & The Region 
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#This Is The Table I Want To Query
table = dynamodb.Table('Music')
# The Key & Attributes I Want To Use As Conditions
ke = Key('year').eq(2023)
fe = Attr('artist').eq('Halle')
#The Variable Holding The Condition Variables
response = table.query(
    KeyConditionExpression=ke,
    FilterExpression=fe
) #The Variable Holding The Response Results
items = response['Items']
print(items)


