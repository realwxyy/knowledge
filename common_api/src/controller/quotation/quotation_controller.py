from flask import Blueprint, request
from src.utils import resp, utils, wechat_login_required
from src.service import quotation_service
from src.constant import CONS_COMMON, CONS_CONTROLLER, CONS_REQ_METHOD, CONS_MSG

gl_quotation = Blueprint(CONS_CONTROLLER.QUOTATION, __name__, url_prefix=CONS_CONTROLLER.QUOTATION_PREFIXX)


@gl_quotation.route(CONS_CONTROLLER.QUOTATION_ROUTE, methods=CONS_REQ_METHOD.POST)
# @wechat_login_required
def quotation_post():
    '''
    @description method of add quotation
    @params params of add quotation
    @return please see message in methods
    '''
    params = request.values.to_dict()
    # validate_resp = utils.validate_dict_not_empty_with_key(params, CONS_CONTROLLER.QUOTATION_POST_PARAMS)
    validate_resp = utils.validate_dict_not_empty_with_key(params, [])
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        if not params.get(CONS_COMMON.CREATE_DATE):
            params.update({CONS_COMMON.CREATE_DATE: utils.if_empty_give_now_date()})
        if not params.get(CONS_COMMON.UPDATE_DATE):
            params.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
        if not params.get(CONS_COMMON.IS_DELETE):
            params.update({CONS_COMMON.IS_DELETE: 0})
        # quotation_base = quotation_service.save_quotation(params)
        products = params.get('products')
        if products and len(products) > 0:
            quotation_products = quotation_service.save_quotation_product(products)
        # return quotation_service.save_quotation(params)
        return resp.resp_succ()
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_quotation.route(CONS_CONTROLLER.QUOTATION_ROUTE, methods=CONS_REQ_METHOD.PUT)
# @wechat_login_required
def quotation_put():
    '''
    @description update quotation info
    @params required: id ...
    @return please see return instance
    '''
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, CONS_CONTROLLER.QUOTATION_PUT_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        params.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
        return quotation_service.save_quotation(params)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_quotation.route(CONS_CONTROLLER.QUOTATION_ROUTE, methods=CONS_REQ_METHOD.DELETE)
# @wechat_login_required
def quotation_delete():
    '''
    @description delete quotation (only set quotation's field is_delete to -1)
    @params required: id
    @return please see return instance
    '''
    params = request.values.to_dict()
    id = params.get(CONS_COMMON.ID)
    validate_resp = utils.validate_dict_not_empty_with_key(params, CONS_CONTROLLER.QUOTATION_DELETE_PARAMS)
    if validate_resp.get(CONS_COMMON.MSG) == 0:
        quotation_req = quotation_service.query_quotation_by_id(id)
        if quotation_req:
            if quotation_req.get(CONS_COMMON.IS_DELETE) != -1:
                params_req = {}
                params_req.update({CONS_COMMON.ID: id})
                params_req.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
                params_req.update({CONS_COMMON.IS_DELETE: -1})
                return quotation_service.save_quotation(params_req)
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

@gl_quotation.route('/test', methods=['get'])
def test():
    quotation_products = quotation_service.save_quotation_product({})
    return {}