import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { HashRouter } from 'react-router-dom'
import { PersistGate } from 'redux-persist/es/integration/react'
import { ConfigProvider } from 'antd'
import App from './views/App'
import store, { persistor } from './redux/store'
import zhCN from 'antd/es/locale/zh_CN'
import 'antd/dist/antd.css'
import '@css/index.css'

ReactDOM.render(
  <Provider store={store}>
    <PersistGate persistor={persistor}>
      <HashRouter>
        <ConfigProvider locale={zhCN}>
          <App />
        </ConfigProvider>
      </HashRouter>
    </PersistGate>
  </Provider>,
  document.getElementById('root')
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
