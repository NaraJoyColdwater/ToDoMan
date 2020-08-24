import json

filename = 'data.json'

def deserialize(filename: str) -> bool:
    try:
        with open(filename, 'rt') as file:
            data = json.load(file)
    except IOError:
        print('deserialize(): ' + filename + ' not available for reading.')
        return False
    global tasks
    tasks = data['tasks']
    global tags
    tags = data['tags']
    return True

def serialize(filename: str) -> bool:
    try:
        with open(filename, 'wt') as file:
            json.dump(data, file, indent=2)
    except IOError:
        print('serialize(): ' + filename + ' not available for writing.')
        return False
    return True

def tagCreate(name: str) -> bool:
    if name in tags:
        return False
    tags[name] = []
    return True

def tagDelete(name: str) -> bool:
    if name in tags:
        tags.pop(name)
        return True
    return False

def tagRename(old: str, new: str) -> bool:
    if old in tags and new not in tags:
        tags[new] = tags[old]
        tagDelete(old)
        return True
    return False

def tagTaskAdd(task: str, tag: str) -> bool:
    if tag in tags and task not in tags[tag] and task in tasks:
        tags[tag].append(task)
        return True
    return False

def tagTaskRemove(task: str, tag: str) -> bool:
    if tag in tags and task in tags[tag] and task in tasks:
        tags[tag].remove(task)
        return True
    return False

def taskCreate(name: str) -> bool:
    if name in tasks:
        return False
    tasks.append(name)
    return True

def taskDelete(name: str) -> bool:
    if name in tasks:
        tasks.remove(name)
        for taskList in tags.values():
            if name in taskList:
                taskList.remove(name)
        return True
    return False

def taskRename(old: str, new: str) -> bool:
    if old in tasks and new not in tasks:
        tasks.remove(old)
        tasks.append(new)
        for taskList in tags.values():
            if old in taskList:
                taskList.remove(old)
                taskList.append(new)
        return True
    return False

def taskSwitchWithinTag(first: str, second: str, tag: str) -> bool:
    if tag not in tags or first not in tags[tag] or second not in tags[tag]:
        return False
    taskList = tags[tag]
    firstIndex = taskList.index(first)
    secondIndex = taskList.index(second)
    taskList[firstIndex], taskList[secondIndex] = taskList[secondIndex], taskList[firstIndex]
    return True
