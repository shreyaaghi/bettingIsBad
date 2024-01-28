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
    pass
# HOMEWORK

def deleteUser(id):
    pass