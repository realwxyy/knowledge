from flask import Blueprint, make_response, jsonify
from src.model import User, UserSchema
from src.utils.database import db

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
  user_schema = UserSchema(many=True, only=['id','name','age'])
  user = user_schema.dump(data)
  return {'coe': 200, 'data': user}