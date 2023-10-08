#My Project Creates A DynamoDB Table That Will Hold 10 Items About Music 
#I'm Using Boto3 To Interact With AWS Services
import boto3

#Getting The Service Resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#This Creates My DynamoDB Table
table = dynamodb.create_table(
    TableName='Music',
    KeySchema=[
        {
            'AttributeName':'year',
            'KeyType': 'HASH'#partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'#sort key 
        }
    ],
    AttributeDefinitions=[ #This Defines The Data Type Of The Partition & Sort Keys
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={ #This Defines The Allocated Input/Output Capacity
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
#This Part Of My Code Will Display The Results
print(table.item_count)

