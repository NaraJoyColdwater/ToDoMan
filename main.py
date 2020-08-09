import json

filename = 'mock.json'

with open(filename) as file:
    data = json.load(file)

def taskCreate(name):
    new = {'name': name, 'tags': []}
    data['tasks'].append(new)

def taskDelete(name):
    new = {'name': name, 'tags': []}
    data['tasks'].remove(new)

def taskRename(old, new):
    pass

def taskTagAdd(name):
    pass

def taskTagRemove(name):
    pass

def tagCreate(name):
    pass

def tagDelete(name):
    pass

def tagRename(old, new):
    pass

taskCreate('nntest')
for task in data['tasks']:
    print(task)
print()
taskDelete('nntest')
for task in data['tasks']:
    print(task)
