from src.model import User, UserSchema
from src.utils import db, resp
from src.utils import create_token


def test_return():
    data = User.query.all()
    user_schema = UserSchema(many=True, only=['id', 'name', 'age'])
    user = user_schema.dump(data)
    return resp.resp_succ(user)


def get_token(params):

    name = params.get('name')
    age = params.get('age')
    try:
        user = User.query.filter_by(name=name).first()
    except Exception:
        return resp.resp_fail({}, '查询用户失败')

    # if user is None or not user.check_password(password):
    #     return jsonify(code=4103,msg="手机号或密码错误")
    # 获取用户id，传入生成token的方法，并接收返回的token
    token = create_token(user.id)
    return resp.resp_succ(token)
