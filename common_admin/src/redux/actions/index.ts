import { DECREMENT, DECREMENT_TYPE, INCREMENT, INCREMENT_TYPE, SET_TOKEN, SET_TOKEN_TYPE, SET_USER_INFO, SET_USER_INFO_TYPE, CLEAR_USER_INFO, CLEAR_USER_INFO_TYPE, CLEAR_TOKEN, CLEAR_TOKEN_TYPE, TOGGLE_OPEN, TOGGLE_CLOSE, TOGGLE } from '../const/const'
import { UserInfo } from '@/types'

export interface IINCREMENTAction {
  type: INCREMENT_TYPE
}

export interface IDECREMENTAction {
  type: DECREMENT_TYPE
}

export interface SET_TOKENAction {
  type: SET_TOKEN_TYPE
  token: string
}

export interface CLEAR_TOKENAction {
  type: CLEAR_TOKEN_TYPE
  token?: string
}

export interface SET_USER_INFOAction {
  type: SET_USER_INFO_TYPE
  userInfo: UserInfo
}

export interface CLEAR_USER_INFOAction {
  type: CLEAR_USER_INFO_TYPE
  userInfo?: UserInfo
}

// 定义 modifyAction 类型，包含 IINCREMENTAction 和 IDECREMENTAction 接口类型
export type ModifyAction = IINCREMENTAction | IDECREMENTAction
// 定义 tokenAction 类型
export type TokenAction = SET_TOKENAction | CLEAR_TOKENAction
// 定义 userInfoAction 类型
export type UserInfoAction = SET_USER_INFOAction | CLEAR_USER_INFOAction

// 增加 state 次数的方法
export const increment = (): IINCREMENTAction => ({ type: INCREMENT })

// 减少 state 次数的方法
export const decrement = (): IDECREMENTAction => ({ type: DECREMENT })

// 设置token的方法
export const set_token = (token: string): SET_TOKENAction => ({
  type: SET_TOKEN,
  token: token,
})

// token 置空的方法
export const clear_token = (): CLEAR_TOKENAction => ({ type: CLEAR_TOKEN })

export const set_user_info = (userInfo: UserInfo): UserInfoAction => ({
  type: SET_USER_INFO,
  userInfo: userInfo,
})

export const clear_user_info = (): UserInfoAction => ({
  type: CLEAR_USER_INFO,
})

export const collapsed_open = () => ({ type: TOGGLE_OPEN })

export const collapsed_close = () => ({ type: TOGGLE_CLOSE })

export const collapsed = (collapsed: boolean) => ({ type: TOGGLE, collapsed })
