# 导入依赖包
from flask import jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from src.model import User, UserSchema


def create_token(api_user):
    '''
    生成token
    :param api_user:用户id
    :return: token
    '''

    # 第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    # 第二个参数是有效期(秒)
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
    # 接收用户id转换与编码
    token = s.dumps({"id": api_user}).decode("ascii")
    return token


def verify_token(token):
    '''
    校验token
    :param token: 
    :return: 用户信息 or None
    '''
    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    # 此处修改 调用service 避免循环引入的同时 消除未引入User造成的代码警告
    user = User.query.get(data["id"])
    return user
    # return user_service.get_user_by_id(data)


def get_token(params):

    name = params.get('name')
    password = params.get('password')
    param_user = User()
    param_user.password = password
    try:
        user = User.query.filter_by(name=name).first()
        if not user.verify_password(password):
            return {'status_code': 1, 'code': 4001, 'msg': '密码错误'}
    except Exception:
        return {'status_code': 1, 'code': 4004, 'msg': '获取用户信息失败'}

    # if user is None or not user.check_password(password):
    #     return jsonify(code=4103,msg="手机号或密码错误")
    # 获取用户id，传入生成token的方法，并接收返回的token
    token = create_token(user.id)
    return {'status_code': 0, 'code': 200, 'msg': token}
