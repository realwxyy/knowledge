

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    #    SQLALCHEMY_DATABASE_URI = <Production DB RUL>
    pass


class DevelopmentConfig(Config):
    SECRET_KEY = 'wxyy'
    username = 'root'
    password = 123456
    database = 'common_api'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@127.0.0.1:3306/%s' % (
        username, password, database)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_ENABLED = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['WTF_CSRF_ENABLED'] = False


class TestingConfig(Config):
    TESTING = True
#    SQLALCHEMY_DATABASE_URI = <Testing DB URL>
    SQLALCHEMY_ECHO = False
