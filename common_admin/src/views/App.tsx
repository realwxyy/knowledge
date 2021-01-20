import React from 'react'
import { Switch, Route, Redirect } from 'react-router-dom'
import { AdminLayout } from '@components/index'
import Login from './Login'

const App = () => (
  <Switch>
    <Route exact path="/" render={() => <Redirect to="/admin/home" push />} />
    <Route path="/admin" component={AdminLayout} />
    <Route path="/login" component={Login} exact />
  </Switch>
)

export default App
