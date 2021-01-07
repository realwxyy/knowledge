import { getRequest, deleteRequest, putRequest, postRequest } from '../utils/request'
import { backUser } from '../config/api'

export const getWechatUser = data => postRequest(backUser, data)