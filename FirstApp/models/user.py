from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(150), unique = True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    role = db.relationship('RolesModel')

    def __init__(self, username, email, role_id):
        self.username = username
        self.email = email
        self.role_id = role_id

    def json(self):
        return {'username': self.username,
                'email': self.email,
                'role_id': self.role_id}

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
