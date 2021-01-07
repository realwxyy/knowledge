import { getRequest, deleteRequest, putRequest, postRequest } from '../utils/request'
import { wechatMaSession, wechatMa, code2sessionUrl } from '../config/api'

export const getWechatMaSession = data => getRequest(wechatMaSession, data)

export const getWechatMa = (data, header) => getRequest(wechatMa, data, header)

export const code2session = data => getRequest(code2sessionUrl, data)