import { getRequest, deleteRequest, putRequest, postRequest } from '../utils/request'
import { api_code2session } from '../config/api'

export const code2session = (data) => getRequest(api_code2session, data)