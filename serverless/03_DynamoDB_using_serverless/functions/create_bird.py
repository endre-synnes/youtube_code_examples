import json
import boto3
import os

TABLE_NAME = os.environ["TABLE_NAME"]

def lambda_handler(event, context):
    
    bird = json.loads(event["body"])

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    table.put_item(Item=bird)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"{bird['name']} stored in DB"})
    }
