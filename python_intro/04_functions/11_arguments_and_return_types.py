penguin = {
  "id" : "1001",
  "name": "Penguin",
  "canFly": False
}

birds = [
  {
  "id" : "1001",
  "name": "Penguin",
  "canFly": False
  },
  {
    "id": "4004",
    "canFly": True,
    "name": "eagle"
  },
  {
    "id": "3003",
    "canFly": True,
    "name": ""
  },
  {
    "id": "2002",
    "canFly": None,
    "name": "albatross"
  }
]


def valid_attribute(bird_attribute):
  if bird_attribute is None:
    return False
  elif bird_attribute == "":
    return False
  else:
    return True

def validate_bird(bird):
  if (valid_attribute(bird["id"]) & 
      valid_attribute(bird["name"]) & 
      valid_attribute(bird["canFly"])):
    return f"valid bird object: {bird}"
  
  return f"invalid bird object: {bird}"
  
response = validate_bird(penguin)
print(response)

for bird in birds:
  response = validate_bird(bird)
  print(response)
