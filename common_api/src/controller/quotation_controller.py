from flask import Blueprint, request
from src.utils import resp, utils, wechat_login_required
from src.service import quotation_service
from src.constant import CONS_COMMON, CONS_CONTROLLER, CONS_REQ_METHOD, CONS_MSG

gl_quotation = Blueprint('quotation', __name__, url_prefix='/quotation')


@gl_quotation.route('/quotation', methods=CONS_REQ_METHOD.POST)
# @wechat_login_required
def quotation_post():
    '''
    @ description method of add quotation
    @ param params of add quotation
    @ param_type dict in request
    @ return please see message in methods
    @ return_type json
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
    @ description update quotation info
    @ params required: id ...
    @ param_type dict in request
    @ return please see return instance
    @ return_type json
    '''
    params = utils.get_params(request)
    req_quotation = params.get('quotation')
    req_products = params.get('products')
    tags = req_quotation.get('tags')
    if tags:
        del req_quotation['tags']  # 该种方法是否合规 不合规请一律修改为（处理参数）
    validate_resp = utils.validate_dict_not_empty_with_key(req_quotation, CONS_CONTROLLER.QUOTATION_PUT_PARAMS)
    if validate_resp.get('code') == 0:
        req_quotation.update({CONS_COMMON.UPDATE_DATE: utils.if_empty_give_now_date()})
        quotation_service.save_quotation(req_quotation)
        if tags:
            if len(tags) > 0:
                tags_req = []
                for tag in tags:
                    item = {}
                    item.update({'quotation_id': req_quotation.get('id')})
                    item.update({'tag_id': int(tag.get('tag_id'))})
                    item = utils.assign_post_fields(item)
                    tags_req.append(item)
                quotation_service.del_tags(req_quotation)
                quotation_service.save_quotation_tag(tags_req)
        # 删除所有产品 再添加用户传过来的产品集合（该方式性能问题严重！）
        if req_products and len(req_products) > 0:
            for item in req_products:
                item.update({'quotation_id': req_quotation.get('id')})
                item = utils.assign_post_fields(item)
        quotation_service.del_products(req_quotation)
        quotation_service.save_quotation_product(req_products)
        return resp.resp_succ(message='修改成功')
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_quotation.route('/quotation', methods=CONS_REQ_METHOD.DELETE)
# @wechat_login_required
def quotation_delete():
    '''
    @ description delete quotation (only set quotation's field is_delete to -1)
    @ params required: id
    @ param_type  dict in reqeust
    @ return please see return instance
    @ return_type json
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


@gl_quotation.route('/mini_list', methods=CONS_REQ_METHOD.GET)
@wechat_login_required
def mini_list():
    '''
    @ description wechat mini program get quotation list
    @ param json in request eg: page/size/name
    @ param_type json
    @ return json of quotation list
    @ return_type json
    '''
    params = utils.get_params(request)
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['page', 'size'])
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        return resp.resp_succ(quotation_service.mini_queryList(params))
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_quotation.route('/admin_list', methods=CONS_REQ_METHOD.GET)
def admin_list():
    '''
    @ description background system get quotation list
    @ param json in request eg: page/size/code(fuzzy query)/name(fuzzy query)
    @ param_type json in reqeust
    @ return json of quotation list
    @ return_type json
    '''
    params = utils.get_params(request)
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['page', 'size'])
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        return resp.resp_succ(quotation_service.admin_list(params))
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))