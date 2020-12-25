from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Brand(db.Model):
    # 定义表名
    __tablename__ = 'brand'
    # 定义字段
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    logo = db.Column(db.String(64))
    story = db.Column(db.String(64))
    zh_name = db.Column(db.String(64))
    en_name = db.Column(db.String(64))
    code = db.Column(db.String(64))
    features = db.Column(db.String(64))
    promotional_img = db.Column(db.String(64))
    promotional_word = db.Column(db.String(64))
    cooperation_conditions = db.Column(db.String(64))
    preferential_conditions = db.Column(db.String(64))
    region = db.Column(db.String(64))
    control_price_display = db.Column(db.String(64))
    serial_number = db.Column(db.String(64))
    create_date = db.Column(db.DateTime(10))
    update_date = db.Column(db.DateTime(10))
    is_delete = db.Column(db.Integer())

    def get_schema(self):
        return {
            'id': self.id,
            'logo': self.logo,
            'story': self.story,
            'zh_name': self.zh_name,
            'en_name': self.en_name,
            'code': self.code,
            'features': self.features,
            'promotional_img': self.promotional_img,
            'promotional_word': self.promotional_word,
            'cooperation_conditions': self.cooperation_conditions,
            'preferential_conditions': self.preferential_conditions,
            'region': self.region,
            'control_price_display': self.control_price_display,
            'serial_number': self.serial_number,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'is_delete': self.is_delete
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class BrandSchema(ModelSchema):
    class Meta:
        model = Brand
        # sqla_session = db.session

    id = fields.Number()
    logo = fields.String(required=False)
    story = fields.String(required=False)
    zh_name = fields.String(required=False)
    en_name = fields.String(required=False)
    code = fields.String(required=False)
    features = fields.String(required=False)
    promotional_img = fields.String(required=False)
    promotional_word = fields.String(required=False)
    cooperation_conditions = fields.String(required=False)
    preferential_conditions = fields.String(required=False)
    region = fields.String(required=False)
    control_price_display = fields.String(required=False)
    serial_number = fields.String(required=False)
    create_date = fields.DateTime(required=False)
    update_date = fields.DateTime(required=False)
    is_delete = fields.Number(required=False)