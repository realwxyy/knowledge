import { Brand } from './Brand'

// UserInfo
interface userInfo {
  id: number
  name: string
  nickname?: string
  phone?: string
  role_id: number
}
export type StoreState = number
export type UserInfo = userInfo

interface tableHeight {
  height?: number
  minHeight?: number
}
export type TableHeight = tableHeight
export type { Brand }
