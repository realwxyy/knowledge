from flask import Flask, request
from src.config.config import DevelopmentConfig
from src.controller import resgister_all_bluePrint
from src.utils import db, resp, get_logger
import logging
import time

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

resgister_all_bluePrint(app)

# 可以使用 @app.before_request 切面编程的方式修饰方法
# 也可以使用 app.before_request(method) 的方式挂载方法


@app.before_request
def before_request():
    logger = get_logger()
    data = request.values
    url = request.base_url
    method = request.method
    params = []
    for k, v in data.items():
        params.append(str(k) + ':' + str(v))
    params_str = ','.join(params)
    now_time = time.time()
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now_time))
    request.start_time = now_time
    logger.info('请求开始--------请求地址:【' + url + '】,请求方式【' + method + '】,请求参数【' + params_str + '】,请求开始时间:【' + start_time + '】')


@app.after_request
def after_request(response, *args, **kwargs):
    # 跨域配置
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET,HEAD,OPTIONS,POST,PUT,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, common-token'
    logger = get_logger()
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
