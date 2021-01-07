from flask import Blueprint, request
from src.utils import resp
from src.service import app_config_service
from src.service import wechat_service
from src.utils import utils, third_session, wechat_login_required

gl_wechat = Blueprint('wechat', __name__, url_prefix='/wechat')


@gl_wechat.route('/add_app_config', methods=['post'])
def add_app_config():
    '''
    @ description add wx app config (appid,appsecret...)
    @ param app config
    @ param_type json in request
    @ return dict of added app_config
    @ return_type json
    '''
    params = utils.get_params(request)
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['app_id', 'app_secret'])
    if validate_resp.get('code') == 0:
        app_config_res = app_config_service.query_app_config_by_app_id(params.get('app_id'))
        if app_config_res.get('id'):
            return resp.resp_fail({}, '请勿重复添加appid')
        else:
            if params.get('create_date') is None:
                params.update({'create_date': utils.if_empty_give_now_date()})
            if params.get('update_date') is None:
                params.update({'update_date': utils.if_empty_give_now_date()})
            return app_config_service.add_app_config(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_wechat.route('/get_user', methods=['post'])
@wechat_login_required
def get_user():
    '''
    @ description 
        when people granted in mini program
        people can get the userInfo from database
        this method can update people's info too
        *** hold openid unique ***
    @ param dict of userInfo eg:nickName,avatar
    @ param_type json
    @ return wechatUser dict
    @ return type json
    '''
    params = utils.get_wechat_params(request)
    dict = third_session.decrypt_3rdsession_from_reqeust(request)
    open_id = dict.get('openid')
    params_req = wechat_service.get_wechat_user_by_open_id(open_id)
    nick_name = params.get('nickName')
    avatar = params.get('avatar')
    params_req.update({'open_id': open_id})
    params_req.update({'nick_name': nick_name})
    params_req.update({'avatar': avatar})
    if params_req.get('id'):
        params_req = utils.assign_put_fields(params_req)
    else:
        params_req = utils.assign_post_fields(params_req)
    return resp.resp_succ(wechat_service.save_wechat_user(params_req))
