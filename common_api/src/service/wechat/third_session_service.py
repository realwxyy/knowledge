from src.utils import third_session

def get_third_session(params):
  session_res = third_session.gen_3rdsession(params)
  return {'third_session': session_res}

def get_openId_and_session_key(param):
  return third_session.decrypt_3rdsession(param)