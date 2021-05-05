import json
import boto3
def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('awesome-birds')
    
    bird = table.get_item(Key={'id': event['pathParameters']['id']})
    
    return {
        'statusCode': 302,
        'headers': {
            'Location': bird["Item"]["imageUrl"]
        }
    }
