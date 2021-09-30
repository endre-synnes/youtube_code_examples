# https://4rw1tg6md2.execute-api.eu-central-1.amazonaws.com

import boto3

def lambda_handler(event, context):

    client = boto3.client('ssm')
    response = client.get_parameter(Name='external-api-url')
    
    
    return {
        'statusCode': 200,
        'body': response['Parameter']['Value']
    }
