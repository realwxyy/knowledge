import React, { useEffect } from 'react'
import { Switch, Route, withRouter, useHistory } from 'react-router-dom'
import { getAllRoute } from '@routes/index'
import AllComponents from '@/views/index'

const ContentCustom = (props: any) => {
  const history = useHistory()
  let { pathname } = history.location
  const routers = getAllRoute()
  let title = routers.filter((o: any) => pathname.includes(o.path))[0].title || '未定义'

  useEffect(() => {
    document.title = title
  }, [title])

  return (
    <div style={{ minHeight: 280 }}>
      <Switch>
        {routers.map((item: any) => {
          return item.accessFlag ? <Route path={item.path} key={item.path} component={AllComponents[item.component]} /> : null
        })}
      </Switch>
    </div>
  )
}

export default withRouter(ContentCustom)
