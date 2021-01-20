import React from 'react'
import { Switch, Route, Redirect } from 'react-router-dom'
import { Button } from 'antd'
import { AdminLayout } from '@components/index'

const App = () => (
  <Switch>
    <Route exact path="/" render={() => <Redirect to="/admin/home" push />} />
    <Route path="/admin" component={AdminLayout} />
  </Switch>
)

export default App
