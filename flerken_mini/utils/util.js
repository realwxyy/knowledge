import { setStorageSync, getStorageSync, wxLoginSync } from '../utils/common'
import { requestUrl, appid } from '../config/path'
import { code2session } from '../api/thirdSession'

const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

const checkThirdSession = () => {
  return getStorageSync('wechat_third_session') || ''
}

const getThirdSession = async (data) => {
  const res = await code2session(data)
  return res.data.third_session
}

const getLoginCode = async () => {
  const res = await wxLoginSync()
  console.log(res)
  return res.code
}

const setThirdSession = async () => {
  let data = await wxLoginSync()
  let code = data.code
  let res = await code2session({ code, appid })
  if (res.code === 0) {
    setStorageSync('wechat_third_session', res.data.third_session)
  }
}

module.exports = {
  formatTime,
  checkThirdSession,
  getThirdSession,
  getLoginCode,
  setThirdSession
}
