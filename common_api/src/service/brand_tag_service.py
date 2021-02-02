from src.model import BrandTag, BrandTagSchema
from src.model import Tag, TagSchema
from src.model import Brand, BrandSchema
from src.utils import db


def save_brand_tag(params):
    '''
    @ description save brand's tag
    @ param dict of added brand tags
    @ param_type dict
    @ return None
    @ return_type None
    '''
    brand_tags = BrandTagSchema().load(params, session=db.session, many=True)
    db.session.bulk_save_objects(brand_tags)
    db.session.commit()


def query_brand_tags_by_brand_id(brand_id):
    '''
    @ description query brand's tag with brand_id
    @ param brand_id
    @ param_type number
    @ return dict of brand tags
    @ return_type dict
    '''
    condition = [BrandTag.is_delete >= 0]
    condition.append(BrandTag.brand_id == brand_id)
    condition.append(BrandTag.tag_id == Tag.id)
    condition.append(Brand.id == BrandTag.brand_id)
    condition.append(Tag.is_delete >= 0)
    # tags_id = QuotationTag.query.filter(*condition).all()
    data = db.session.query(Tag.id, Tag.name, Tag.color).filter(*condition).all()
    tags = []
    for t in data:
        tags.append({'name': t.name, 'color': t.color, 'id': t.id})
    return tags


def delete_tag_with_brand_id(brand_id):
    condition = [BrandTag.brand_id == brand_id]
    db.session.query(BrandTag).filter(*condition).delete(synchronize_session=False)
    db.session.commit()