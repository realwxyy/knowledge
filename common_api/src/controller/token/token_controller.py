from flask import Blueprint, request
from src.utils import resp
from src.service import token_service

gl_token = Blueprint('token', __name__, url_prefix='/token')


@gl_token.route('/get_token', methods=['post'])
def get_token():
    data = token_service.get_token(request.values)
    if data['status_code'] == 0:
        return resp.resp_succ(data['msg'])
    else:
        return resp.resp_fail({}, data['msg'])
    # try:
    #     user = User.query.filter_by(phone=phone).first()
    # except Exception:
    #     return jsonify(code=4004,msg="获取信息失败")

    # if user is None or not user.check_password(password):
    #     return jsonify(code=4103,msg="手机号或密码错误")

    # # 获取用户id，传入生成token的方法，并接收返回的token
    # token = create_token(user.id)

    # # 把token返回给前端
    # return jsonify(code=0,msg="成功",data=token)
