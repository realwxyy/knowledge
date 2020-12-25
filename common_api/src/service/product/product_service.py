from src.model import Product, ProductSchema
from src.utils import db


def query_product_by_name(name):
    product_schema = ProductSchema()
    product = Product.query.filter(Product.zh_name == name).filter(Product.is_delete >= 0).first()
    return product_schema.dump(product)


def query_product_by_id(id):
    product_schema = ProductSchema()
    product = Product.query.get(id)
    return product_schema.dump(product)


def save_product(params):
    product_schema = ProductSchema()
    product = product_schema.load(params, session=db.session)
    return product_schema.dump(product.save())


def delete_product(params):
    product_schema = ProductSchema()
    try:
        product = product_schema.load(params, session=db.session)
        product.save()
        name = product.name
        return {'code': 0, 'message': '已删除:' + name}
    except Exception:
        return {'code': -1, 'message': '删除失败'}