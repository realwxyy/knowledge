from src.model import User, UserSchema
from src.utils import db


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
