import { code2session, getWechatMa } from '../api/login'
import { getWechatUser } from '../api/user'
import { requestUrl, appid } from '../config/path'
import { page_quotationList, page_authorization } from '../config/page'
import { checkSession, wxLogin, setStorageSync, getStorageSync, removeStorageSync, wxRelaunch, wxNavigateTo } from './common'
// const cookie = require('./weapp-cookie')

const wxLoginSucc = async res => {
  // debugger
  console.log(res)
  let { code } = res
  const data = await code2session({ code, appid })
  console.log(data)
  if(data.code === 0) {
    setStorageSync('wechat_third_session', data.data.third_session)
    login()
  }
  // .then(res => {
  //   console.log(res)
  //   if (res.code === 0) {
  //     setStorageSync('wechat_third_session', res.data.third_session)
  //     // wxRelaunch(page_quotationList)
  //   } else {
  //     console.log('wechat_third_session 生成失败....')
  //   }
  // })
}

const wxLoginFail = fail => { console.log(fail) }

export const login = () => {
  const wechatUserInfo = getStorageSync('wechatUserInfo')
  const { nickName, avatar } = wechatUserInfo
  if (nickName && avatar) {
    getWechatUser({ nickName, avatar }).then(res => {
      console.log(res)
      if (res.code === 0) {
        setStorageSync('userInfo', res.data)
        wxRelaunch(page_quotationList)
      }
    })
  } 
  // else {
  //   wxNavigateTo(page_authorization)
  // }
}

const reLogin = () => {
  // 微信登录
  wxLogin(wxLoginSucc, wxLoginFail)
  //登录
  // login()
  // const session_key = getStorageSync('session_key')
  // if (session_key) {
  //   login()
  // } else {
  //   wxLogin(wxLoginSucc, wxLoginFail)
  //   wxNavigateTo(page_authorization)
  // }
}

/**
 * 处理错误方法
 */
const handleError = res => {
  if (res.code === -1) {
    // 重新登录逻辑
    removeStorageSync('wechat_third_session')
    removeStorageSync('wechatUserInfo')
    removeStorageSync('userInfo')
    removeStorageSync('grant')
    // reLogin()
    wxLogin(wxLoginSucc, wxLoginFail)
  }
}

/**
 * wx.request 方法封装
 */
const reqeust = (url, data, header, method) => {
  url = requestUrl + url
  const wechat_third_session = getStorageSync('wechat_third_session')
  const grant = getStorageSync('grant')
  if (wechat_third_session && grant) {
    header = Object.assign({}, header, { 'wechat_third_session': wechat_third_session })
  }
  return new Promise((resolve, reject) => {
    wx.request({
      url, data: data, header, method,
      success: (res => {
        if (res.statusCode === 200) {
          resolve(res.data)
        } else {
          //接口请求失败 处理失败方法
          handleError(res.data)
        }
      }),
      fail: (res => reject(res))
    })
  })
}

/**
 * header
 */
const _header = { 'Content-Type': 'application/x-www-form-urlencoded' }

/**
 * GET类型的网络请求
 */
const getRequest = (url, data, header = _header) => {
  return reqeust(url, data, header, 'GET')
}

/**
 * DELETE类型的网络请求
 */
const deleteRequest = (url, data, header = _header) => {
  return reqeust(url, data, header, 'DELETE')
}

/**
 * PUT类型的网络请求
 */
const putRequest = (url, data, header = _header) => {
  return reqeust(url, data, header, 'PUT')
}

/**
 * POST类型的网络请求
 */
const postRequest = (url, data, header = _header) => {
  return reqeust(url, data, header, 'POST')
}

export { getRequest, deleteRequest, putRequest, postRequest }