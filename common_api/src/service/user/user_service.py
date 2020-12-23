from src.model import User, UserSchema, Code2Session
from src.utils import db
from src.constant import code2Session
import json
import requests


def save_user(data):
    user_schema = UserSchema()
    user = user_schema.load(data, session=db.session)
    result = user_schema.dump(user.save())
    print(result)


def get_users():
    data = User.query.all()
    user_schema = UserSchema(many=True, only=['id', 'name', 'age'])
    users = user_schema.dump(data)
    return users


def test_return():
    data = User.query.all()
    user_schema = UserSchema(many=True, only=['id', 'name'])
    user = user_schema.dump(data)
    return user


# get user with user_id
def get_user_by_id(data):
    return User.query.get(data["id"])

# get user with name


def get_user_by_name(data):
    user = User.query.filter_by(name=data['name']).first()
    return user


def code2session(data):
    data['js_code'] = data['code']
    code_2_session = Code2Session(data)
    data_json = code_2_session.__dict__
    resp_data = requests.get(code2Session, params = data_json).json()
    if resp_data.get('errcode'):
        return {'errcode': resp_data.get('errcode'), 'errmsg': resp_data.get('errmsg')}
    else:
        return {'session_key': resp_data.get('session_key'), 'openid': resp_data.get('openid')}
