import React, { FC } from 'react'
import { useDispatch } from 'react-redux'
import { Button } from 'antd'
import { increment } from '@/redux/actions'

const Home: FC = () => {
  console.log(window)
  console.log(window.innerHeight)
  console.log(window.innerWidth)
  let style = { width: window.innerWidth, height: window.innerHeight, border: '1px solid' }
  return <div style={style}>Home</div>
}

export default Home
