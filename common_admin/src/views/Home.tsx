import React, { FC } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { increment } from '@/redux/store/actions'

const Home: FC = () => {
  const dispatch = useDispatch()
  const test = useSelector((state) => state)
  console.log(test)
  const f: any = () => {
    dispatch({ type: 'INCREMENT' })
    console.log(test)
  }
  console.log(test)
  // dispatch(increment())
  return (
    <div>
      <button onClick={f}></button>
    </div>
  )
}

export default Home
