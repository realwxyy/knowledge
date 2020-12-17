from src.controller.test.test import t

def resgister_test(app):
  app.register_blueprint(t)