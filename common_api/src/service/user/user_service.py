from src.model import User, UserSchema
from src.utils import db, resp
# from src.service import token_service


def test_return():
    data = User.query.all()
    user_schema = UserSchema(many=True, only=['id', 'name', 'age'])
    user = user_schema.dump(data)
    return resp.resp_succ(user)


# get user with user_id
def get_user_by_id(data):
  return User.query.get(data["id"])