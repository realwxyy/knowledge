import React, { FC } from 'react'
import { Row, Col, Input, Button } from 'antd'
import '@less/Login.less'

const Login: FC = () => {
  return (
    <>
      <Row>
        <Col span={8}></Col>
        <Col span={8} xs={24} md={24} xl={8} className="login-col">
          <div className="login-container">
            <div className="login-text-container">登录</div>
            <div className="login-input-container">
              <Input
                className="login-input"
                bordered={false}
                placeholder="用户名"
              />
              <Input
                className="login-input"
                bordered={false}
                placeholder="密码"
              />
            </div>
            <div className="login-button-area">
              <Button className="login-button" type="primary" size="large">
                登录
              </Button>
            </div>
          </div>
        </Col>
        <Col span={8}></Col>
      </Row>
    </>
  )
}

export default Login
