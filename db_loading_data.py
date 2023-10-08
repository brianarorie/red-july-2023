#To Interact With DynamoDB
import boto3
#To Use The Resource
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
#The Name Of The Table I'm Loading The Items On
table = dynamodb.Table('Music')
#The Items
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'year': 2011,
            'title': 'Radio',
            'artist': 'Lana Del Ray',
            }
    )
    batch.put_item(
        Item={
            'year': 2023,
            'title': 'Angel',
            'artist': 'Halle',
            }
    )
    batch.put_item(
        Item={
            'year': 2020,
            'title': 'More Than Enough',
            'artist': 'Alina Baraz',
            }
    )
    batch.put_item(
        Item={
            'year': 2009,
            'title': 'Pursuit Of Happiness',
            'artist': 'Kid Cudi',
            }
    )
    batch.put_item(
        Item={
            'year': 2006,
            'title': 'Maneater',
            'artist': 'Nelly Furtado',
            }
    )
    batch.put_item(
        Item={
            'year': 2022,
            'title': 'Wrnkles',
            'artist': 'Lil Rocket',
            }
    )
    batch.put_item(
        Item={
            'year': 2019,
            'title': 'Feel Something',
            'artist': 'Bea Miller',
            }
    )
    batch.put_item(
        Item={
            'year': 2019,
            'title': 'Might Be Ready',
            'artist': 'V. Rose',
            }
    )
    batch.put_item(
        Item={
            'year': 2016,
            'title': 'Martinelli',
            'artist': 'Wordsplayed',
            }
    )
    batch.put_item(
        Item={
            'year': 2019,
            'title': 'Happy',
            'artist': 'Wande',
            }
    )