// quotationList.js
import { getQuotationList, testReturn } from '../../api/quotation'
import Dialog from '../../miniprogram_npm/@vant/weapp/dialog/dialog'
import { getStorageSync, wxRelaunch, wxNavigateTo } from '../../utils/common'
import { page_quotationList, page_authorization } from '../../config/page'

const data = {
  list: [],
  page: 1,
  size: 10,
  quotationName: '',
  checkedNum: 0,
  sharePopup: false,
  maxPage: 1,
  loading: true,
  showLoading: true,
  grant: ''
}

const onLoad = function () { }

const onShow = function () {
  this.inialData()
  // grant undefined 执行查询
  // grant true 执行查询
  // grant false 不执行
  let grant = getStorageSync('grant')
  if (grant) {
    this.queryQuotationList()
  }
  this.setData({ grant })
}

const inialData = function () {
  let checkedNum = 0
  let list = []
  let page = 1
  this.setData({ checkedNum, list, page })
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
  let list = this.data.list
  getQuotationList({ page, size, name }).then(res => {
    if (res.code === 0) {
      list = list.concat(res.data.list)
      list.forEach(o => {
        if (!o.checked) {
          o.checked = false
        }
      })
      total = res.data.total
      if (total % size > 0) {
        maxPage = parseInt(total / size) + 1
      } else {
        maxPage = parseInt(total / size)
      }
      if (page >= maxPage) {
        loading = false
        showLoading = false
      } else {
        page = page + 1
        loading = true
        showLoading = true
      }
    } else {
      Dialog.alert({ title: '失败', message: res.message })
    }
    this.setData({ list, maxPage, loading, showLoading, page })
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
  let list = []
  let loading = true
  let showLoading = true
  this.setData({ list, showLoading, loading })
  this.queryQuotationList(1)
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
  let showLoading = this.data.showLoading
  if (showLoading) {
    this.queryQuotationList()
  }
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
