from flask import Blueprint, request
from src.utils import resp, utils
from src.service import quotation_service

gl_quotation = Blueprint('quotation', __name__, url_prefix='/quotation')


@gl_quotation.route('/quotation', methods=['post'])
def quotation_post():
    '''
    @description method of add quotation
    @params params of add quotation
    @return please see message in methods
    '''
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['name', 'short_name'])
    if validate_resp.get('code') == 0:
        if params.get('create_date') is None:
            params.update({'create_date': utils.if_empty_give_now_date()})
        if params.get('update_date') is None:
            params.update({'update_date': utils.if_empty_give_now_date()})
        if params.get('is_delete') is None:
            params.update({'is_delete': 0})
        return quotation_service.save_quotation(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_quotation.route('/quotation', methods=['put'])
def quotation_put():
    '''
    @description update quotation info
    @params required: id ...
    @return please see return instance
    '''
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id', 'name', 'short_name'])
    if validate_resp.get('code') == 0:
        params.update({'update_date': utils.if_empty_give_now_date()})
        return quotation_service.save_quotation(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_quotation.route('/quotation', methods=['delete'])
def quotation_delete():
    '''
    @description delete quotation (only set quotation's field —— is_delete to -1)
    @params required: id
    @return please see return instance
    '''
    params = request.values.to_dict()
    id = params.get('id')
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id'])
    if validate_resp.get('code') == 0:
        quotation_req = quotation_service.query_quotation_by_id(id)
        if quotation_req:
            if quotation_req.get('is_delete') != -1:
                params_req = {}
                params_req.update({'id': id})
                params_req.update({'update_date': utils.if_empty_give_now_date()})
                params_req.update({'is_delete': -1})
                return quotation_service.save_quotation(params_req)
            else:
                return resp.resp_fail({}, '该报价单已被删除，无法重复删除')
        else:
            return resp.resp_fail({}, '商品信息查询失败，请确认商品id是否正确')
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_quotation.route('/quotation', methods=['get'])
def quotation_get():
    return resp.resp_succ({}, 'with developing....')