import React, { FC } from 'react'
import { withRouter } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { Layout } from 'antd'
import SiderCustom from './SiderCustom'
import ContentCustom from './ContentCustom'
import HeaderCustom from './HeaderCustom'
import BreadcrumbCustom from './BreadcrumbCustom'
import { collapsed as collapsed_param } from '@redux/actions'
import '@less/AdminLayout.less'

const { Content } = Layout

const AdminLayout: FC = () => {
  const dispatch = useDispatch()
  const collapsed = useSelector((state: any) => state.collapsed)
  const toggle = () => dispatch(collapsed_param(!collapsed))

  return (
    <Layout
      className="site-layout"
      style={{
        overflow: 'auto',
        height: '100vh',
      }}
    >
      <SiderCustom collapsed={collapsed} />
      <Layout>
        <HeaderCustom
          collapsed={collapsed}
          toggle={toggle}
          // history={history}
        />
        <div style={{ marginLeft: '16px' }}>
          <BreadcrumbCustom />
        </div>
        <Content style={{ margin: '16px 16px 0', overflow: 'initial' }}>
          <ContentCustom />
        </Content>
      </Layout>
    </Layout>
  )
}

export default withRouter(AdminLayout)
