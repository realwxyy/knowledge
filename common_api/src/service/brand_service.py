from sqlalchemy import or_, and_
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


def admin_list(params):
    page = int(params.get('page'))
    size = int(params.get('size'))
    brandName = params.get('brandName')
    brand_schema = BrandSchema(many=True)
    total = 0
    condition = Brand.is_delete >= 0
    if brandName:
        match1 = Brand.en_name.like('%' + brandName + '%')
        match2 = Brand.zh_name.like('%' + brandName + '%')
        condition = and_(condition, or_(match1, match2))
    sql_res = Brand.query.filter(condition)
    admin_list = sql_res.paginate(page=page, per_page=size, error_out=False).items
    total = sql_res.count()
    return {'list': brand_schema.dump(admin_list), 'total': total}
