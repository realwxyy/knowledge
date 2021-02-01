import React, { useEffect } from 'react'
import { Switch, Route, withRouter, useHistory } from 'react-router-dom'
import { getAllRoute } from '@routes/index'
import AllComponents from '@/views/index'

const ContentCustom = () => {
  const history = useHistory()
  let { pathname } = history.location
  const routers = getAllRoute()
  let routers_temp = JSON.parse(JSON.stringify(routers))
  routers_temp.forEach((o: any) => {
    let { path } = o
    let pathArr = path.split('/')
    if (pathArr[pathArr.length - 1].includes(':')) {
      pathArr.splice(-1)
    }
    o.path = pathArr.join('/')
  })
  let title = routers_temp.filter((o: any) => pathname.includes(o.path))[0].title || '未定义'
  useEffect(() => {
    document.title = title
  })

  return (
    <div style={{ minHeight: 280 }}>
      <Switch>{routers.map((item: any) => (item.accessFlag ? <Route path={item.path} key={item.path} component={AllComponents[item.component]} /> : null))}</Switch>
    </div>
  )
}

export default withRouter(ContentCustom)
