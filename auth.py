from flask import request, Response
from util import readFile, writeToFile
import bcrypt
import jwt
import uuid
import os
from datetime import datetime, timezone, timedelta


def encode(user):
   return jwt.encode({'user_id': user.get('id'), "iat": datetime.now(tz=timezone.utc), 'exp': datetime.now(tz=timezone.utc)+timedelta(seconds=30)}, os.environ.get("JWT_SECRET"),  algorithm='HS256')

def signup():
  id = uuid.uuid4()
  username = request.form['username']
  password = request.form['password'].encode('utf-8') 
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  # FIXME; use actual password and not the string password as a byte
  newUser = {'id': str(id), 'username':username, 'password':hashed.decode('utf-8')}
  users = readFile('users.json')
  for user in users:
    if user.get('username') == username:
      return Response('User already exists', 409)
  users.append(newUser)
  writeToFile('users.json', users)
  token = encode(newUser)
  return Response(token, 200)
# return jwt later (WHAT IS JWT)

def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')  # Convert to bytes
    users = readFile('users.json')
    user_found = None
    for user in users:
        if user.get('username') == username:
            user_found = user
            break
    if user_found is None:
      return Response('User not found', 404) 
    else:
      hashed_password = user_found.get('password').encode('utf-8')
        #retrieves the stored hashed password
      if bcrypt.checkpw(password, hashed_password):
        token = encode(user)
        return Response(token, 200)
      else:
        return Response('Incorrect password', 401)
      

# HOMEWORK: encode the signup with jwt