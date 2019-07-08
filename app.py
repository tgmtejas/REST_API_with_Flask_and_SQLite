from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from item import Item, ItemList

from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)


# Data in/out path
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


# If app.py executed not imported, then only run
if __name__ == '__main__':
    app.run(port = 5000, debug=True)  # important to mention debug=True