import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("sqs")
    response = client.send_message(
        QueueUrl="QUEUE_URL", 
        MessageBody=json.dumps(event["body"])
    )

    print(response)
    
    return {
        'statusCode': response["ResponseMetadata"]["HTTPStatusCode"],
        'body': json.dumps(response["ResponseMetadata"])
    }
