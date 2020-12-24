from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Role(db.Model):
    # 定义表名
    __tablename__ = 'role'
    # 定义字段
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    level  = db.Column(db.Integer())
    remark = db.Column(db.String(64))
    create_date = db.Column(db.DateTime(10))
    update_date = db.Column(db.DateTime(10))

    def get_schema(self):
        return {
            'id': self.id,
            'name': self.app_id,
            'level': self.app_secret,
            'remark': self.app_desc,
            'create_date': self.create_date,
            'update_date': self.update_date,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

class RoleSchema(ModelSchema):
    class Meta:
        model = Role
        # sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    level = fields.Number()
    remark = fields.String()
    create_date = fields.DateTime()
    update_date = fields.DateTime()