import React, { useState, useEffect, useCallback } from 'react'
import { Button, Row, Col, Input, Table, Pagination } from 'antd'
import { Brand as T_Brand } from '@/types'
import { queryBrandList } from '@api/brand'
import { useWindowSize } from '@utils/utils'
import '@less/Brand.less'

const Brand = () => {
  const columns = [
    {
      title: 'ID',
      dataIndex: 'id',
      key: 'id',
      width: 80,
      align: 'center' as 'center',
      className: 'column_ID',
    },
    {
      title: '名称',
      key: 'name',
      width: 200,
      align: 'center' as 'center',
      className: 'column_name',
      render: (t: any, r: any, i: number) => <div>{r.en_name + '/' + r.zh_name}</div>,
    },
    {
      title: 'code',
      dataIndex: 'code',
      key: 'code',
      width: 140,
      align: 'center' as 'center',
      className: 'column_code',
    },
    {
      title: '地区',
      dataIndex: 'region',
      key: 'region',
      width: 100,
      align: 'center' as 'center',
      className: 'column_region',
    },
    {
      title: '关于品牌',
      dataIndex: 'about_brand',
      key: 'about_brand',
      width: 240,
      align: 'center' as 'center',
      className: 'column_about_brand',
      render: (t: any) => <div className="about_brand">{t}</div>,
    },
    {
      title: '序号',
      dataIndex: 'serial_number',
      key: 'serial_number',
      width: 80,
      align: 'center' as 'center',
      className: 'column_serial_number',
    },
  ]
  const windowSize = useWindowSize()
  const [tableHeight, setTableHeight] = useState<number>(windowSize.innerHeight - 176)
  const tableStyle = { minHeight: tableHeight }
  const [page] = useState<number>(1)
  const [size] = useState<number>(50)
  const [brandListTotal, setBrandListTotal] = useState<number>(0)
  const [brandName, setBrandName] = useState<string>()
  const [brandList, setBrandList] = useState<T_Brand[]>([])

  const getBrandList = useCallback(() => {
    queryBrandList({ page, size, brandName }).then((res: any) => {
      console.log(res)
      let list = res.data.list
      list.forEach((o: T_Brand) => (o.key = o.id))
      setBrandList(list)
      setBrandListTotal(res.data.total)
    })
  }, [page, size, brandName])

  useEffect(() => {
    setTableHeight(windowSize.innerHeight - 176)
  }, [windowSize.innerHeight])

  useEffect(() => {
    getBrandList()
  }, [getBrandList])
  return (
    <>
      <Row gutter={[0, 16]} className="operate-row">
        <Col span={12}>
          <Button type="primary">新增品牌</Button>
        </Col>
        <Col className="right-item" span={12}>
          <Input className="brand-input default-input" onChange={(e: any) => setBrandName(e.target.value)} placeholder="请输入品牌名称" />
          <Button type="primary">搜索</Button>
        </Col>
      </Row>
      <Row gutter={[0, 8]} className="table-row">
        <Col span={24}>
          <Table bordered style={tableStyle} scroll={{ y: tableHeight - 64 }} dataSource={brandList} columns={columns} pagination={false} />
        </Col>
      </Row>
      <Row className="pagination-row">
        <Col span={12} className="pagination">
          <Pagination pageSize={size} defaultPageSize={size} total={brandListTotal} />
        </Col>
      </Row>
    </>
  )
}

export default Brand
