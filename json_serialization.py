import json

friends = {'Dan': [20, 'London', 123600210], 'Maria': [24, 'Madrid', 133940753]}

# print(friends)

with open('friends.json', 'w') as f:
    # f.write(friends)
    json.dump(friends, f, indent=4)


print(json.dumps(friends, indent=4))
print(type(json.dumps(friends)))