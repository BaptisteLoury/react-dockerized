from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from model import sign_in_up as siu, user
import os

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(siu.Authenticate, '/authenticate')
api.add_resource(siu.ExtAuth, '/authenticate-ext')
api.add_resource(siu.Register, '/register')
api.add_resource(user.User, '/user')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)