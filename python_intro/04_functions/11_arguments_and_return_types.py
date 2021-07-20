
def hello(name):
  return f"Hello {name}"


response = hello("Eagle")
print(response)
print(type(response))


penguin = {
  "id" : "1001",
  "name": "Penguin",
  "canFly": False
}


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
    return "Valid bird :D"
  
  return "Invalid bird"
  
response = validate_bird(penguin)
print(response)
