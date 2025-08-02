import json
import boto3

s3_client = boto3.client("s3")

def lambda_handler(event, context):
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  file_name = event['Records'][0]['s3']['object']['key']

  sign_params = {"Bucket": bucket_name, "Key": file_name}
  expires_in = 129600  # 36 hours
  signed_url = s3_client.generate_presigned_url('get_object', Params=sign_params, ExpiresIn=expires_in)
  print(signed_url)
