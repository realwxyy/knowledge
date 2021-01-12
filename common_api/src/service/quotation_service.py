from sqlalchemy import or_, and_
from src.model import Quotation, QuotationSchema
from src.model import QuotationProduct, QuotationProductSchema
from src.model import QuotationTag, QuotationTagSchema
from src.utils import db
from . import quotation_tag_service
import time


def query_quotation_by_name(name):
    '''
    @ description query quotation with quotation's name (may be no useful)
    @ param quotation's name
    @ param_type string
    @ return_type dict
    '''
    quotation_schema = QuotationSchema()
    condition = (and_(Quotation.is_delete >= 0))
    condition = and_(condition, Quotation.zh_name == name)
    sql_res = Quotation.query.filter(*condition)
    quotation = sql_res.first()
    return quotation_schema.dump(quotation)


def query_quotation_by_id(id):
    '''
    @ description query quotation with quotation's id
    @ param quotation's id
    @ param_type number
    @ return_type dict
    '''
    quotation_schema = QuotationSchema()
    quotation = Quotation.query.get(id)
    return quotation_schema.dump(quotation)


def save_quotation(params):
    '''
    @ description save quotation
    @ param dict of quotation object
    @ param_type a dict of added quotation
    @ return dict of added quotation
    @ return_type: dict
    '''
    quotation_schema = QuotationSchema()
    quotation = quotation_schema.load(params, session=db.session)
    return quotation_schema.dump(quotation.save())


def save_quotation_product(params):
    '''
    @ description save quotation's product
    @ param dict of added quotation products
    @ param_type dict
    @ return None
    @ return_type None
    '''
    quotation_product_schema = QuotationProductSchema()
    quotation_product = quotation_product_schema.load(params, session=db.session, many=True)
    db.session.bulk_save_objects(quotation_product)
    db.session.commit()


def save_quotation_tag(params):
    '''
    @ description save quotation's tag
    @ param dict of added quotation tags
    @ param_type dict
    @ return None
    @ return_type None
    '''
    quotation_tag_schema = QuotationTagSchema()
    quotation_tags = quotation_tag_schema.load(params, session=db.session, many=True)
    db.session.bulk_save_objects(quotation_tags)
    db.session.commit()


def del_tags(params):
    '''
    @ description delete quotation's tags (only save)
    @ param dict of quotation (only needed id of quotation)
    @ param_type dict
    @ return None
    @ return_type None
    '''
    id = int(params.get('id'))
    condition = (and_(QuotationTag.is_delete >= 0))
    condition = and_(condition, QuotationTag.quotation_id == id)
    quotation_tags = QuotationTag.query.filter(*condition)
    for item in quotation_tags:
        item.is_delete = -1
        item.update_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    db.session.bulk_save_objects(quotation_tags)
    db.session.commit()
    pass


def del_products(params):
    '''
    @ description set is_delete to -1 and assign udpate_date to now time which quotation_id = params's id
    @ param dict of id
    @ param_type dict
    @ return None
    @ return_type None
    '''
    id = int(params.get('id'))
    condition = (and_(QuotationProduct.is_delete >= 0))
    condition = and_(condition, QuotationProduct.quotation_id == id)
    quotation_products = QuotationProduct.query.filter(*condition)
    for item in quotation_products:
        item.is_delete = -1
        item.update_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    db.session.bulk_save_objects(quotation_products)
    db.session.commit()


def delete_quotation(params):
    '''
    @ description set is_delete to -q and assign update_date to now time which quotation_id = param's id
    @ param dict to be processed
    @ param_type dict
    @ return dict to delete result (keep it like this for now)
    @ return_type dict
    '''
    quotation_schema = QuotationSchema()
    try:
        quotation = quotation_schema.load(params, session=db.session)
        quotation.save()
        name = quotation.name
        return {'code': 0, 'message': '已删除:' + name}
    except Exception:
        return {'code': -1, 'message': '删除失败'}


def mini_queryList(params):
    '''
    @ description wechat mini program quotation list
    @ param dict of query eg: quotation name/page/size
    @ param_type dict
    @ return dict of quotation list
    @ return_type dict
    '''
    name = params.get('name')
    page = int(params.get('page'))
    size = int(params.get('size'))
    quotation_schema = QuotationSchema(many=True, only=['id', 'main_img', 'name', 'short_name', 'description', 'create_date'])
    condition = [Quotation.is_delete >= 0]
    total = Quotation.query.filter(*condition).count()
    if name:
        condition.append(Quotation.name.like('%' + name + '%'))
        total = Quotation.query.filter(*condition).count()
    sql_res = Quotation.query.filter(*condition)
    list = sql_res.paginate(page=page, per_page=size, error_out=False).items
    quotation_list = quotation_schema.dump(list)
    for q in quotation_list:
        q.update({'tags': quotation_tag_service.query_tags_id_by_quotation_id(q.get('id'))})
    return {'list': quotation_list, 'total': total}


def admin_list(params):
    '''
    @ description background system quotation list
    @ param dict of query eg: code/quotation_name/page/size
    @ param_type dict
    @ return dict of quottion list
    @ return_type dict
    '''
    code = params.get('code')
    name = params.get('name')
    page = int(params.get('page'))
    size = int(params.get('size'))
    quotation_schema = QuotationSchema(many=True)
    condition = [Quotation.is_delete >= 0]
    # try:
    if code:
        condition = and_(condition, Quotation.code.like('%' + code + '%'))
    if name:
        condition = and_(condition, Quotation.name.like('%' + name + '%'))
    sql_res = Quotation.query.filter(*condition)
    admin_list = sql_res.paginate(page=page, per_page=size, error_out=False).items
    total = len(admin_list)
    # except Exception as e:
    #     print(e)
    #     return {'code': -1, 'msg': '服务器异常'}
    return {'list': quotation_schema.dump(admin_list), 'total': total}