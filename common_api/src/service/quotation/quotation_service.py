from src.model import Quotation, QuotationSchema
from src.utils import db


def query_quotation_by_name(name):
    quotation_schema = QuotationSchema()
    quotation = Quotation.query.filter(Quotation.zh_name == name).filter(Quotation.is_delete >= 0).first()
    return quotation_schema.dump(quotation)


def query_quotation_by_id(id):
    quotation_schema = QuotationSchema()
    quotation = Quotation.query.get(id)
    return quotation_schema.dump(quotation)


def save_quotation(params):
    quotation_schema = QuotationSchema()
    quotation = quotation_schema.load(params, session=db.session)
    return quotation_schema.dump(quotation.save())


def delete_quotation(params):
    quotation_schema = QuotationSchema()
    try:
        quotation = quotation_schema.load(params, session=db.session)
        quotation.save()
        name = quotation.name
        return {'code': 0, 'message': '已删除:' + name}
    except Exception:
        return {'code': -1, 'message': '删除失败'}