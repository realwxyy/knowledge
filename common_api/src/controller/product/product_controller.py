from flask import Blueprint, request
from src.utils import resp, utils
from src.service import product_service
from src.constant import CONS_COMMON, CONS_CONTROLLER, CONS_REQ_METHOD, CONS_MSG

gl_product = Blueprint(CONS_CONTROLLER.PRODUCT, __name__, url_prefix=CONS_CONTROLLER.PRODUCT_PREFIX)


@gl_product.route(CONS_CONTROLLER.PRODUCT_ROUTE, methods=CONS_REQ_METHOD.POST)
def product_post():
    '''
    @description method of add product
    @params params of add product
    @return please see message in 
    '''
    params = request.values.to_dict()
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.PRODUCT_POST_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        if params.get(CONS_COMMON.CREATE_DATE) is None:
            params.update({CONS_COMMON.CREATE_DATE: utils.if_empty_give_now_date()})
        if params.get(CONS_COMMON.UPDATE_DATE) is None:
            params.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
        if params.get(CONS_COMMON.IS_DELETE) is None:
            params.update({CONS_COMMON.IS_DELETE: 0})
        return product_service.save_product(params)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_product.route(CONS_CONTROLLER.PRODUCT_ROUTE, methods=CONS_REQ_METHOD.PUT)
def product_put():
    '''
    @description update product info
    @params required: id ...
    @return please see return instance
    '''
    params = request.values.to_dict()
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.PRODUCT_PUT_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        params.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
        return product_service.save_product(params)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_product.route(CONS_CONTROLLER.PRODUCT_ROUTE, methods=CONS_REQ_METHOD.DELETE)
def product_delete():
    '''
    @description delete product (only set product's field —— is_delete to -1)
    @params required: id
    @return please see return instance
    '''
    params = request.values.to_dict()
    id = params.get(CONS_COMMON.ID)
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.PRODUCT_DELETE_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        product_req = product_service.query_product_by_id(id)
        if product_req:
            if product_req.get(CONS_COMMON.IS_DELETE) != -1:
                params_req = {}
                params_req.update({CONS_COMMON.ID: id})
                params_req.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
                params_req.update({CONS_COMMON.IS_DELETE: -1})
                return product_service.save_product(params_req)
            else:
                return resp.resp_fail({}, CONS_MSG.PRODUCT_DEDUPLICATION)
        else:
            return resp.resp_fail({}, CONS_MSG.PRODUT_INFO_QUERY_FAIL)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_product.route('/product', methods=['get'])
def product_get():
    return resp.resp_succ({}, 'with developing....')