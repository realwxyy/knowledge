import React from "react";
import { Switch, Route, withRouter } from "react-router-dom";
import { getAllRoute } from "@routes/index";
import AllComponents from "@/views/index";

const ContentCustom = (props: any) => {
  const routers = getAllRoute();

  return (
    <div style={{ minHeight: 280 }}>
      <Switch>
        {routers.map((item: any) => {
          return item.accessFlag ? (
            <Route
              path={item.path}
              key={item.path}
              component={AllComponents[item.component]}
            />
          ) : null;
        })}
      </Switch>
    </div>
  );
};

export default withRouter(ContentCustom);
