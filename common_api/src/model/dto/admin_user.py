from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from werkzeug.security import generate_password_hash, check_password_hash


class AdminUser(db.Model):
    # 定义表名
    __tablename__ = 'admin_user'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    nickname = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    role_id = db.Column(db.Integer)
    create_date = db.Column(db.DateTime(10))
    update_date = db.Column(db.DateTime(10))
    is_delete = db.Column(db.Integer())

    def get_schema(self):
        return {
            'id': self.id,
            'name': self.name,
            # 'password': self.password,
            'password_hash': self.password_hash,
            'nickname': self.nickname,
            'phone': self.phone,
            'role_id': self.role_id,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'is_delete': self.is_delete,
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
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class AdminUserSchema(ModelSchema):
    class Meta:
        model = AdminUser
        # sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    password = fields.String()
    password_hash = fields.String()
    nickname = fields.String()
    phone = fields.String()
    role_id = fields.Number()
    create_date = fields.String()
    update_date = fields.String()
    is_delete = fields.Number()