from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class WechatUser(db.Model):
    # 定义表名
    __tablename__ = 'wechat_user'
    # 定义字段
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    avatar = db.Column(db.String(128))
    nick_name  = db.Column(db.String(128))
    open_id = db.Column(db.String(64))
    create_date = db.Column(db.DateTime(10))
    update_date = db.Column(db.DateTime(10))
    is_delete = db.Column(db.Integer())

    def get_schema(self):
        return {
            'id': self.id,
            'avatar': self.avatar,
            'nick_name': self.nick_name,
            'open_id': self.open_id,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'is_delete': self.is_delete
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

class WechatUserSchema(ModelSchema):
    class Meta:
        model = WechatUser
        # sqla_session = db.session

    id = fields.Number()
    avatar = fields.String()
    nick_name = fields.String()
    open_id = fields.String()
    create_date = fields.DateTime()
    update_date = fields.DateTime()
    is_delete = fields.Number()