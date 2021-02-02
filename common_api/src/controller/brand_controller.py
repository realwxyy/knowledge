from flask import Blueprint, request
from src.utils import resp, utils, login_required
from src.service import brand_service, brand_tag_service
from src.constant import CONS_COMMON, CONS_CONTROLLER, CONS_REQ_METHOD, CONS_MSG

gl_brand = Blueprint('brand', __name__, url_prefix='/brand')


@gl_brand.route('/brand', methods=['get'])
def brand_get():
    '''
    @ description get brand info
    @ params required: id ...
    @ param_type dict in request
    @ return please see return instance
    @ return_type json
    '''
    params = utils.get_params(request)
    validate_resp = utils.dict_not_empty(params, ['id'])
    if validate_resp.get('code') == 0:
        brand = brand_service.query_brand_by_id(params.get('id'))
        brand_tags = brand_tag_service.query_brand_tags_by_brand_id(params.get('id'))
        brand.update({'tags': brand_tags})
        return resp.resp_succ(brand)
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_brand.route('/brand', methods=['post'])
def brand_post():
    '''
    @description 新增品牌方法
    @params 新增品牌的参数
    @return 具体见返回参数中的 message
    '''
    params = utils.get_params(request)
    tags = params.get('tags')
    if tags:
        del params['tags']  # 该种方法是否合规 不合规请一律修改为（处理参数）
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.BRAND_POST_PARAMS)
    if validate_resp.get('code') == 0:
        brand_resp = brand_service.query_brand_by_name(params.get(CONS_CONTROLLER.ZH_NAME))
        if brand_resp.get(CONS_COMMON.ID):
            return resp.resp_fail({}, CONS_MSG.BRAND_DUPLICATION + brand_resp.get(CONS_CONTROLLER.ZH_NAME))
        else:
            params = utils.assign_post_fields(params)
            brand = brand_service.save_brand(params)
            if tags:
                if len(tags) > 0:
                    tags_req = []
                    for tag in tags:
                        item = {}
                        item.update({'brand_id': brand.get('id')})
                        item.update({'tag_id': int(tag)})
                        item = utils.assign_post_fields(item)
                        tags_req.append(item)
                    brand_tag_service.save_brand_tag(tags_req)
            return resp.resp_succ({}, '添加成功')
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_brand.route('/brand', methods=['put'])
def brand_put():
    '''
    @description update brand info
    @params required: id, logo, code, zh_name
    @return please see return instance
    '''
    params = utils.get_params(request)
    tags = params.get('tags')
    if tags:
        del params['tags']  # 该种方法是否合规 不合规请一律修改为（处理参数）
    validate_resp = utils.dict_not_empty(params, CONS_CONTROLLER.BRAND_PUT_PARAMS)
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        params = utils.assign_put_fields(params)
        brand = brand_service.save_brand(params)
        if tags:
            if len(tags) > 0:
                tags_req = []
                for tag in tags:
                    item = {}
                    item.update({'brand_id': brand.get('id')})
                    item.update({'tag_id': int(tag)})
                    item = utils.assign_post_fields(item)
                    tags_req.append(item)
                brand_tag_service.delete_tag_with_brand_id(brand.get('id'))
                brand_tag_service.save_brand_tag(tags_req)
        return resp.resp_succ({}, '修改成功')
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_brand.route('brand', methods=['delete'])
def brand_delete():
    '''
    @description delete brand (only set brand's field —— is_delete to -1)
    @params required: id
    @return please see return instance
    '''
    params = utils.get_params(request)
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
                brand_service.save_brand(params_req)
                return resp.resp_succ({}, '删除成功')
            else:
                return resp.resp_fail({}, CONS_MSG.BRAND_DEDUPLICATION)
        else:
            return resp.resp_fail({}, CONS_MSG.BRAND_INFO_QUERY_FAIL)
    else:
        return resp.resp_fail({}, validate_resp.get(CONS_COMMON.MSG))


@gl_brand.route('/admin_list', methods=['get'])
@login_required
def admin_list():
    params = utils.get_params(request)
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['page', 'size'])
    if validate_resp.get(CONS_COMMON.CODE) == 0:
        return resp.resp_succ(brand_service.admin_list(params))
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))