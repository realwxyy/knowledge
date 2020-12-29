from src.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Product(db.Model):
    # 定义表名
    __tablename__ = 'product'
    # 定义字段
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    brand_id = db.Column(db.Integer())
    series = db.Column(db.String(64))
    specification = db.Column(db.String(64))
    main_img = db.Column(db.String(64))
    shelf_number = db.Column(db.String(64))
    code = db.Column(db.String(64))
    factor_code = db.Column(db.String(64))
    unit = db.Column(db.String(64))
    desc = db.Column(db.String(128))
    standard_price = db.Column(db.DECIMAL(7))
    in_stock = db.Column(db.String(64))
    origin = db.Column(db.String(64))
    daily_retail_price = db.Column(db.DECIMAL(7))
    daily_red_line_price = db.Column(db.DECIMAL(7))
    promotional_red_line_price = db.Column(db.DECIMAL(7))
    box_gauge = db.Column(db.String(64))
    suitable_age = db.Column(db.String(64))
    suitable_sex = db.Column(db.String(64))
    gross_weight = db.Column(db.String(64))
    box_gross_weight = db.Column(db.String(64))
    expect_arrival_time = db.Column(db.DateTime(7))
    features = db.Column(db.String(64))
    serial_number = db.Column(db.Integer())
    detail = db.Column(db.Text())
    create_date = db.Column(db.DateTime(10))
    update_date = db.Column(db.DateTime(10))
    is_delete = db.Column(db.Integer())

    def get_schema(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand_id': self.brand_id,
            'series': self.series,
            'specification': self.specification,
            'main_img': self.main_img,
            'shelf_number': self.shelf_number,
            'code': self.code,
            'factor_code': self.factor_code,
            'unit': self.unit,
            'desc': self.desc,
            'standard_price': self.standard_price,
            'in_stock': self.in_stock,
            'origin': self.origin,
            'daily_retail_price': self.daily_retail_price,
            'daily_red_line_price': self.daily_red_line_price,
            'promotional_red_line_price': self.promotional_red_line_price,
            'box_gauge': self.box_gauge,
            'suitable_age': self.suitable_age,
            'suitable_sex': self.suitable_sex,
            'gross_weight': self.gross_weight,
            'box_gross_weight': self.box_gross_weight,
            'expect_arrival_time': self.expect_arrival_time,
            'features': self.features,
            'serial_number': self.serial_number,
            'detail': self.origin,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'is_delete': self.is_delete
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        # sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    brand_id = fields.Integer()
    series = fields.String()
    specification = fields.String()
    main_img = fields.String()
    shelf_number = fields.String()
    code = fields.String()
    factor_code = fields.String()
    unit = fields.String()
    desc = fields.String()
    standard_price = fields.Number()
    in_stock = fields.String()
    origin = fields.String()
    daily_retail_price = fields.Number()
    daily_red_line_price = fields.Number()
    promotional_red_line_price = fields.Number()
    box_gauge = fields.String()
    suitable_age = fields.String()
    suitable_sex = fields.String()
    gross_weight = fields.String()
    box_gross_weight = fields.String()
    expect_arrival_time = fields.DateTime()
    features = fields.String()
    serial_number = fields.Integer()
    detail = fields.String()
    create_date = fields.DateTime()
    update_date = fields.DateTime()
    is_delete = fields.Number()