import json
import boto3

def lambda_handler(event, context):
    filename = event['Records'][0]['s3']['object']['key']
    
    s3 = boto3.resource('s3')
    file = s3.Object('awesome-birds-bucket-test-1', filename).get()
    
    file_conent = json.load(file["Body"])

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('awesome-birds')

    for bird in file_conent:
        table.put_item(Item=bird)