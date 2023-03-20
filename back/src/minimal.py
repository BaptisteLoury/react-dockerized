from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from model import sign_in_up as siu, user
import os

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}})
api = Api(app)


api.add_resource(siu.Authenticate, '/authenticate')
api.add_resource(siu.ExtAuth, '/authenticate-ext')
api.add_resource(siu.Register, '/register')
api.add_resource(user.User, '/user')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)