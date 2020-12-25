from src.model import Tag, TagSchema
from src.utils import db
import json


def query_tag_by_name(name):
    tag_schema = TagSchema()
    print('sql start--------------------------------------------------')
    tag = Tag.query.filter(Tag.name == name).filter(Tag.is_delete >= 0).first()
    print('sql end--------------------------------------------------')
    return tag_schema.dump(tag)


def query_tag_by_id(id):
    tag_schema = TagSchema()
    tag = Tag.query.get(id)
    return tag_schema.dump(tag)


def save_tag(params):
    tag_schema = TagSchema()
    tag = tag_schema.load(params, session=db.session)
    return tag_schema.dump(tag.save())


def delete_tag(params):
    tag_schema = TagSchema()
    params.update({'is_delete': -1})
    try:
        tag = tag_schema.load(params, session=db.session)
        tag.save()
        name = tag.name
        return {'code': 0, 'message': '已删除:' + name}
    except Exception:
        return {'code': -1, 'message': '删除失败'}


def query_tags():
    tag_schema = TagSchema(many=True, only=['id', 'name'])
    tag = Tag.query.filter(Tag.is_delete >= 0).all()
    return tag_schema.dump(tag)
