from flask import Blueprint, request
from src.utils import resp, utils
from src.service import product_service

gl_product = Blueprint('product', __name__, url_prefix='/product')


@gl_product.route('/product', methods=['post'])
def product_post():
    '''
    @description method of add product
    @params params of add product
    @return please see message in 
    '''
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['brand_id', 'name', 'main_img', 'standard_price', 'in_stock', 'promotional_red_line_price', 'box_gauge', 'gross_weight', 'box_gross_weight'])
    if validate_resp.get('code') == 0:
        if params.get('create_date') is None:
            params.update({'create_date': utils.if_empty_give_now_date()})
        if params.get('update_date') is None:
            params.update({'update_date': utils.if_empty_give_now_date()})
        if params.get('is_delete') is None:
            params.update({'is_delete': 0})
        return product_service.save_product(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_product.route('/product', methods=['put'])
def product_put():
    '''
    @description update product info
    @params required: id ...
    @return please see return instance
    '''
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id', 'brand_id', 'name', 'main_img', 'standard_price', 'in_stock', 'promotional_red_line_price', 'box_gauge', 'gross_weight', 'box_gross_weight'])
    if validate_resp.get('code') == 0:
        params.update({'update_date': utils.if_empty_give_now_date()})
        return product_service.save_product(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_product.route('/product', methods=['delete'])
def product_delete():
    '''
    @description delete product (only set product's field —— is_delete to -1)
    @params required: id
    @return please see return instance
    '''
    params = request.values.to_dict()
    id = params.get('id')
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id'])
    if validate_resp.get('code') == 0:
        product_req = product_service.query_product_by_id(id)
        if product_req:
            if product_req.get('is_delete') != -1:
                params_req = {}
                params_req.update({'id': id})
                params_req.update({'update_date': utils.if_empty_give_now_date()})
                params_req.update({'is_delete': -1})
                return product_service.save_product(params_req)
            else:
                return resp.resp_fail({}, '该商品已被删除，无法重复删除')
        else:
            return resp.resp_fail({}, '商品信息查询失败，请确认商品id是否正确')
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_product.route('/product', methods=['get'])
def product_get():
    return resp.resp_succ({}, 'with developing....')