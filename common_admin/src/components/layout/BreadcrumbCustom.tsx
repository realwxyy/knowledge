import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import { Breadcrumb } from 'antd'
import { exceptRouter, exceptHomeRouter, AdminHome } from '@/constant/exceptRouter'

const breadcrumbNameMap: any = {
  //跟路由路径保持一致
  '/': '首页',
  '/403': '403',
  '/404': '404',
  '/admin/brand/brand': '品牌列表',
  '/admin/brand/editBrand': '编辑品牌',
}

const BreadcrumbCustom = (props: any) => {
  const { location } = props
  let pathSnippets = location.pathname.split('/').filter((i: any) => i)
  const extraBreadcrumbItems = pathSnippets.map((_: any, index: number) => {
    const url = `/${pathSnippets.slice(0, index + 1).join('/')}`
    return (
      <Breadcrumb.Item key={url}>
        <Link to={url}>{breadcrumbNameMap[url]}</Link>
      </Breadcrumb.Item>
    )
  })
  let breadcrumbItems = [
    <Breadcrumb.Item key="/home">
      <Link to="/">首页</Link>
    </Breadcrumb.Item>,
  ].concat(extraBreadcrumbItems)
  if (location.pathname === AdminHome) {
    breadcrumbItems = breadcrumbItems.filter((o: any) => !exceptRouter.includes(o.key))
  } else {
    breadcrumbItems = breadcrumbItems.filter((o: any) => !exceptHomeRouter.includes(o.key))
  }
  console.log(extraBreadcrumbItems)
  return (
    <div className="demo">
      <Breadcrumb style={{ margin: '16px 0 0' }}>{breadcrumbItems}</Breadcrumb>
    </div>
  )
}
export default withRouter(BreadcrumbCustom)
