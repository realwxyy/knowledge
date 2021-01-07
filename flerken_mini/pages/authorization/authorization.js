// authorization.js
import { setStorageSync, getStorageSync } from '../../utils/common'
import { login } from '../../utils/request'
import { queryAllUser } from '../../api/quotation'

const data = {}

const onLoad = () => { }

const onShow = () => { }

const getUserInfo = res => {
  let { userInfo } = res.detail
  if (userInfo) {
    userInfo.avatar = userInfo.avatarUrl
    console.log(userInfo)
    setStorageSync('wechatUserInfo', userInfo)
    login()
  } else {
    console.log('需要授权才能查看报价单等信息')
  }
}

const getUsers = res => {
  queryAllUser().then(res => {
    console.log(res)
  })
}

const authorization = { data, onLoad, onShow, getUserInfo, getUsers }

Page({ ...authorization })
