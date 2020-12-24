from src.controller.user.user_controller import gl_user
from src.controller.token.token_controller import gl_token
from src.controller.wechat.wechat_controller import gl_wechat
from src.controller.role.role_controller import gl_role

def resgister_all_bluePrint(app):
  app.register_blueprint(gl_user)
  app.register_blueprint(gl_token)
  app.register_blueprint(gl_wechat)
  app.register_blueprint(gl_role)