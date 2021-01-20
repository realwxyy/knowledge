import React, { FC } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { Button } from 'antd'
import { increment } from '@/redux/store/actions'

const Home: FC = () => {
  const dispatch = useDispatch()
  const test = useSelector((state) => state)
  console.log(test)
  const f: any = () => {
    dispatch(increment())
    console.log(test)
  }
  console.log(test)
  // dispatch(increment())
  return (
    <div>
      <Button type="primary" onClick={f}>
        按钮
      </Button>
    </div>
  )
}

export default Home
