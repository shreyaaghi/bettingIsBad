from flask import Flask, request, Response

# app = Flask(__name__)



# @app.route('/')
# def index():
#     return 'Hello from Flask!'

# @app.route('/<name>')
# def get_name(name):
#     return f'hi {name}'

# @app.route('/add/<num1>/<num2>')
# def add(num1, num2):
#     num1 = int(num1)
#     num2 = int(num2)
#     return str(num1 + num2)

# @app.route('/multiply', methods=['POST'])
# def multiply():
#   keys=request.form
#   if "num1" not in keys or "num2" not in keys:
#     return Response('missing arguments', 400)
#   num1 = request.form['num1']
#   num2 = request.form['num2']
#   num1=int(num1)
#   num2=int(num2)
#   return str(num1 * num2)


# app.run(host='0.0.0.0', port=81)


# app.route("/{sport}/{type}/{location}/<team>")

# from util import writeToFile
# writeToFile('test.json', [{'username':'edward', 'password':'edward'}])

from util import createContents

createContents([{'username':'edward', 'password':'edward'}, {'username': 'shreya', 'password': 'shreya'}, {'username': 'allen', 'password': 'allen'}, {'username': 'tyler', 'password': 'tyler'}, {'username': 'aldo', 'password': 'aldo'}, {'username': 'arjun', 'password': 'arjun'}])