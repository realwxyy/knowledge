from src.model import AdminUser, AdminUserSchema
from . import admin_user_service
from src.utils import db


def login(params):
    admin_user_schema = AdminUserSchema(only=['id', 'name', 'nickname', 'phone', 'role_id'])
    admin_user = admin_user_service.query_admin_user_entity_by_name(params.get('name'))
    if admin_user:
        flag = admin_user_service.check_admin_user_password(admin_user, params.get('password'))
        if flag:
            return {'code': 0, 'data': admin_user_schema.dump(admin_user)}
        else:
            return {'code': 1, 'msg': '密码错误'}
    else:
        return {'code': 1, 'msg': '用户名错误'}
