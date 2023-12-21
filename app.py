from flask import Flask, request, Response
from auth import signup

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/signup', methods=['POST'])
def signup_route():
    return signup()

def run():
    app.run(host='0.0.0.0', port=81)

