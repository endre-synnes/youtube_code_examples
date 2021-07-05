import json
import boto3

def lambda_handler(event, context):
    
    bird = json.loads(event["body"])

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('awesome-birds')

    table.put_item(Item=bird)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"{bird['name']} stored in DB"})
    }
