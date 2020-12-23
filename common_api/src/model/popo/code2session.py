class Code2Session(object):
  def __init__(self, params):
    self.appid = params.get('appid')
    self.secret = params.get('secret')
    self.js_code = params.get('code')
    self.grant_type = 'authorization_code'

