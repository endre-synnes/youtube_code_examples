import json

def lambda_handler(event, context):
    
    bird = json.loads(event["body"])
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Received a bird called {bird['name']}"})
    }
