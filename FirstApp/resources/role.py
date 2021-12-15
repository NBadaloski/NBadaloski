from flask_restful import Resource
from models.role import RolesModel


class Role(Resource):
    def get(self, role_name):
        role = RolesModel.find_by_name(role_name)
        if role:
            return role.json()
        return {'message': 'Role not found'}, 404

    def post(self, role_name):
        if RolesModel.find_by_name(role_name):
            return {'message': "A role with the same name '{}' already exists.".format(role_name)}, 400

        role = RolesModel(role_name)
        try:
            role.save_to_db()
        except:
            return {"message": "An error occurred creating the role."}, 500

        return role.json(), 201

    def delete(self, role_name):
        role = RolesModel.find_by_name(role_name)
        if role:
            role.delete_from_db()

        return {'message': 'Role deleted'}


class Roles(Resource):
    def get(self):
        return {'roles': list(map(lambda x: x.json(), RolesModel.query.all()))}
