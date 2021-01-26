import React, { FC, useState } from 'react'
import { withRouter } from 'react-router-dom'
import { Layout } from 'antd'
import SiderCustom from './SiderCustom'
import ContentCustom from './ContentCustom'
import HeaderCustom from './HeaderCustom'
import '@less/AdminLayout.less'

const { Content } = Layout

const AdminLayout: FC = () => {
  const [collapsed, setCollapsed] = useState<boolean>(false)
  const toggle = () => setCollapsed(!collapsed)
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
        {/* <BreadcrumbCustom /> */}
        <Content style={{ margin: '16px', overflow: 'initial' }}>
          <ContentCustom />
        </Content>
      </Layout>
    </Layout>
  )
}

export default withRouter(AdminLayout)
