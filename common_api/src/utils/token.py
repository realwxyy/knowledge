# 导入依赖包
from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# # from src.service import user_service
# from src.model import User
import functools

# AOP can only be called after logging in


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers["common-token"]
        except Exception:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            return jsonify(code=4103, msg='缺少参数token')

        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify(code=4101, msg="登录已过期")

        return view_func(*args, **kwargs)

    return verify_token
