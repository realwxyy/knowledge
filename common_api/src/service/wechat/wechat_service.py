from sqlalchemy import or_, and_
from src.model import WechatUser, WechatUserSchema
from src.utils import db
import time


def save_wechat_user(params):
    wechat_user_schema = WechatUserSchema()
    wechat_user = wechat_user_schema.load(params, session=db.session)
    return wechat_user_schema.dump(wechat_user.save())


def get_wechat_user_by_open_id(openId):
    wechat_user_schema = WechatUserSchema()
    condition = and_(WechatUser.is_delete >= 0)
    condition = and_(condition, WechatUser.open_id == openId)
    sql_res = WechatUser.query.filter(*condition)
    wechat_user = sql_res.first()
    return wechat_user_schema.dump(wechat_user)