from sqlalchemy import or_, and_
from src.model import Quotation, QuotationSchema
from src.model import QuotationProduct, QuotationProductSchema
from src.model import QuotationProducts, QuotationProductsSchema
from src.utils import db
import json


def query_quotation_by_name(name):
    quotation_schema = QuotationSchema()
    quotation = Quotation.query.filter(Quotation.zh_name == name).filter(Quotation.is_delete >= 0).first()
    return quotation_schema.dump(quotation)


def query_quotation_by_id(id):
    quotation_schema = QuotationSchema()
    quotation = Quotation.query.get(id)
    return quotation_schema.dump(quotation)


def save_quotation(params):
    '''save quotation
    @param params: dict of quotation object
    @return: a dict of added quotation
    @return type: dict
    '''
    quotation_schema = QuotationSchema()
    quotation = quotation_schema.load(params, session=db.session)
    return quotation_schema.dump(quotation.save())


def save_quotation_product(params):
    params = [{'id': 9, 'product_id': 2, 'quotation_id': 2, 'supply_price': 12.5}, {'id': 10, 'product_id': 2, 'quotation_id': 2, 'supply_price': 13.5}]
    quotation_product_schema = QuotationProductSchema()
    print(type(params))
    print(params)
    quotation_product = quotation_product_schema.load(params, session=db.session, many=True)
    # print(quotation_product_schema.dump(quotation_product))
    print(quotation_product)
    db.session.bulk_save_objects(quotation_product)
    db.session.commit()
    return {}
    # quotation_products_schema = QuotationProductsSchema()
    # print(params)
    # quottion_products = quotation_products_schema.load(params, many=True)
    # print(quotation_products_schema.dump(quottion_products))
    # return {}


def delete_quotation(params):
    quotation_schema = QuotationSchema()
    try:
        quotation = quotation_schema.load(params, session=db.session)
        quotation.save()
        name = quotation.name
        return {'code': 0, 'message': '已删除:' + name}
    except Exception:
        return {'code': -1, 'message': '删除失败'}


def mini_queryList(params):
    name = params.get('name')
    page = int(params.get('page'))
    size = int(params.get('size'))
    quotation_schema = QuotationSchema(many=True, only=['id', 'name', 'short_name', 'create_date'])
    total = Quotation.query.filter(Quotation.is_delete >= 0).count()
    list = []
    if name:
        list = Quotation.query.filter(Quotation.name.like('%' + name + '%') and Quotation.is_delete >= 0).paginate(page=page, per_page=size, error_out=False).items
    else:
        list = Quotation.query.filter(Quotation.is_delete >= 0).paginate(page=page, per_page=size, error_out=False).items
    return {'list': quotation_schema.dump(list), 'total': total}


def admin_list(params):
    code = params.get('code')
    name = params.get('name')
    page = int(params.get('page'))
    size = int(params.get('size'))
    quotation_schema = QuotationSchema(many=True)
    condition = (and_(Quotation.is_delete >= 0))
    # try:
    if code:
        condition = and_(condition, Quotation.code.like('%' + code + '%'))
    if name:
        condition = and_(condition, Quotation.name.like('%' + name + '%'))
    sql_res = Quotation.query.filter(*condition)
    total = sql_res.count()
    admin_list = sql_res.paginate(page=page, per_page=size, error_out=False).items
    # except Exception as e:
    #     print(e)
    #     return {'code': -1, 'msg': '服务器异常'}
    return {'list': quotation_schema.dump(admin_list), 'total': total}


def save_product_to_quotation(params):
    return {}