from flask import Flask, request, Response
from auth import signup, login
from userProfile import createUser, getUser

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/signup', methods=['POST'])
def signup_route():
    return signup()

@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/user', methods=['POST'])
def createUser_route():
    id = request.form['id']
    username = request.form['username']
    # userPhoto = request.form['userPhoto']
    userBio = request.form['userBio']
    print(request.form)
    return createUser(id, username, None, userBio)

@app.route('/user/<id>')
def getUser_route(id):
    return getUser(id)

    

def run():
    app.run(host='0.0.0.0', port=81)

