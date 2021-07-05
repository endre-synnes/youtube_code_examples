import json
import boto3
import os

TABLE_NAME = os.environ["TABLE_NAME"]

def lambda_handler(event, context):
  
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(TABLE_NAME)
  
  response = table.get_item(Key={'id': event["pathParameters"]["id"]})

  return {
    'statusCode': 200,
    'body': json.dumps(response['Item'])
  }
