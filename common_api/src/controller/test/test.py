from flask import Blueprint, make_response, jsonify, request
from src.model import User, UserSchema
from src.utils.database import db
from src.service import test
from src.utils import create_token, login_required, verify_token

t = Blueprint('test', __name__, url_prefix='/test')


@t.route('/t1', methods=['get'])
def t1():
    return 'welocome to /test/t1'


@t.route('/t2', methods=['post'])
def t2():
    return 'welcome to /test/t2'

# 模拟请求接口成功的参数


@t.route('/t3', methods=['get'])
def t3():
    # return {'code': 200, 'msg': '成功', 'data': []}
    return make_response(jsonify({'code': 200, 'msg': '成功', 'data': []}))

# 新增测试参数


@t.route('/add_user', methods=['post'])
def add_user():
    data = {'name': 'wxyy', 'age': 18}
    user_schema = UserSchema()
    user = user_schema.load(data, session=db.session)
    result = user_schema.dump(user.save())
#   logger.info(str(result))
    return {'code': 200, 'data': result}


@t.route('/get_user', methods=['get'])
def get_user():
  data = User.query.all()
  user_schema = UserSchema(many=True, only=['id', 'name', 'age'])
  user = user_schema.dump(data)
  return {'coe': 200, 'data': user}

@t.route('/test_return', methods=['get', 'post'])
@login_required
def test_return():
    return test.test_return()


@t.route('/get_token', methods=['post'])
def get_token():
    return test.get_token(request.values)

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
