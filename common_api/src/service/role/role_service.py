from src.model import Role, RoleSchema
from src.utils import db


def query_role_by_name(name):
    role_schema = RoleSchema()
    role = Role.query.filter_by(name=name).first()
    return role_schema.dump(role)


def add_role(params):
    role_schema = RoleSchema()
    role = role_schema.load(params, session=db.session)
    return role_schema.dump(role.save())


def query_roles():
    role_schema = RoleSchema(many=True, only=['id', 'name', 'level', 'remark', 'create_date', 'update_date'])
    roles = Role.query.all()
    return role_schema.dump(roles)
