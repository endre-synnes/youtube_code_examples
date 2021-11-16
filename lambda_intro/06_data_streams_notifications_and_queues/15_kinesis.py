import base64
import json
import boto3

def lambda_handler(event, context):
  for record in event['Records']:
    #Kinesis data is base64 encoded so decode here
    payload=base64.b64decode(record["kinesis"]["data"])
    res = json.loads(payload)
  
    write_to_db(res)
    print("Object successfully stored in DB.")
       
def write_to_db(data):
  dynamodb = boto3.resource('dynamodb', region_name="eu-central-1")
  table = dynamodb.Table("endres-test")

  table.put_item(
      Item=data
  )
