from flask import Flask, request, Response
from auth import signup
from auth import login

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

def run():
    app.run(host='0.0.0.0', port=81)

