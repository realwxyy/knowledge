/**
 * 处理路由数据
 */

import routers from './router'
import {
  PieChartOutlined,
  BarChartOutlined,
  AppstoreOutlined,
  OrderedListOutlined,
  UserOutlined,
  MoneyCollectOutlined,
  CarOutlined,
  MenuOutlined,
  TrademarkOutlined,
} from '@ant-design/icons'

export const routerConfig = () => {
  return routers
}

export const handleJoinPath = (router: any, path: any, role: any) => {
  router.children &&
    router.children.forEach((item: any) => {
      handleJoinPath(item, path + item.key, role)
    })
  router.accessFlag = true
  if (router.access) {
    if (router.access.indexOf(role) === -1) {
      // 有权限
      router.accessFlag = false
    }
  }
  router.path = path
}

export const filterLayout = (type: any) => {
  let router
  for (let i = 0; i < routerConfig().length; i++) {
    const item: any = routerConfig()[i]
    if (item.layout === type) {
      router = item
      break
    }
  }
  return router
}

export const getAllRoute = (role: any = '') => {
  let layout_list: any = [] // 所有 layout 的集合
  let route_list: any = [] // 所有 route 的集合
  routerConfig().forEach((item: any) => {
    if (item.layout) {
      handleJoinPath(item, item.key, role)
      layout_list.push(item)
    }
  })

  getRoute(layout_list, route_list)

  routerConfig().forEach((item: any) => {
    if (!item.layout) {
      item.path = item.key
      route_list.push(item)
    }
  })
  return route_list
}

export const getRoute = (routes: any, list: any) => {
  for (const k in routes) {
    const item = routes[k]
    if (item.children) {
      getRoute(item.children, list)
    } else {
      document.title = item.title
      list.push(item)
    }
  }
}

export const getIcon = (icon: any) => {
  if (icon === 'PieChartOutlined') {
    return PieChartOutlined
  } else if (icon === 'BarChartOutlined') {
    return BarChartOutlined
  } else if (icon === 'AppstoreOutlined') {
    return AppstoreOutlined
  } else if (icon === 'OrderedListOutlined') {
    return OrderedListOutlined
  } else if (icon === 'UserOutlined') {
    return UserOutlined
  } else if (icon === 'MoneyCollectOutlined') {
    return MoneyCollectOutlined
  } else if (icon === 'CarOutlined') {
    return CarOutlined
  } else if (icon === 'MenuOutlined') {
    return MenuOutlined
  } else if (icon === 'TrademarkOutlined') {
    return TrademarkOutlined
  }
}
