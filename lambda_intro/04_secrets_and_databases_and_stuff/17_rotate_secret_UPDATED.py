import json
import boto3

def lambda_handler(event, context):
    arn = event["SecretId"]
    token = event["ClientRequestToken"]
    step = event["Step"]
    
    client = boto3.client("secretsmanager")
    
    metadata = client.describe_secret(SecretId=arn)

    if not metadata["RotationEnabled"]:
        raise ValueError(f"Secret {arn} is not enabled for rotation")
        
    print(f"step: {step}")
    
    if step == "createSecret":
        createSecret(client, arn, token)
    
    elif step == "setSecret":
        setSecret(client, arn, token)
        
    elif step == "testSecret":
        testSecret(client, arn, token)
        
    elif step == "finishSecret":
        finishSecret(client, arn, token)
        
    else:
        raise ValueError("Invalid step parameter")


def createSecret(client, arn, token):
    client.get_secret_value(SecretId=arn, VersionStage="AWSCURRENT")
    
    try:
        client.get_secret_value(SecretId=arn, VersionId=token, VersionStage="AWSPENDING")
    except client.exceptions.ResourceNotFoundException:
        password = client.get_random_password(ExcludeCharacters='/@"\'\\')
        client.put_secret_value(SecretId=arn, ClientRequestToken=token, SecretString=json.dumps({"api-key": password["RandomPassword"]}), VersionStages=["AWSPENDING"])
    
def setSecret(client, arn, token):
    print("No database credentials to update...")
    
def testSecret(client, arn, token):
    print("No need for testing against any service...")

def finishSecret(client, arn, token):
    metadata = client.describe_secret(SecretId=arn)
    
    for version in metadata["VersionIdsToStages"]:
        if "AWSCURRENT" in metadata["VersionIdsToStages"][version]:
            if version == token:
                return
            
            client.update_secret_version_stage(SecretId=arn, VersionStage="AWSCURRENT", MoveToVersionId=token, RemoveFromVersionId=version)
            break
