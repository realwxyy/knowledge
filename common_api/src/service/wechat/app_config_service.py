from src.model import APP_CONFIG, APP_CONFIG_SCHEMA
from src.utils import db

def add_app_config(params):
  app_config_schema = APP_CONFIG_SCHEMA()
  app_config_req = app_config_schema.load(params, session=db.session)
  return app_config_schema.dump(app_config_req.save())

def query_app_config_by_app_id(app_id):
  app_config_schema = APP_CONFIG_SCHEMA()
  app_config_res = APP_CONFIG.query.filter_by(app_id = app_id).first()
  return app_config_schema.dump(app_config_res)
  
