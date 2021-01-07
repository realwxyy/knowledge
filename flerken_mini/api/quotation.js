import { getRequest, deleteRequest, putRequest, postRequest } from '../utils/request'
import { quotationUrl, testReturnUrl, getUsers } from '../config/api'

export const getQuotationList = (data) => getRequest(quotationUrl, data)
export const testReturn = () => getRequest(testReturnUrl)
export const queryAllUser = () => getRequest(getUsers)