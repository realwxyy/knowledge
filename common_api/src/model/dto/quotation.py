from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Quotation(db.Model):
    # 定义表名
    __tablename__ = 'quotation'
    # 定义字段
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    code = db.Column(db.String())
    name = db.Column(db.String(64))
    short_name = db.Column(db.String(64))
    main_img = db.Column(db.String(64))
    banner = db.Column(db.String(64))
    description = db.Column(db.String(64))
    material_link = db.Column(db.String(64))
    sort = db.Column(db.Integer())
    out_stock_status = db.Column(db.Integer())
    box_gauge_status = db.Column(db.Integer())
    create_date = db.Column(db.DateTime(10))
    update_date = db.Column(db.DateTime(10))
    is_delete = db.Column(db.Integer())

    def get_schema(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'short_name': self.short_name,
            'main_img': self.main_img,
            'banner': self.banner,
            'description': self.description,
            'material_link': self.material_link,
            'sort': self.sort,
            'out_stock_status': self.out_stock_status,
            'box_gauge_status': self.box_gauge_status,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'is_delete': self.is_delete
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def bulk_save(self, params):
        db.session.bulk_save_objects(params)
        db.session.commit()
        return self


class QuotationSchema(ModelSchema):
    class Meta:
        model = Quotation
        # sqla_session = db.session

    id = fields.Number()
    code = fields.String()
    name = fields.String()
    short_name = fields.String()
    main_img = fields.String()
    banner = fields.String()
    description = fields.String()
    material_link = fields.String()
    sort = fields.Number()
    out_stock_status = fields.Number()
    box_gauge_status = fields.Number()
    create_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    update_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    is_delete = fields.Number()