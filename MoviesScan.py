#The scan method reads every item in the entire table and returns all the data in the table.
#You can provide an optional filter_expression so that only the items matching your criteria are returned. 
#However, the filter is applied only after the entire table has been scanned.
#The following program scans the entire Movies table, which contains approximately 5,000 items.
#The scan specifies the optional filter to retrieve only the movies from the 1950s (approximately 100 items) and discard all the others.

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

fe = Key('year').between(1950, 1959)
pe = "#yr, title, info.rating"
# Expression Attribute Names for Projection Expression only.
ean = { "#yr": "year", }
esk = None

response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean
    )

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

while 'LastEvaluatedKey' in response:
    response = table.scan(
        ProjectionExpression=pe,
        FilterExpression=fe,
        ExpressionAttributeNames= ean,
        ExclusiveStartKey=response['LastEvaluatedKey']
        )

    for i in response['Items']:
        print(json.dumps(i, cls=DecimalEncoder))

#ProjectionExpression specifies the attributes you want in the scan result.
#FilterExpression specifies a condition that returns only items that satisfy the condition. 
#All other items are discarded.
#The scan method returns a subset of the items each time, called a page. 
#The LastEvaluatedKey value in the response is then passed to the scan method via the ExclusiveStartKey parameter.
#When the last page is returned, LastEvaluatedKey is not part of the response.

#ExpressionAttributeNames provides name substitution.
#We use this because year is a reserved word in DynamoDB—you can't use it directly in any expression,
#including KeyConditionExpression. 
#You can use the expression attribute name #yr to address this. 
#ExpressionAttributeValues provides value substitution. 
#You use this because you can't use literals in any expression, including KeyConditionExpression.
#You can use the expression attribute value \:yyyy to address this.