import { oss } from '../../config/path'

const properties = {
  quotation: Object
}

const data = {
  oss: oss
}

const pageLifetimes = {}

const methods = {
  chooseQuotation() {
    let id = this.data.quotation.id
    this.triggerEvent('chooseQuotation', { id })
  }
}

Component({ properties, data, pageLifetimes, methods })