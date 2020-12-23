import time


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
