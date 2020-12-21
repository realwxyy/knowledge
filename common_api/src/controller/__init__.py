# from src.controller.test.test import t
from src.controller.user.user_controller import uc

def resgister_all_bluePrint(app):
  # app.register_blueprint(t)
  app.register_blueprint(uc)