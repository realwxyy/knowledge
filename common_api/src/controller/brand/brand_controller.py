from flask import Blueprint, request
from src.utils import resp, utils
from src.service import brand_service
from src.constant import CONS_COMMON, CONS_CONTROLLER, CONS_CONTROLLER, CONS_REQ_METHOD, CONS_MSG

gl_brand = Blueprint(CONS_CONTROLLER.BRAND, __name__, url_prefix=CONS_CONTROLLER.BRAND_PREFIX)


@gl_brand.route(CONS_CONTROLLER.BRAND_ROUTE, methods=CONS_REQ_METHOD.POST)
def brand_post():
    '''
    @description 新增品牌方法
    @params 新增品牌的参数
    @return 具体见返回参数中的 message
    '''
    params = request.values.to_dict()
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.BRAND_POST_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        brand_resp = brand_service.query_brand_by_name(params.get(CONS_CONTROLLER.ZH_NAME))
        if brand_resp.get(CONS_COMMON.ID):
            return resp.resp_fail({}, CONS_MSG.BRAND_DUPLICATION + brand_resp.get(CONS_CONTROLLER.ZH_NAME))
        else:
            if params.get(CONS_COMMON.CREATE_DATE) is None:
                params.update({CONS_COMMON.CREATE_DATE: utils.if_empty_give_now_date()})
            if params.get(CONS_COMMON.UPDATE_DATE) is None:
                params.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
            if params.get(CONS_COMMON.IS_DELETE) is None:
                params.update({CONS_COMMON.IS_DELETE: 0})
            return brand_service.save_brand(params)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_brand.route(CONS_CONTROLLER.BRAND_ROUTE, methods=CONS_REQ_METHOD.PUT)
def brand_put():
    '''
    @description update brand info
    @params required: id, logo, code, zh_name
    @return please see return instance
    '''
    params = request.values.to_dict()
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.BRAND_PUT_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        params.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
        return brand_service.save_brand(params)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_brand.route(CONS_CONTROLLER.BRAND_ROUTE, methods=CONS_REQ_METHOD.DELETE)
def brand_delete():
    '''
    @description delete brand (only set brand's field —— is_delete to -1)
    @params required: id
    @return please see return instance
    '''
    params = request.values.to_dict()
    id = params.get(CONS_COMMON.ID)
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.BRAND_DELETE_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        brand_req = brand_service.query_brand_by_id(id)
        if brand_req:
            if brand_req.get(CONS_COMMON.IS_DELETE) != -1:
                params_req = {}
                params_req.update({CONS_COMMON.ID: id})
                params_req.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
                params_req.update({CONS_COMMON.IS_DELETE: -1})
                return brand_service.save_brand(params_req)
            else:
                return resp.resp_fail({}, CONS_MSG.BRAND_DEDUPLICATION)
        else:
            return resp.resp_fail({}, CONS_MSG.BRAND_INFO_QUERY_FAIL)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_brand.route('/brand', methods=['get'])
def brand_get():
    return resp.resp_succ({}, 'with developing....')