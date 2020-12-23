from flask import Blueprint, request
from src.utils import resp, login_required
from src.service import user_service, app_config_service, third_session_service
from src.utils import utils

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
    user = user_service.get_user_by_name(params)
    try:
        params['id']
    except Exception:
        if user:
            if user.name == params['name']:
                return resp.resp_fail({}, 'the name can not be repeat')
    try:
        params['password']
    except Exception:
        return resp.resp_fail({}, 'the password can not be empty')
    # 憨批代码 不准删 以后多看看自己犯的错误
    # params.update({'password': generate_password_hash(params['password'])})
    user_service.save_user(params)
    return resp.resp_succ()


@gl_user.route('/get_users', methods=['get'])
@login_required
def get_users():
    return resp.resp_succ(user_service.get_users())


@gl_user.route('/test_return', methods=['get', 'post'])
@login_required
def test_return():
    user = user_service.test_return()
    return resp.resp_succ(user)


@gl_user.route('/code2session', methods=['get'])
def code2session():
    params = request.values.to_dict()
    # params['secret'] = '4cee1bf90ecce506dbc06680c127b603'#先写死 后续入库
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['appid', 'code'])
    if validate_resp['code'] == 0:
        app_config_res = app_config_service.query_app_config_by_app_id(
            params.get('appid'))
        app_secret = app_config_res.get('app_secret')
        if app_secret:
            params.update({'secret': app_secret})
            service_resp = user_service.code2session(params)
            third_session = third_session_service.get_third_session(service_resp)
            return resp.resp_succ(third_session)
        else:
            return resp.resp_fail({}, '未找到与该appid关联的appsecret,请确认appid是否正确')
    else:
        return resp.resp_fail({}, validate_resp['msg'])
