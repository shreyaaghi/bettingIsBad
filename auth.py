from flask import request, Response
from util import readFile, writeToFile
import bcrypt
def signup():
  username = request.form['username']
  password = request.form['password']
  hashed = bcrypt.hashpw(b"{password}", bcrypt.gensalt())
  # FIXME; use actual password and not the string password as a byte
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