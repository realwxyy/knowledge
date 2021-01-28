import { combineReducers } from 'redux'
import { ModifyAction } from '../actions'
import { DECREMENT, INCREMENT, SET_TOKEN, CLEAR_TOKEN, TOGGLE_OPEN, TOGGLE_CLOSE, TOGGLE } from '../const/const'

// 处理并返回 state 测试
const Test = (state = 0, action: ModifyAction): number => {
  switch (action.type) {
    case INCREMENT:
      return state + 1
    case DECREMENT:
      return state - 1
    default:
      return state
  }
}

// 测试
const Test2 = (state = 0, action: ModifyAction): number => {
  return state
}

// common-token
const token = (state = '', action: any) => {
  switch (action.type) {
    case SET_TOKEN:
      return action.token
    case CLEAR_TOKEN:
      return ''
    default:
      return state
  }
}

// admin-user
// const userInfo = (state = {}, action: any) => {}

// collapse
const collapsed = (state = false, action: any) => {
  switch (action.type) {
    case TOGGLE_OPEN:
      return !state
    case TOGGLE_CLOSE:
      return state
    case TOGGLE:
      return action.collapsed
    default:
      return state
  }
}

const rootReducer: any = combineReducers({
  Test,
  Test2,
  token,
  collapsed,
})

export default rootReducer
