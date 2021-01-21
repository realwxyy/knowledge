from flask import Blueprint, request
from src.utils import resp, utils
from src.service import admin_user_service, login_service

gl_login = Blueprint('login', __name__, url_prefix='/login')


@gl_login.route('/login', methods=['post'])
def login_post():
    '''
    @ description user login
    @ param name password
    @ param_type dict
    @ return succ: admin_user info fail: failed message
    @ return_type json
    '''
    params = utils.get_params(request)
    validate_resp = utils.dict_not_empty(params, ['name', 'password'])
    if validate_resp.get('code') == 0:
        resp_dict = login_service.login(params)
        if resp_dict.get('code') == 0:
            admin_resp = resp_dict.get('data')
            return resp.resp_succ(admin_resp, '登录成功')
        else:
            return resp.resp_fail({}, resp_dict.get('msg'))
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))
