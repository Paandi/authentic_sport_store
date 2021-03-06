from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from Resource.User import UserRegister
from Resource.Item import Items, ItemAll
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db').replace('postgres:', 'postgresql:')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'SportsStore'
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(ItemAll, '/allitems')
api.add_resource(UserRegister, '/signup')
api.add_resource(Items, '/item/<string:name>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
