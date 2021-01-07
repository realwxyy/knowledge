from flask import Blueprint, request, current_app
from src.utils import resp, utils, get_logger
from src.service import role_service

gl_role = Blueprint('role', __name__, url_prefix='/role')


@gl_role.route('/role', methods=['post'])
def role_post():
    '''
    @ description save new role
    @ param json in reqeust
    @ param_type json
    @ return resposne
    @ response_type json
    '''
    params = utils.get_params(request)
    name = params.get('name')
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['name', 'level'])
    if validate_resp.get('code') == 0:
        role_resp = role_service.query_role_by_name(name)
        if not role_resp.get('id'):
            params = utils.assign_post_fields(params)
            return role_service.save_role(params)
        else:
            return resp.resp_fail({}, '请勿重复添加角色【' + role_resp.get('remark') + '】')
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_role.route('/role', methods=['put'])
def role_put():
    '''
    @ description update role
    @ param json in reqeust
    @ param_type json
    @ return response
    @ return_type json
    '''
    params = utils.get_params(request)
    id = params.get('id')
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id'])
    if validate_resp.get('code') == 0:
        role_resp = role_service.query_role_by_id(id)
        if role_resp.get('name'):
            params = utils.assign_put_fields(params)
            return role_service.save_role(params)
        else:
            return resp.resp_fail({}, '未找到该角色')
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_role.route('/role', methods=['delete'])
def role_delete():
    '''
    @ description delete role (only set is_delete = -1 which id = request's id)
    @ param json in reqeust
    @ param_type json
    @ return response
    @ return_type json
    '''
    params = utils.get_params(request)
    id = params.get('id')
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id'])
    if validate_resp.get('code') == 0:
        role_req = role_service.query_role_by_id(id)
        if role_req:
            if role_req.get('is_delete') == 0:
                params_req = {}
                params_req.update({'id': id})
                params_req = utils.assign_delete_fields(params_req)
                role_service.save_role(params_req)
                return resp.resp_succ({}, '删除成功')
            else:
                return resp.resp_fail({}, '未找到该角色')
        else:
            pass
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_role.route('/admin_list', methods=['get'])
def query_role():
    return resp.resp_succ(role_service.query_roles())
