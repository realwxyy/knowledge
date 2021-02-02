from src.controller.user.user_controller import gl_user
from src.controller.token.token_controller import gl_token
from src.controller.wechat.wechat_controller import gl_wechat
from src.controller.role.role_controller import gl_role
from src.controller.tag_controller import gl_tag
from src.controller.brand_controller import gl_brand
from src.controller.product.product_controller import gl_product
from src.controller.quotation_controller import gl_quotation
from src.controller.admin_user_controller import gl_admin_user
from src.controller.login_controller import gl_login
from src.controller.upload_controller import gl_upload


def resgister_all_bluePrint(app):
    app.register_blueprint(gl_user)
    app.register_blueprint(gl_token)
    app.register_blueprint(gl_wechat)
    app.register_blueprint(gl_role)
    app.register_blueprint(gl_tag)
    app.register_blueprint(gl_brand)
    app.register_blueprint(gl_product)
    app.register_blueprint(gl_quotation)
    app.register_blueprint(gl_admin_user)
    app.register_blueprint(gl_login)
    app.register_blueprint(gl_upload)
