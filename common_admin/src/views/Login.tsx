import React, { FC, ChangeEvent, useState } from 'react'
import { useDispatch } from 'react-redux'
import { Row, Col, Input, Button } from 'antd'
import { login } from '@api/login'
import { set_token } from '@redux/actions'
import '@less/Login.less'

const Login: FC = () => {
  const dispath = useDispatch()
  const [name, setName] = useState<string>('')
  const [password, setPassword] = useState<string>('')
  const [nameErr, setNameErr] = useState<boolean>(false)
  const [passwordErr, setPasswordErr] = useState<boolean>(false)
  const [nameErrWord, setNameErrWord] = useState<string>('')
  const [passwordErrWord, setPasswordErrWord] = useState<string>('')

  /**
   * validate name
   */
  const validateName = (e: ChangeEvent<HTMLInputElement>) => {
    let name = e.target.value
    if (name) {
      setNameErr(false)
      setNameErrWord('')
    } else {
      setNameErr(true)
      setNameErrWord('请输入用户名')
    }
    setName(name)
  }

  /**
   * validate password
   */
  const validatePassword = (e: ChangeEvent<HTMLInputElement>) => {
    let password = e.target.value
    if (password) {
      setPasswordErr(false)
      setPasswordErrWord('')
    } else {
      setPasswordErr(true)
      setPasswordErrWord('请输入密码')
    }
    setPassword(password)
  }

  /**
   * submit login info
   */
  const submitLogin = () => {
    let param = { name, password }
    login(param).then((res: any) => {
      console.log(res)
      if (res.code === 0) {
        dispath(set_token(res.data.id))
      }
    })
  }

  return (
    <>
      <Row>
        <Col span={8}></Col>
        <Col span={8} xs={24} md={24} xl={8} className="login-col">
          <div className="login-container">
            <div className="login-text-container">登录</div>
            <div className="login-input-container">
              <div
                className={
                  nameErr
                    ? 'login-name-container name-error'
                    : 'login-name-container'
                }
              >
                <Input
                  className="login-input name-error"
                  bordered={false}
                  placeholder={!nameErr ? '用户名' : nameErrWord}
                  onChange={validateName}
                />
              </div>
              <div
                className={
                  passwordErr
                    ? 'login-password-container name-error'
                    : 'login-password-container'
                }
              >
                <Input.Password
                  className="login-input"
                  bordered={false}
                  placeholder={!passwordErr ? '密码' : passwordErrWord}
                  onChange={validatePassword}
                />
              </div>
            </div>
            <div className="login-button-area">
              <Button
                className="login-button"
                type="primary"
                size="large"
                onClick={submitLogin}
              >
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
