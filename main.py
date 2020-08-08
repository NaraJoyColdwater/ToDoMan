import json

with open('mock.json') as file:
    data = json.load(file)
    for task in data['tasks']:
        print(task['name'])

