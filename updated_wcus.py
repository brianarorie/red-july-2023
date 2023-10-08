import boto3

dynamodb = boto3.client('dynamodb')

table_name = 'Music'

new_wcu = 10
new_rcu = 10

response = dynamodb.update_table(
   TableName=table_name,
   ProvisionedThroughput={
     'WriteCapacityUnits':new_wcu,
     'ReadCapacityUnits':new_rcu    
   }
    
)


print(response)