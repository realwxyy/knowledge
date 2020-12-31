from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields, post_load


class QuotationProduct(db.Model):
    # 定义表名
    __tablename__ = 'quotation_product'
    # 定义字段
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer())
    quotation_id = db.Column(db.Integer())
    supply_price = db.Column(db.DECIMAL())
    serial_number = db.Column(db.Integer())
    create_date = db.Column(db.DateTime())
    update_date = db.Column(db.DateTime())
    is_delete = db.Column(db.Integer())

    def get_schema(self):
        return {'id': self.id, 'product_id': self.product_id, 'quotation_id': self.quotation_id, 'supply_price': self.supply_price, 'serial_number': self.serial_number, 'create_date': self.create_date, 'update_date': self.update_date, 'is_delete': self.is_delete}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def bulk_save(self):
        db.session.bulk_save_objects(self)
        db.session.commit()
        return self


class QuotationProductSchema(ModelSchema):
    class Meta:
        model = QuotationProduct
        # sqla_session = db.session

    id = fields.Number()
    product_id = fields.Number()
    quotation_id = fields.Number()
    supply_price = fields.Number()
    serial_number = fields.Number()
    create_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    update_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    is_delete = fields.Number()