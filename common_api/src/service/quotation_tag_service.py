from sqlalchemy import or_, and_
from src.model import Quotation, QuotationSchema
from src.model import QuotationProduct, QuotationProductSchema
from src.model import QuotationTag, QuotationTagSchema
from src.model import Tag, TagSchema
from src.utils import db
from . import quotation_tag_service
import time


def query_tags_id_by_quotation_id(id):
    # quotation_tag_schema = QuotationTagSchema(many=True, only=['tag_id'])
    condition = [QuotationTag.is_delete >= 0]
    condition.append(QuotationTag.quotation_id == id)
    condition.append(QuotationTag.tag_id == Tag.id)
    condition.append(Quotation.id == QuotationTag.quotation_id)
    condition.append(Tag.is_delete >= 0)
    # tags_id = QuotationTag.query.filter(*condition).all()
    data = db.session.query(Tag.name).filter(*condition).all()
    tags = []
    for t in data:
        tags.append(t.name)
    return tags
