from db import db

class RolesModel(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80))

    users = db.relationship('UserModel', lazy='dynamic')

    def __init__(self, role_name):
        self.role_name = role_name

    def json(self):
        return {'role_name': self.role_name, 'users': [user.json() for user in self.users.all()]}

    @classmethod
    def find_by_name(cls, role_name):
        return cls.query.filter_by(role_name=role_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
