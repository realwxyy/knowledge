// authorization.js
import { setStorageSync, getStorageSync, wxRelaunch } from '../../utils/common'
import { page_quotationList } from '../../config/page'
import { login } from '../../utils/request'
import { queryAllUser } from '../../api/quotation'

const data = {}

const onLoad = () => { }

const onShow = () => { }

const getUserInfo = res => {
  let { userInfo } = res.detail
  console.log(userInfo)
  if (userInfo) {
    userInfo.avatar = userInfo.avatarUrl
    console.log(userInfo)
    setStorageSync('wechatUserInfo', userInfo)
    setStorageSync('grant', true)
    login()
  } else {
    console.log('需要授权才能查看报价单等信息')
    setStorageSync('grant', false)
    wxRelaunch(page_quotationList)
    
  }
}

const getUsers = res => {
  queryAllUser().then(res => {
    console.log(res)
  })
}

const cancelGrant = () => {
  setStorageSync('grant', false)
  wxRelaunch(page_quotationList)
}

const authorization = { data, onLoad, onShow, getUserInfo, getUsers, cancelGrant }

Page({ ...authorization })
