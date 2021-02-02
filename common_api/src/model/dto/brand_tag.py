from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class BrandTag(db.Model):
    # 定义表名
    __tablename__ = 'brand_tag'
    # 定义字段
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    brand_id = db.Column(db.Integer())
    tag_id = db.Column(db.Integer())
    create_date = db.Column(db.DateTime())
    update_date = db.Column(db.DateTime())
    is_delete = db.Column(db.Integer())

    def get_schema(self):
        return {'id': self.id, 'tag_id': self.tag_id, 'brand_id': self.brand_id, 'create_date': self.create_date, 'update_date': self.update_date, 'is_delete': self.is_delete}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class BrandTagSchema(ModelSchema):
    class Meta:
        model = BrandTag
        # sqla_session = db.session

    id = fields.Number()
    tag_id = fields.Number()
    brand_id = fields.Number()
    create_date = fields.DateTime()
    update_date = fields.DateTime()
    is_delete = fields.Number()