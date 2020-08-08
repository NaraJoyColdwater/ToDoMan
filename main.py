import json

with open('mock.json') as file:
    data = json.load(file)
    for task in data['tasks']:
        print(task['name'])

def taskCreate(name):
    pass

def taskDelete(name):
    pass

def taskRename(name):
    pass

def taskTagAdd(name):
    pass

def taskTagRemove(name):
    pass

def tagCreate(name):
    pass

def tagDelete(name):
    pass

def tagRename(name):
    pass
