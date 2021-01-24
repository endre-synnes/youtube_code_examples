import boto3
import os

table_name = os.environ['TABLE_NAME']
region = os.environ['REGION']


def lambda_handler(event, context):
    print(f"Event: {event}")
    write_to_db(event["data"])


def write_to_db(data):
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(table_name)

    table.put_item(
        TableName=table_name,
        Item=data
    )
