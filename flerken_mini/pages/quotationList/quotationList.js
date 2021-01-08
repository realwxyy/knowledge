// quotationList.js
import { getQuotationList, testReturn } from '../../api/quotation'
import Dialog from '../../miniprogram_npm/@vant/weapp/dialog/dialog'
import { getStorageSync, wxRelaunch, wxNavigateTo } from '../../utils/common'
import { page_quotationList, page_authorization } from '../../config/page'

const data = {
  list: [],
  page: 0,
  size: 10,
  quotationName: '',
  checkedNum: 0,
  sharePopup: false,
  maxPage: 0,
  loading: true,
  showLoading: false,
  grant: false
}

const onLoad = function () { }

const onShow = function () {
  this.inialData()
  let showLoading = false
  // grant undefined 执行查询
  // grant true 执行查询
  // grant false 不执行
  if (!(getStorageSync('grant') === false)) {
    this.queryQuotationList()
  }
  this.setData({ grant: getStorageSync('grant') })
}

const inialData = function () {
  let checkedNum = 0
  this.setData({ checkedNum })
}

const queryQuotationList = function (nextPage = 0) {
  let page = this.data.page
  if (nextPage) {
    page = nextPage
  }
  let size = this.data.size
  let name = this.data.quotationName
  let maxPage = this.data.maxPage
  let loading = this.data.loading
  let showLoading = this.data.showLoading
  let total = 0
  let list = []
  getQuotationList({ page, size, name }).then(res => {
    if (res.code === 0) {
      list = res.data.list
      list.forEach(o => o.checked = false)
      total = res.data.total
      if (total % size > 0) {
        maxPage = parseInt(total / size) + 1
      } else {
        maxPage = parseInt(total / size)
      }
      if (page + 1 >= maxPage) {
        loading = false
        showLoading = false
      }
    } else {
      Dialog.alert({ title: '失败', message: res.message })
    }
    this.setData({ list, maxPage, loading, showLoading })
  })
}

const chooseQuotation = function (e) {
  let { id } = e.detail;
  let list = this.data.list
  let checkedNum = this.data.checkedNum
  list.forEach(o => {
    if (o.id === id) {
      o.checked = !o.checked
    }
  })
  let checkedList = list.filter(o => o.checked)
  checkedNum = checkedList.length
  this.setData({ list, checkedNum })
}

const setQuotationName = function (e) {
  this.setData({ quotationName: e.detail })
}

const quotationSearch = function (e) {
  this.queryQuotationList(0)
}

// const beforeShare = function () {
//   let list = this.data.list
//   let sharePopup = true
//   list = list.filter(o => o.checked)
//   this.setData({ list })
// }

const onShareAppMessage = function () {
  let list = this.data.list
  list = list.filter(o => o.checked)
  this.setData({ list })
  return { title: '测试', path: '测试' }
}

const loadQuotation = function () {
  let page = this.data.page
  let maxPage = this.data.maxPage
  if (page + 1 >= maxPage) {
    return
  }
  this.queryQuotationList(page + 1)
}

const toAuthorization = function () {
  wxNavigateTo(page_authorization)
}


const quotationList = {
  data,
  onLoad,
  onShow,
  inialData,
  chooseQuotation,
  queryQuotationList,
  setQuotationName,
  quotationSearch,
  onShareAppMessage,
  loadQuotation,
  toAuthorization
}

Page({ ...quotationList })
