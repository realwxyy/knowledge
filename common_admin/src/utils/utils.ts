import { useState, useEffect } from 'react'

export const getTableHeight = (otherHeight: number) => {
  let innerHeight = window.innerHeight
  let tableHeight = innerHeight - otherHeight
  return tableHeight
}

export const useWindowSize = () => {
  const getWindowSize = () => ({
    innerHeight: window.innerHeight,
    innerWidth: window.innerWidth,
  })

  const [windowSize, setWindowSize] = useState(getWindowSize())

  const handleResize = () => {
    setWindowSize(getWindowSize())
  }

  useEffect(() => {
    // 监听
    window.addEventListener('resize', handleResize)

    // 销毁
    return () => window.removeEventListener('resize', handleResize)
  })

  return windowSize
}
