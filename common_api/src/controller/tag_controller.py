from flask import Blueprint, request
from src.utils import resp, utils
from src.service import tag_service

gl_tag = Blueprint('tag', __name__, url_prefix='/tag')


@gl_tag.route('tag', methods=['post'])
def tag_post():
    params = utils.get_params(request)
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['name'])
    if validate_resp.get('code') == 0:
        tag_resp = tag_service.query_tag_by_name(params.get('name'))
        if tag_resp.get(id):
            return resp.resp_fail({}, '请勿重复添加标签：' + tag_resp.get('name'))
        else:
            params = utils.assign_post_fields(params)
            tag_service.save_tag(params)
            return resp.resp_succ()
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_tag.route('tag', methods=['put'])
def tag_put():
    params = utils.get_params(request)
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id'])
    if validate_resp.get('code') == 0:
        params = utils.assign_put_fields(params)
        tag_service.save_tag(params)
        return resp.resp_succ()
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_tag.route('tag', methods=['delete'])
def tag_delete():
    params = utils.get_params(request)
    print(params)
    validate_resp = utils.validate_dict_not_empty_with_key(params, ['id'])
    if validate_resp.get('code') == 0:
        params = utils.assign_delete_fields(params)
        tag_service.save_tag(params)
        return resp.resp_succ()
    else:
        return resp.resp_fail({}, validate_resp.get('msg'))


@gl_tag.route('query_tags', methods=['get'])
def query_tags():
    return resp.resp_succ(tag_service.query_tags())
