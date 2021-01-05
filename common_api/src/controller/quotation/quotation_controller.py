from flask import Blueprint, request
from src.utils import resp, utils, wechat_login_required
from src.service import quotation_service
from src.constant import CONS_COMMON, CONS_CONTROLLER, CONS_REQ_METHOD, CONS_MSG
import json

gl_quotation = Blueprint('quotation', __name__, url_prefix='/quotation')


@gl_quotation.route('/quotation', methods=CONS_REQ_METHOD.POST)
# @wechat_login_required
def quotation_post():
    '''
    @description method of add quotation
    @params params of add quotation
    @return please see message in methods
    '''
    params = utils.get_params(request)
    req_quotation = params.get('quotation')
    req_products = params.get('products')
    validate_resp = utils.validate_dict_not_empty_with_key(req_quotation, CONS_CONTROLLER.QUOTATION_POST_PARAMS)
    if validate_resp.get('code') == 0:
        req_quotation = utils.assign_post_fields(req_quotation)
        quotation = quotation_service.save_quotation(req_quotation)
        if req_products and len(req_products) > 0:
            for item in req_products:
                item.update({'quotation_id': quotation.get('id')})
                item = utils.assign_post_fields(item)
            quotation_service.save_quotation_product(req_products)
            return resp.resp_succ()
        else:
            return resp.resp_fail({}, 'products参数验证失败')
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_quotation.route('/quotation', methods=CONS_REQ_METHOD.PUT)
# @wechat_login_required
def quotation_put():
    '''
    @description update quotation info
    @params required: id ...
    @return please see return instance
    '''
    params = utils.get_params(request)
    req_quotation = params.get('quotation')
    req_products = params.get('products')
    validate_resp = utils.validate_dict_not_empty_with_key(req_quotation, CONS_CONTROLLER.QUOTATION_PUT_PARAMS)
    if validate_resp.get('code') == 0:
        req_quotation.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
        quotation_service.save_quotation(req_quotation)
        quotation_service.save_quotation_product(req_products)
        return resp.resp_succ(message='修改成功')
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_quotation.route('/quotation', methods=CONS_REQ_METHOD.DELETE)
# @wechat_login_required
def quotation_delete():
    '''
    @description delete quotation (only set quotation's field is_delete to -1)
    @params required: id
    @return please see return instance
    '''
    params = utils.get_params(request)
    id = params.get(id)
    validate_resp = utils.validate_dict_not_empty_with_key(params, CONS_CONTROLLER.QUOTATION_DELETE_PARAMS)
    if validate_resp.get(CONS_COMMON.MSG) == 0:
        quotation_req = quotation_service.query_quotation_by_id(id)
        if quotation_req:
            if quotation_req.get(CONS_COMMON.IS_DELETE) != -1:
                params_req = {}
                params_req.update({'id': id})
                quotation_service.del_products(params_req)
                params_req = utils.assign_delete_fields(params_req)
                quotation_service.save_quotation(params_req)
            else:
                return resp.resp_fail({}, CONS_MSG.QUOTATION_DEDUPLICATION)
        else:
            return resp.resp_fail({}, CONS_MSG.QUOTATION_INFO_QUERY_FAIL)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_quotation.route(CONS_CONTROLLER.QUOTATION_WECHAT_LIST, methods=CONS_REQ_METHOD.GET)
@wechat_login_required
def mini_list():
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, CONS_CONTROLLER.QUOTATION_WECHAT_LIST_GET_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        return quotation_service.mini_queryList(params)


@gl_quotation.route(CONS_CONTROLLER.QUOTATION_ADMIN_LIST, methods=CONS_REQ_METHOD.GET)
def admin_list():
    params = request.values.to_dict()
    return quotation_service.admin_list(params)


@gl_quotation.route('/save_product_to_quotation', methods=['POST'])
def save_procut_to_quotation():
    params = request.values.to_dict()
    return quotation_service.save_product_to_quotation(params)


@gl_quotation.route('/test', methods=['get', 'post', 'put', 'delete', 'patch', 'head', 'options'])
def test():
    quotation_service.del_products({'id': 14})
    return resp.resp_succ()