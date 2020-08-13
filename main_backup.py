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

def taskCreate(name):
  if name in tasks:
    return False
  tasks[name] = []
  return True

def taskDelete(name):
  if name in tasks:
    tasks.pop(name)
    return True
  return False

def taskRename(old, new):
  if old in tasks and new not in tasks:
    tasks[new] = tasks[old]
    taskDelete(old)
    return True
  return False

def taskTagAdd(task, tag):
  if task in tasks and tag not in tasks[task] and tag in tags:
    tasks[task].append(tag)
    return True
  return False

def taskTagRemove(task, tag):
  if task in tasks and tag in tasks[task] and tag in tags:
    tasks[task].remove(tag)
    return True
  return False
      
def tagCreate(name):
  if name in tags:
    return False
  tags.append(name)
  return True

def tagDelete(name):
  if name in tags:
    tags.remove(name)
    for tagList in tasks.values():
      if name in tagList:
        tagList.remove(name)
    return True
  return False

def tagRename(old, new):
  if old in tags:
    tags.remove(old)
    tags.append(new)
    for tagList in tasks.values():
      if old in tagList:
        tagList.remove(old)
        tagList.append(new)
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
taskTagAdd('task 2', 'tag 1')
taskTagAdd('task 2', 'tag 3') # Nonexistent tag
taskTagAdd('task 5', 'tag 1') # Nonexistent task
print('3: ' + json.dumps(data))
taskRename('task 2', 'task 4')
print('4: ' + json.dumps(data))
taskTagAdd('task 4', 'tag 2')

# Tag editing:
tagRename('tag 1', 'tag 3')
print('5: ' + json.dumps(data))
tagDelete('tag 3')
print('6: ' + json.dumps(data))

# TODO : add file writing
try:
  with open(filename, 'wt') as file:
    json.dump(data, file, indent=4)
except IOError:
  print('Error: file ' + filename + ' not available for writing.')
  sys.exit(1)
sys.exit(0)