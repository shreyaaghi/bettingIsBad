from flask import Flask, request, Response
from auth import signup, login
from userProfile import createUser, getUser, updateUser, deleteUser

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

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
def user_routes(id):
    if request.method == 'GET':
        return getUser(id)
    
    elif request.method == 'PUT':
        data = {}
        username = request.form.get('username')
        if username is not None:
            data['username'] = username

        userPhoto = request.form.get('userPhoto')
        if userPhoto is not None:
            data['userPhoto'] = userPhoto

        userBio = request.form.get('userBio')
        if userBio is not None:
            data['userBio'] = userBio

        return updateUser(id, data)   
    
    elif request.method == 'DELETE':
        return deleteUser(id)
 

def run():
    app.run(host='0.0.0.0', port=81)

