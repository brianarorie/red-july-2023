import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Specify the table name and item attributes, including the new attribute
table_name = 'Music'
item_attributes = {
    'year': {'N': '2023'},
    'artist': {'S': 'Lana Del Ray'}
}

# Put the new item into the DynamoDB table
dynamodb.put_item(
    TableName=table_name,
    Item=item_attributes
)
