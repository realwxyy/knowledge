from flask import current_app
import logging


def get_logger():
    logger = current_app.logger
    logger.setLevel(logging.INFO)
    return logger
    # print('执行了')
    # return ''
