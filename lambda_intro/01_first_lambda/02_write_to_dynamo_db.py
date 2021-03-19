import boto3

TABLE_NAME = "birds"
REGION = "eu-central-1"


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name=REGION)
    table = dynamodb.Table(TABLE_NAME)

    table.put_item(
        Item=event
    )


    # Extra
    response = table.get_item(Key={'id': event["id"]})
    return response["Item"]
