from flask import Flask
from flask_restful import Api

from resources.user import User, Users
# from resources.item import Item, ItemList
from resources.role import Role, Roles

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Nikola:1234@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(Role, '/role/<string:role_name>')
api.add_resource(Roles, '/roles')
api.add_resource(User, '/users/<string:email>')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,
            debug=True)
