from flask import current_app, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import response as resp
import functools


def wechat_login_required(view_func):
    '''
    AOP can only be called after logging in
    微信小程序登录态拦截
    '''
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # 在请求头上拿到token
            third_session = request.headers["wechat_third_session"]
        except Exception:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            # return jsonify(code=4103, msg='缺少参数token')
            return resp.resp_unauthorized({}, '用户无法识别')

        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(third_session)
        except Exception:
            # return jsonify(code=4101, msg="登录已过期")
            return resp.resp_unauthorized({}, '登录态已过期')

        return view_func(*args, **kwargs)

    return verify_token


def gen_3rdsession(params):
    # 用 openId 和 session_key 加密生成 3rd session
    # 过期时间为 60s * 60m * 24h * 30d
    # .decode("ascii")必加 一下午就解决这个 bug 了 不然是 byte 类型 jsonify 方法无法转换byte类型
    s = Serializer(current_app.config['SECRET_KEY'], 60 * 60 * 24 * 31)
    third_session = s.dumps(params).decode("ascii")
    return third_session


def decrypt_3rdsession(third_session):
    # 用 3rd_session 解密生成 openId 和 session_key
    s = Serializer(current_app.config['SECRET_KEY'])
    params = s.loads(third_session)
    return params
