// quotationList.js
import { getQuotationList, testReturn } from '../../api/quotation'
import Dialog from '../../miniprogram_npm/@vant/weapp/dialog/dialog'

const data = {
  list: [],
  page: 0,
  size: 10,
  quotationName: '',
  checkedNum: 0,
  sharePopup: false
}

const onLoad = function () { }

const onShow = function () {
  this.inialData()
  this.queryQuotationList()
}

const inialData = function () {
  let checkedNum = 0
  this.setData({ checkedNum })
}

const queryQuotationList = function (search = false) {
  let page = this.data.page
  if (search) {
    page = 0
  }
  let size = this.data.size
  let name = this.data.quotationName
  let list = []
  getQuotationList({ page, size, name }).then(res => {
    if (res.code === 0) {
      list = res.data.list
      list.forEach(o => o.checked = false)
    } else {
      Dialog.alert({ title: '失败', message: res.message })
    }
    this.setData({ list })
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
  this.queryQuotationList(true)
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


const quotationList = {
  data,
  onLoad,
  onShow,
  inialData,
  chooseQuotation,
  queryQuotationList,
  setQuotationName,
  quotationSearch,
  onShareAppMessage
}

Page({ ...quotationList })
