from flask import request, Response
from util import readFile, writeToFile
import bcrypt
import jwt

def signup():
  username = request.form['username']
  password = request.form['password'].encode('utf-8') 
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  # FIXME; use actual password and not the string password as a byte DID I FIX THIS
  newUser = {'username':username, 'password':hashed.decode('utf-8')}
  users = readFile('users.json')
  for user in users:
    if user.get('username') == username:
      return Response('User already exists', 409)
  users.append(newUser)
  writeToFile('users.json', users)
  return str(newUser)
  if bcrypt.checkpw():
    token = jwt.encode({'user_id': newUser.get('id')}, algorithm='HS256')
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
        token = jwt.encode({'user':user_found},'jwt/secret', algorithm = 'HS256')
        return Response(token, 200)
      else:
        return Response('Incorrect password', 401)
      

# HOMEWORK: encode the signup with jwt