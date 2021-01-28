import axios, { AxiosRequestConfig, AxiosResponse } from 'axios'
import { message, Modal } from 'antd'
import { requestConfig } from '@config/path'
import { clear_token } from '@redux/actions'
import store from '@redux/store'

let logoutCount = 0

const service = axios.create({
  baseURL: requestConfig, // url = base url + request url
  timeout: 5000,
  withCredentials: false, // send cookies when cross-domain requests
})

// Request interceptors
service.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    // config.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8';
    // config.headers['Access-Control-Allow-Origin'] = '*';
    // config.headers['Access-Control-Allow-Headers'] = 'Authorization,Origin, X-Requested-With, Content-Type, Accept';
    // config.headers['Access-Control-Allow-Methods'] = 'GET,POST';
    // Add X-Access-Token header to every request, you can add other custom headers here
    let storage: any = store.getState()
    if (storage.token) {
      config.headers['common-token'] = storage.token
    }
    return config
  },
  (error: string) => {
    Promise.reject(error)
  }
)

// Response interceptors
service.interceptors.response.use(
  (response: AxiosResponse<any>) => {
    const res = response.data
    if (res.code !== 0) {
      if (res.code === 1) {
        message.error({
          content: res.message || 'Error',
          duration: 5,
        })
        return response.data
      } else {
        message.error({
          content: res.message || 'Error',
          duration: 5,
        })
        return Promise.reject(new Error(res.message || 'Error'))
      }
    } else {
      return response.data
    }
  },
  (error: any) => {
    let errorInfo = error.response
    let msg
    if (!errorInfo) {
      const {
        request: { statusText, status },
        config,
      } = JSON.parse(JSON.stringify(error))
      errorInfo = {
        statusText,
        status,
        request: { responseURL: config.url },
      }
      msg = status + '：' + errorInfo.statusText
    } else {
      if (error.response.data.code === -1) {
        if (logoutCount === 0) {
          Modal.confirm({
            content: '你已被登出，可以取消继续留在该页面，或者重新登录, 确定登出?',
            okText: '重新登录',
            cancelText: '取消',
            onOk: () => {
              logoutCount = 0
              localStorage.clear()
              sessionStorage.clear()
              store.dispatch(clear_token())
              // window.location.reload()
              const { host, protocol } = window.location
              let url = protocol + '//' + host + '/#/login'
              console.log(url)
              window.location.replace(url)
              msg = error.response.data.message
            },
          })
          logoutCount++
          return Promise.reject(msg)
        }
      } else if (errorInfo.data.code === 1 || errorInfo.data.code === 2) {
        msg = errorInfo.data.message
      } else {
        msg = error.response.data.status + '：' + error.response.data.message
      }
    }
    message.error({
      content: msg,
      duration: 5,
    })
    return Promise.reject(msg)
  }
)

export default service
