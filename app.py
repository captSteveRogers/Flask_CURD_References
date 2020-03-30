from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'ashu'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates a /auth endpoint which inturn after calling creates a jwt token

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':      # if the name is equal to  the run file... done to ensure that we need to to the below steps after executing the app only
    app.run(port=5000, debug=True)
