from flask import Blueprint, request
from src.utils import resp, utils
from src.service import brand_service

gl_brand = Blueprint('brand', __name__, url_prefix='/brand')


@gl_brand.route('/brand', methods=['get'])
def brand_get():
    return resp.resp_succ({}, 'with developing....')


@gl_brand.route('/brand', methods=['post'])
def brand_post():
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['logo', 'code', 'zh_name'])
    if validate_resp.get('code') == 0:
        brand_resp = brand_service.query_brand_by_name(params.get('zh_name'))
        if brand_resp.get('id'):
            return resp.resp_fail({}, '请勿重复添加品牌：' + brand_resp.get('zh_name'))
        else:
            if params.get('create_date') is None:
                params.update({'create_date': utils.if_empty_give_now_date()})
            if params.get('update_date') is None:
                params.update({'update_date': utils.if_empty_give_now_date()})
            if params.get('is_delete') is None:
                params.update({'is_delete': 0})
            return brand_service.save_brand(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_brand.route('/brand', methods=['put'])
def brand_put():
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id', 'logo', 'code', 'zh_name'])
    if validate_resp.get('code') == 0:
        params.update({'update_date': utils.if_empty_give_now_date()})
        return brand_service.save_brand(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_brand.route('/brand', methods=['delete'])
def brand_delete():
    params = request.values.to_dict()
    id = params.get('id')
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id'])
    if validate_resp.get('code') == 0:
        brand_req = brand_service.query_brand_by_id(id)
        if brand_req:
          if brand_req.get('is_delete') != -1:
            params_req = {}
            params_req.update({'id': id})
            params_req.update({'update_date': utils.if_empty_give_now_date()})
            params_req.update({'is_delete': -1})
            return brand_service.save_brand(params_req)
          else:
            return resp.resp_fail({}, '该品牌已被删除，无法重复删除')
        else:
          return resp.resp_fail({}, '品牌信息查询失败，请确认品牌id是否正确')
    else:
        return resp.resp_fail({}, validate_resp['msg'])
