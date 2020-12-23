from flask import Blueprint, request
from src.utils import resp
from src.service import app_config_service
from src.utils import utils

gl_wechat = Blueprint('wechat', __name__, url_prefix='/wechat')


@gl_wechat.route('/add_app_config', methods=['post'])
def add_app_config():
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['app_id', 'app_secret'])
    if validate_resp.get('code') == 0:
        app_config_res = app_config_service.query_app_config_by_app_id(params.get('app_id'))
        if app_config_res.get('id'):
          return resp.resp_fail({},'请勿重复添加appid')
        else:
          if params.get('create_date') is None:
            params.update({'create_date': utils.if_empty_give_now_date()})
          if params.get('update_date') is None:
            params.update({'update_date': utils.if_empty_give_now_date()})
          return app_config_service.add_app_config(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])
