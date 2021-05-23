import json

BIRDS = [
  {
    "id": "123abc",
    "name": "eagle"
  },
  {
    "id": "321def",
    "name": "penguin"
  }
]

def lambda_handler(event, context):
  
  bird_id = json.loads(event["pathParameters"]["id"])

  for bird in BIRDS:
    if bird["id"] == bird_id:
      return {
          "statusCode": 200,
          "body": json.dumps({"message": f"Received a bird called {bird['name']}"})
      }
  

  return {"statusCode": 404}
