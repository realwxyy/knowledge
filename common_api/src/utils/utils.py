from src.constant import CONS_COMMON
import time
import json


def dict_not_empty(params, key_arr):
    '''
    @ desc 验证参数是否为空
    @ param  params 要验证的dict key_arr 要验证的key的list
    '''
    msg = []
    code = 0
    for k in key_arr:
        if not all([params.get(k)]):
            code = -1
            msg.append('参数 [' + k + '] 不可为空')
    return {'code': code, 'msg': msg}


def validate_dict_not_empty_with_key(params, key_arr):
    '''
    @ desc 验证参数是否为空
    @ param  params 要验证的dict key_arr 要验证的key的list
    '''
    msg = []
    code = 0
    for k in key_arr:
        if not all([params.get(k)]):
            code = -1
            msg.append('参数 [' + k + '] 不可为空')
    return {'code': code, 'msg': msg}


def if_empty_give_now_date(param=''):
    '''
    @ desc 如果值为空 就赋默认值 否则不做操作
    @ param param 要验证的值
    '''
    # 可否使用如下代码
    '''
    if not param:
      return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return param
    '''
    if not param:
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    else:
        return param


def get_params(req):
    '''
    @ desc package request params according to request method
    @ param reqeust
    @ param_type request
    @ return_type dict
    '''
    params = {}
    if req.method == 'GET' or req.method == 'DELETE':
        params = req.args.to_dict()
    if req.method == 'POST' or req.method == 'PUT':
        params = json.loads(req.data.decode('UTF-8'))
    return params


def assign_post_fields(item):
    '''
    @ desc assign common fields eg: create_date/udpate_date/is_delete
    @ param dict to be handled
    @ param_type dict
    @ return_type dict
    '''
    if not item.get(CONS_COMMON.CREATE_DATE):
        item.update({CONS_COMMON.CREATE_DATE: if_empty_give_now_date()})
    if not item.get(CONS_COMMON.UPDATE_DATE):
        item.update({CONS_COMMON.UPDATE_DATE: if_empty_give_now_date()})
    if not item.get(CONS_COMMON.IS_DELETE):
        item.update({CONS_COMMON.IS_DELETE: 0})
    return item


def assign_put_fields(item):
    '''
    @ desc assign save fields eg: update_date
    @ param dict to be handled
    @ param_type dict
    @ return_type dict
    '''
    item.update({CONS_COMMON.UPDATE_DATE: if_empty_give_now_date()})
    return item


def assign_delete_fields(item):
    '''
    @ desc assign save fields eg: update_date/is_delete
    @ param dict to be handled
    @ param_type dict
    @ return_type dict
    '''
    item.update({CONS_COMMON.UPDATE_DATE: if_empty_give_now_date()})
    item.update({CONS_COMMON.IS_DELETE: -1})
    return item