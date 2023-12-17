from flask import request, Response
# import bcrypt
def signup():
  username = request.form['username']
  password = request.form['password']
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())