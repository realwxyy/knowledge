from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class User(db.Model):
    # 定义表名
    __tablename__ = 'user_info'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    age = db.Column(db.String(64))

    def get_schema(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class UserSchema(ModelSchema):
    class Meta:
        model = User
        # sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    age = fields.Number()
