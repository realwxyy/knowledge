from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from werkzeug.security import generate_password_hash, check_password_hash


class APP_CONFIG(db.Model):
    # 定义表名
    __tablename__ = 'app_config'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_id = db.Column(db.String(64))
    app_secret  = db.Column(db.String(128))
    app_desc = db.Column(db.String())
    create_date = db.Column(db.DateTime(10))
    update_date = db.Column(db.DateTime(10))

    def get_schema(self):
        return {
            'id': self.id,
            'app_id': self.app_id,
            'app_secret': self.app_secret,
            'app_desc': self.app_desc,
            'create_date': self.create_date,
            'update_date': self.update_date,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

class APP_CONFIG_SCHEMA(ModelSchema):
    class Meta:
        model = APP_CONFIG
        # sqla_session = db.session

    id = fields.Number()
    app_id = fields.String()
    app_secret = fields.String()
    app_desc = fields.String()
    create_date = fields.DateTime()
    update_date = fields.DateTime()