import React, { FC, useState, useEffect, useCallback } from 'react'
import { Button, Row, Col, Input, Table, Pagination, Space, Popconfirm, message } from 'antd'
import { useHistory } from 'react-router-dom'
import { Brand as T_Brand } from '@/types'
import { queryBrandList, delBrand } from '@api/brand'
import { useWindowSize } from '@utils/utils'
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

  const BrandListColumns = [
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
    {
      title: '操作',
      key: 'operate',
      width: 100,
      align: 'center' as 'center',
      render: (item: any) => (
        <Space>
          <Button size="small" type="primary" onClick={() => editBrand(item)}>
            编辑
          </Button>
          <Popconfirm title="确认删除该品牌?" onConfirm={() => deleteBrand(item)} okText="是" cancelText="否">
            <Button size="small" type="primary" danger>
              删除
            </Button>
          </Popconfirm>
        </Space>
      ),
    },
  ]

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

  const addBrand = () => history.push('/admin/brand/editBrand')

  const editBrand = (item: any) => history.push(`/admin/brand/editBrand/${item.id}`)

  const deleteBrand = (item: any) => {
    const { id } = item
    delBrand({ id }).then((res: any) => {
      if (res.code === 0) {
        message.success('删除成功')
        getBrandList()
      }
    })
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
