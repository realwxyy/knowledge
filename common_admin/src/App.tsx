import React from "react";
import { Switch, Route, Redirect } from "react-router-dom";
// import { AdminLayout } from "@component/index";

const App = () => (
  <Switch>
    <Route exact path="/" render={() => <Redirect to="/admin/home" push />} />
    <Route path="/login" />
    <Route path="/" />
  </Switch>
);

export default App;
