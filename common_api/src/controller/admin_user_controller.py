from flask import Blueprint, request
from src.utils import resp, utils
from src.service import admin_user_service
from src.constant import CONS_COMMON, CONS_CONTROLLER, CONS_REQ_METHOD, CONS_MSG

gl_admin_user = Blueprint('admin_user', __name__, url_prefix='/admin_user')


@gl_admin_user.route('/admin_user', methods=['post'])
def admin_user_post():
    '''
    @ description add admin user
    @ params name, password
    @ params_type dict
    @ return dict of added admin user
    @ return_type dict
    '''
    params = utils.get_params(request)
    validate_resp = utils.dict_not_empty(params, ['name', 'password'])
    if validate_resp.get('code') == 0:
        admin_user_resp = admin_user_service.query_admin_user_by_name(params.get('name'))
        if admin_user_resp.get('id'):
            return resp.resp_fail({}, '该用户名已存在')
        else:
            params = utils.assign_post_fields(params)
            admin_user_service.save_admin_user(params)
            return resp.resp_succ({}, '添加成功')
    else:
        return resp.resp.fail({}, validate_resp.get('msg'))


@gl_admin_user.route('/admin_user', methods=['put'])
def admin_user_put():
    '''
    @ description update admin user info
    @ params admin user entity
    @ params_type dict
    @ return message of udpate info
    @ return_type json
    '''
    params = utils.get_params(request)
    validate_resp = utils.dict_not_empty(params, ['id', 'password'])
    if validate_resp.get('code') == 0:
        admin_user_resp = admin_user_service.query_admin_user_by_id(params.get('id'))
        if admin_user_resp:
            params = utils.assign_put_fields(params)
            admin_user_service.save_admin_user(params)
            return resp.resp_succ({}, '修改成功')
        else:
            return resp.resp.fail({}, '未查找到该用户')
    else:
        return resp.resp.fail({}, validate_resp.get('msg'))


@gl_admin_user.route('/admin_user', methods=['delete'])
def admin_user_delete():
    '''
    @ description update admin_user's field is_delete to -1
    @ param id
    @ param_type dict
    @ return message of delete info
    @ return_type json
    '''
    params = utils.get_params(request)
    validate_resp = utils.dict_not_empty(params, ['id'])
    if validate_resp.get('code') == 0:
        admin_user_resp = admin_user_service.query_admin_user_by_id(params.get('id'))
        if admin_user_resp:
            params = utils.assign_delete_fields(params)
            admin_user_service.save_admin_user(params)
            return resp.resp_succ({}, '删除成功')
        else:
            return resp.resp.fail({}, '未查找到该用户')
    else:
        return resp.resp.fail({}, validate_resp.get('msg'))
