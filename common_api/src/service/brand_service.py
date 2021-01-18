from src.model import Brand, BrandSchema
from src.utils import db


def query_brand_by_name(name):
    brand_schema = BrandSchema()
    brand = Brand.query.filter(Brand.zh_name == name).filter(Brand.is_delete >= 0).first()
    return brand_schema.dump(brand)


def query_brand_by_id(id):
    brand_schema = BrandSchema()
    brand = Brand.query.get(id)
    return brand_schema.dump(brand)


def save_brand(params):
    brand_schema = BrandSchema()
    brand = brand_schema.load(params, session=db.session)
    return brand_schema.dump(brand.save())


def delete_brand(params):
    brand_schema = BrandSchema()
    try:
        brand = brand_schema.load(params, session=db.session)
        brand.save()
        name = brand.name
        return {'code': 0, 'message': '已删除:' + name}
    except Exception:
        return {'code': -1, 'message': '删除失败'}


# def query_brands():
#     tag_schema = BrandSchema(many=True, only=['id', 'name'])
#     tag = Brand.query.filter(Brand.is_delete >= 0).all()
#     return tag_schema.dump(tag)
