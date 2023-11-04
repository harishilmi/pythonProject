import json

with open('friends.json') as f:
    obj = json.load(f)

print(type(obj))
print(obj)