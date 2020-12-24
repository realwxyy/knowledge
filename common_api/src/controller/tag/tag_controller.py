from flask import Blueprint, request
from src.utils import resp, utils
from src.service import tag_service

gl_tag = Blueprint('tag', __name__, url_prefix='/tag')

@gl_tag.route('save_tag', methods=['post', 'put'])
def save_role():
    params = request.values.to_dict()
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['name'])
    if validate_resp.get('code') == 0:
        role_resp = tag_service.query_tag_by_name(params.get('name'))
        if role_resp.get('id') and not params.get('id'):
            return resp.resp_fail({}, '请勿重复添加标签：' + role_resp.get('name'))
        else:
            if params.get('create_date') is None:
                if not params.get('id'):
                  params.update({'create_date': utils.if_empty_give_now_date()})
            if params.get('update_date') is None:
                params.update({'update_date': utils.if_empty_give_now_date()})
            if params.get('is_delete') is None:
                params.update({'is_delete': 0})
            return tag_service.save_tag(params)
    else:
        return resp.resp_fail({}, validate_resp['msg'])


@gl_tag.route('query_tags', methods=['get'])
def query_tags():
    return resp.resp_succ(tag_service.query_tags())


@gl_tag.route('delete_tag', methods=['delete'])
def delete_tag():
  params = request.values.to_dict()
  service_resp = tag_service.delete_tag(params)
  if service_resp.get('code') == 0:
    return resp.resp_succ({}, service_resp.get('message'))
  else:
    return resp.resp_fail({}, service_resp.get('message'))