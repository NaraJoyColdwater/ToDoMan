import json
import sys

filename = 'data.json'

try:
  with open(filename, 'rt') as file:
    data = json.load(file)
except IOError:
  print('Error: file ' + filename + 'not available for reading.')
  sys.exit(1)
tasks = data['tasks']
tags = data['tags']

def tagCreate(name):
  if name in tags:
    return False
  tags[name] = []
  return True

def tagDelete(name):
  if name in tags:
    tags.pop(name)
    return True
  return False

def tagRename(old, new):
  if old in tags and new not in tags:
    tags[new] = tags[old]
    tagDelete(old)
    return True
  return False

def tagTaskAdd(task, tag):
  if tag in tags and task not in tags[tag] and task in tasks:
    tags[tag].append(task)
    return True
  return False

def tagTaskRemove(task, tag):
  if tag in tags and task in tags[tag] and task in tasks:
    tags[tag].remove(task)
    return True
  return False
      
def taskCreate(name):
  if name in tasks:
    return False
  tasks.append(name)
  return True

def taskDelete(name):
  if name in tasks:
    tasks.remove(name)
    for taskList in tags.values():
      if name in taskList:
        taskList.remove(name)
    return True
  return False

def taskRename(old, new):
  if old in tasks and new not in tasks:
    tasks.remove(old)
    tasks.append(new)
    for taskList in tags.values():
      if old in taskList:
        taskList.remove(old)
        taskList.append(new)
    return True
  return False


# Testing

# Tasks:
taskCreate('task 1')
taskCreate('task 2')
taskCreate('task 1') # Duplicate task
taskRename('task 1', 'task 3')
taskCreate('task 1') # Recently deleted task
print('1: ' + json.dumps(tasks))
taskDelete('task 3')
print('2: ' + json.dumps(tasks))

# Tag creation:
tagCreate('tag 1')
tagCreate('tag 2')
tagCreate('tag 1') # Duplicate tag

# Interaction:
tagTaskAdd('task 2', 'tag 1')
tagTaskAdd('task 2', 'tag 3') # Nonexistent tag
tagTaskAdd('task 5', 'tag 1') # Nonexistent task
print('3: ' + json.dumps(data))
taskRename('task 2', 'task 4')
print('4: ' + json.dumps(data))
tagTaskAdd('task 4', 'tag 2')

# Tag editing:
tagRename('tag 1', 'tag 3')
print('5: ' + json.dumps(data))
tagDelete('tag 3')
print('6: ' + json.dumps(data))
tagCreate('tag 69')
taskCreate('nice')
tagTaskAdd('nice', 'tag 69')
# TODO : add file writing
try:
  with open(filename, 'wt') as file:
    json.dump(data, file, indent=2)
except IOError:
  print('Error: file ' + filename + ' not available for writing.')
  sys.exit(1)
sys.exit(0)