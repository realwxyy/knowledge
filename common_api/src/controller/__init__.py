from src.controller.user.user_controller import gl_user
from src.controller.token.token_controller import gl_token

def resgister_all_bluePrint(app):
  app.register_blueprint(gl_user)
  app.register_blueprint(gl_token)