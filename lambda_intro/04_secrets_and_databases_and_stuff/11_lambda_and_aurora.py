import json

import boto3
rds_client = boto3.client('rds-data')

database_name = "serverlesstest"
db_cluster_arn = "cluster-arn-here"
db_credentials_secrets_arn = "credentials-secret-here"

def lambda_handler(event, context):
    
    sql = "select * from birds"

    response = rds_client.execute_statement(
        secretArn=db_credentials_secrets_arn,
        database=database_name,
        resourceArn=db_cluster_arn,
        sql=sql
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response["records"])
    }
