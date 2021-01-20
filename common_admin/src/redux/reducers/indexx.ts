import { combineReducers } from 'redux'
import { ModifyAction } from '../store/actions'
import { DECREMENT, INCREMENT } from '../const/const'

// 处理并返回 state
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

const rootReducer: any = combineReducers({
  Test,
  Test2,
})

export default rootReducer
