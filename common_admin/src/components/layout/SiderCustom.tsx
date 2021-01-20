import React, { useState, useEffect } from 'react'
import { Link, withRouter } from 'react-router-dom'
import { Layout, Menu } from 'antd'
import Icon from '@ant-design/icons'
import { handleJoinPath, filterLayout } from '@routes/index'

const { SubMenu } = Menu
const { Sider } = Layout

const SiderCustome = (props: any) => {
  const [openKey, setOpenyKey] = useState<any>()
  const [selectKey, setSelectKey] = useState<any>()
  const [routers, setRouters] = useState<any>()

  const { collapsed } = props

  const handleClick = (e: any) => {
    let key = e.key
    let openKey = [key.substring(0, key.lastIndexOf('/'))]
    setOpenyKey(openKey)
    setSelectKey(e.keyPath)
  }

  const renderSubMenu = (item: any) => {
    // console.log(item);
    return (
      <SubMenu
        key={item.path}
        data-test={item.path}
        title={
          <span>
            <Icon component={item.icon} className="sider-menu-icon" />
            <span className="nav-text">{item.title}</span>
          </span>
        }
      >
        {item.children &&
          item.children.map((sub: any) =>
            sub.children
              ? renderSubMenu(sub)
              : sub.hideInMenu || !sub.accessFlag
              ? null
              : renderMenuItem(sub)
          )}
      </SubMenu>
    )
  }

  const renderMenuItem = (item: any) => {
    return (
      <Menu.Item data-tset1={item.path} key={item.path}>
        <Link to={item.path}>
          {item.icon ? (
            <Icon component={item.icon} className="sider-menu-icon" />
          ) : null}
          <span>{item.title}</span>
        </Link>
      </Menu.Item>
    )
  }

  useEffect(() => {
    let routers = filterLayout('AdminLayout')
    setRouters(routers)
    handleJoinPath(routers, routers.key, '')
    let pathname = props.location.pathname
    let openKey = [pathname.substring(0, pathname.lastIndexOf('/'))]
    setOpenyKey(openKey)
    setSelectKey([pathname])
  }, [props.location.pathname])

  return (
    <Sider
      // width={150}
      trigger={null}
      collapsible
      collapsed={collapsed}
      className="site-layout-background"
      style={{
        overflow: 'auto',
        height: '100vh',
      }}
      theme="light"
    >
      <div className="sider-menu-item-logo">admin</div>
      <Menu
        mode="inline"
        theme="light"
        defaultOpenKeys={openKey}
        selectedKeys={selectKey}
        onClick={(e) => handleClick(e)}
      >
        {routers &&
          routers.key &&
          routers.children.map((item: any) => {
            return item.children
              ? renderSubMenu(item)
              : item.accessFlag && !item.hideInMenu
              ? renderMenuItem(item)
              : null
          })}
      </Menu>
    </Sider>
  )
}

export default withRouter(SiderCustome)
