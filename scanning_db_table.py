#Helps Me Interact With DynamoDB 
import boto3
#The Conditions Key Is Used To Scan For Items Related To The Key "title"
from boto3.dynamodb.conditions import Key, Attr
#Grabs The Specific Resource I Want To Use & Sets The Region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#The Name Of The Table
table = dynamodb.Table('Music')
#This Stores My Tables Actual Conditions That Will Be Filtered
fe = Key('title').begins_with('M')
#The Results From The Scan Based On The Filter Expression 
response = table.scan(
    FilterExpression=fe
) #The Response Is Stored In The Items Variable & Then Printed Out
items = response['Items']
print(items)

#The boto3.dynamodb.conditions.Key Is Used To Query Or Scan Based On The Primary
#Key Attributes. While The boto3.dynamodb.conditions.Attr Is Used To Scan Or Query
#Based On Non Key Attributes
#Scanning Uses The FilterExpression ONLY & Querying Uses The KeyCondtionExpression
# & The FilterExpression For More Specific Results
#The Condition & The Expression Values Have To Match