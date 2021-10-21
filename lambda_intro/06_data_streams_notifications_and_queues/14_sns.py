import json
import boto3

def lambda_handler(event, context):

  write_to_db(event)

  client = boto3.client("sns")

  response = client.publish(
    TopicArn='string',
    Message=json.dumps({
      "event": "newBird",
      "birdName": event["birdName"]
    })
  )
  
  return {
    'statusCode': 200,
    'body': json.dumps(response)
  }


def write_to_db(data):
  dynamodb = boto3.resource('dynamodb', region_name="eu-central-1")
  table = dynamodb.Table("birds")

  table.put_item(
      Item=data
  )
