import React from "react";
import { Layout } from "antd";
import { MenuUnfoldOutlined, MenuFoldOutlined } from "@ant-design/icons";

const { Header } = Layout;

const HeaderCustom = (props: any) => {
  const { collapsed, toggle } = props;

  return (
    <Header
      className="site-layout-background site-layout-header-customer"
      style={{ padding: 0 }}
    >
      <div className="site-left-layout-header">
        {React.createElement(
          collapsed ? MenuUnfoldOutlined : MenuFoldOutlined,
          {
            className: "trigger",
            onClick: toggle,
          }
        )}
        <div className="site-layout-header-customer-user">
          {/* <Dropdown overlay={menu}>
            <Button type="text" className="site-layout-header-customer-user-button">
              <span className="username">{localStorage.getItem('nickname')}</span><Avatar size={32} src={localStorage.getItem('icon')} />
            </Button>
          </Dropdown> */}
        </div>
      </div>
    </Header>
  );
};

export default HeaderCustom;
