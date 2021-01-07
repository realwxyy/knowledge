from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # 定义表名
    __tablename__ = 'user_info'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    password_hash  = db.Column(db.String(128))

    def get_schema(self):
        return {
            'id': self.id,
            'name': self.name,
            # 'password': self.password,
            'password_hash': self.password_hash
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash  = generate_password_hash(password)
    
    def verify_password(self, password):
        print(self.password_hash)
        return check_password_hash(self.password_hash, password)

class UserSchema(ModelSchema):
    class Meta:
        model = User
        # sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    password = fields.String()
    password_hash = fields.String()