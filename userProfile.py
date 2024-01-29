from util import readFile, writeToJson
from flask import Response

def getUser(id):
    profiles = readFile('profiles.json', {})
    return profiles.get(id)

def createUser(id, username, userPhoto, userBio):
    newUser = {'username':username, 
            'userPhoto':userPhoto, 
            'userBio':userBio}
    user = getUser(id)
    if user is not None:
        return Response('User already exists', 409)
    profiles = readFile('profiles.json', {})
    profiles.update({id:newUser})
    writeToJson('profiles.json', profiles)
    return "New user created"

def updateUser(id, data):
    user = getUser(id)
    if user is None:
        return Response("User not found", 404)
    for key, value in data.items():
        user[key] = value
    profiles = readFile('profiles.json', {})
    profiles.update({id:user})
    writeToJson('profiles.json', profiles)
    return "User updated"

def deleteUser(id):
    user = getUser(id)
    if user is None:
        return Response("User not found", 404)
    profiles = readFile('profiles.json', {})
    del profiles[id]
    writeToJson('profiles.json', profiles)
    return 'User deleted'
    
  
# implement delete