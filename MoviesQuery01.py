#Queries All Movies Released In A Year

import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

print("Movies from 1985")

response = table.query(
    KeyConditionExpression=Key('year').eq(1985)
)

for i in response['Items']:
    print(i['year'], ":", i['title'])

#The Boto 3 SDK constructs a ConditionExpression for you when you use the Key and Attr functions imported from boto3.dynamodb.conditions.
#You can also specify a ConditionExpression as a string. 
#The preceding program shows how to query a table by its primary key attributes.
#In DynamoDB, you can optionally create one or more secondary indexes on a table and query those indexes in the same way that you query a table. 
#Secondary indexes give your applications additional flexibility by allowing queries on non-key attributes