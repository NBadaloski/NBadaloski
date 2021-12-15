from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('role_id',
                        type=int,
                        required=True,
                        help="Every user needs a role_id."
                        )

    def get(self, email):
        user = UserModel.find_by_email(email)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self, email):
        if UserModel.find_by_email(email):
            return {'message': "A user with that email address '{}' already exists.".format(email)}, 400

        data = User.parser.parse_args()

        user = UserModel(data['username'], email, data['role_id'])

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the user."}, 500

        return user.json(), 201

    def delete(self, email):
        user = UserModel.find_by_email(email)
        if user:
            user.delete_from_db()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404

    def put(self, email):
        data = User.parser.parse_args()

        user = UserModel.find_by_email(email)

        if user:
            (user.username, user.role_id) = (data['username'], data['role_id'])
        else:
            user = UserModel(data['username'], email, data['role_id'])

        user.save_to_db()

        return user.json()

class Users(Resource):
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}
