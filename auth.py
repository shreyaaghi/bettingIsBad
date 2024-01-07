from flask import request, Response
from util import readFile, writeToFile
import bcrypt
def signup():
  username = request.form['username']
  password = request.form['password']
  hashed = bcrypt.hashpw(b"{password}", bcrypt.gensalt())
  # FIXME; use actual password and not the string password as a byte DID I FIX THIS
  newUser = {'username':username, 'password':hashed}
  users = readFile('users.json')
  for user in users:
    if user.get('username') == username:
      return Response('User already exists', 409)
  users.append(newUser)
  writeToFile('users.json', users)
  return str(newUser)
# return jwt later (WHAT IS JWT)
# how to do login?

def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')  # Convert to bytes

    users = readFile('users.json')
    user_found = None
    for user in users:
        if user.get('username') == username:
            user_found = user
            break

    if user_found:
        hashed_password = user_found.get('password').encode('utf-8') 
        #retrieves the stored hashed password
        if bcrypt.checkpw(password, hashed_password):
            return Response('Login successful', 200)
        else:
            return Response('Incorrect password', 401)
    else:
        return Response('User not found', 404)
