import json
import boto3
import urllib3

REGION = "eu-central-1"
SECRET_NAME = "lambda-authorizer-api-key"
API_URL = "https://z785cwhbu3.execute-api.eu-central-1.amazonaws.com/demo/birds"
BIRD_ID = "079b42b8-a1ab-11eb-bcbc-0242ac130002"

def lambda_handler(event, context):
  
  http = urllib3.PoolManager()
  api_key = get_api_key()
  response = http.request('GET', f"{API_URL}/{BIRD_ID}", headers=api_key)

  if response.status != 200:
    return {
      "statusCode": response.status,
      "errorMessage": "Could not retreive data"
    }
  

  return {
        'statusCode': 200,
        'body': response.data.decode('utf8')
    }


def get_api_key():
  session = boto3.session.Session()
  client = session.client(
      service_name='secretsmanager',
      region_name=REGION
  )
  get_secret_value_response = client.get_secret_value(
      SecretId=SECRET_NAME
  )
  secrets_response = get_secret_value_response['SecretString']

  return json.loads(secrets_response)
  