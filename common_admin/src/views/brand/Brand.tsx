import React, { FC, useState, useEffect, useCallback } from 'react'
import { Button, Row, Col, Input, Table, Pagination } from 'antd'
import { useHistory } from 'react-router-dom'
import { Brand as T_Brand } from '@/types'
import { queryBrandList } from '@api/brand'
import { useWindowSize } from '@utils/utils'
import { BrandListColumns } from '@/constant/column'
import '@less/Brand.less'

const Brand: FC = () => {
  const history = useHistory()
  const windowSize = useWindowSize()
  const [tableHeight, setTableHeight] = useState<number>(windowSize.innerHeight - 176 - 38)
  const tableStyle = { minHeight: tableHeight, maxHeight: tableHeight }
  const [page] = useState<number>(1)
  const [size] = useState<number>(50)
  const [brandListTotal, setBrandListTotal] = useState<number>(0)
  const [brandName, setBrandName] = useState<string>()
  const [brandList, setBrandList] = useState<T_Brand[]>([])
  const [brandListLoading, setBrandListLoading] = useState<boolean>(false)

  const getBrandList = useCallback(() => {
    setBrandListLoading(true)
    queryBrandList({ page, size, brandName }).then((res: any) => {
      console.log(res)
      if (res.code === 0) {
        let list = res.data.list
        list.forEach((o: T_Brand) => (o.key = o.id))
        setBrandList(list)
        setBrandListTotal(res.data.total)
        setBrandListLoading(false)
      }
    })
  }, [page, size, brandName])

  const addBrand = () => {
    history.push('/admin/brand/editBrand')
  }

  useEffect(() => {
    setTableHeight(windowSize.innerHeight - 176 - 38)
  }, [windowSize.innerHeight])

  useEffect(() => {
    getBrandList()
  }, [getBrandList])
  return (
    <>
      <Row gutter={[0, 16]} className="operate-row">
        <Col span={12}>
          <Button type="primary" onClick={addBrand}>
            新增品牌
          </Button>
        </Col>
        <Col className="right-item" span={12}>
          <Input className="brand-input default-input" onBlur={(e: any) => setBrandName(e.target.value)} placeholder="请输入品牌名称" />
          <Button type="primary">搜索</Button>
        </Col>
      </Row>
      <Row gutter={[0, 8]} className="table-row">
        <Col span={24}>
          <Table bordered loading={brandListLoading} style={tableStyle} scroll={{ y: tableHeight - 70 }} dataSource={brandList} columns={BrandListColumns} pagination={false} />
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
