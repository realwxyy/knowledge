from flask import Blueprint, request
from src.utils import resp, utils
from src.service import role_service

gl_role = Blueprint('role', __name__, url_prefix='/role')


@gl_role.route('save_role', methods=['post', 'put'])
def save_role():
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['name', 'level'])
    if validate_resp.get('code') == 0:
        role_resp = role_service.query_role_by_name(params.get('name'))
        if role_resp.get('id') and not params.get('id'):
            return resp.resp_fail({}, '请勿重复添加角色：' + role_resp.get('remark'))
        else:
            if params.get('create_date') is None:
                params.update({'create_date': utils.if_empty_give_now_date()})
            if params.get('update_date') is None:
                params.update({'update_date': utils.if_empty_give_now_date()})
            return role_service.add_role(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_role.route('query_roles', methods=['get'])
def query_role():
    params = request.values.to_dict()
    return resp.resp_succ(role_service.query_roles())
