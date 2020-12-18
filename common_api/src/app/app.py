from flask import Flask, jsonify, current_app, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import ImmutableMultiDict, CombinedMultiDict
from src.config.config import DevelopmentConfig
from src.controller import resgister_test
from src.utils import db, response_with, resp
import logging
import time

app = Flask(__name__)
app_ctx = app.app_context()
app_ctx.push()
logger = current_app.logger
logger.setLevel(logging.INFO)
app.config.from_object(DevelopmentConfig)

resgister_test(app)

# 可以使用 @app.before_request 切面编程的方式修饰方法
# 也可以使用 app.before_request(method) 的方式挂载方法


@app.before_request
def before_request():
    data = request.values
    url = request.base_url
    method = request.method
    params = []
    for k, v in data.items():
        params.append(str(k) + ':' +str(v))
    params_str = ','.join(params)
    now_time = time.time()
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now_time))
    request.start_time = now_time
    logger.info('请求开始--------请求地址:【' + url + '】,请求方式【' + method + '】,请求参数【' + params_str + '】,请求开始时间:【' + start_time + '】')


@app.after_request
def after_request(response, *args, **kwargs):
    # logger.info('after-request')
    # time.sleep(2)
    start_time = request.start_time
    now_time = time.time()
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now_time))
    diff_time = now_time - start_time
    logger.info('请求结束--------请求结束时间:【' + end_time + '】,请求耗时【' + str(round(diff_time, 3)) + 's】')
    return response

@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return resp.resp_fail()

@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return resp.resp_err()

@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return resp.resp_not_found()

db.init_app(app)
