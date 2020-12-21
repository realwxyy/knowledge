from flask import Blueprint, request
from src.utils import resp, login_required
from src.service import user_service, token_service
from werkzeug.security import generate_password_hash, check_password_hash

gl_user = Blueprint('user', __name__, url_prefix='/user')


@gl_user.route('/t1', methods=['get'])
def t1():
    return 'welocome to /test/t1'


@gl_user.route('/t2', methods=['post'])
def t2():
    return 'welcome to /test/t2'

# 模拟请求接口成功的参数


@gl_user.route('/t3', methods=['get'])
def t3():
    # return {'code': 200, 'msg': '成功', 'data': []}
    return resp.resp_succ()

# 新增测试参数


@gl_user.route('/save_user', methods=['post', 'put'])
def save_user():
    params = request.values.to_dict()
    try:
        params['password']
    except Exception:
        return resp.resp_fail('the password can not be empty')
    params.update({'password': generate_password_hash(params['password'])})
    user_service.save_user(params)
    return resp.resp_succ()


@gl_user.route('/get_users', methods=['get'])
def get_users():
    return resp.resp_succ(user_service.get_users())


@gl_user.route('/test_return', methods=['get', 'post'])
@login_required
def test_return():
    user = user_service.test_return()
    return resp.resp_succ(user)
