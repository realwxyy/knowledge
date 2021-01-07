export const checkSession = (success, fail) => wx.checkSession({ success, fail })
export const wxLogin = (success, fail) => wx.login({ success, fail })
export const setStorageSync = (key, value) => wx.setStorageSync(key, value)
export const getStorageSync = key => wx.getStorageSync(key)
export const removeStorageSync = key => wx.removeStorageSync(key)
export const getStorageInfoSync = () => wx.getStorageInfoSync()
export const wxRelaunch = url => wx.reLaunch({ url })
export const wxNavigateTo = url => wx.navigateTo({ url });