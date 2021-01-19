import React, { FC, useState } from "react";
import { withRouter } from "react-router-dom";
import { Layout } from "antd";
import "@less/AdminLayout.less";

const AdminLayout: FC = () => {
  const [collapsed, setCollapsed] = useState(false);
  return <Layout></Layout>;
};

export default withRouter(AdminLayout);
