import React from 'react'
import { Button, Row, Col, Input, Table, Pagination } from 'antd'
import '@less/Brand.less'

const Brand = () => {
  const dataSource = [
    {
      key: '1',
      name: '胡彦斌',
      age: 32,
      address: '西湖区湖底公园1号',
    },
    {
      key: '2',
      name: '胡彦祖',
      age: 42,
      address: '西湖区湖底公园1号',
    },
  ]

  const columns = [
    {
      title: '姓名',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: '年龄',
      dataIndex: 'age',
      key: 'age',
    },
    {
      title: '住址',
      dataIndex: 'address',
      key: 'address',
    },
  ]

  const tableStyle = { minHeight: '400px' }
  return (
    <>
      <Row gutter={[0, 16]}>
        <Col span={12}>
          <Button type="primary">新增品牌</Button>
        </Col>
        <Col className="right-item" span={12}>
          <Input className="brand-input default-input" placeholder="请输入品牌名称" />
          <Button type="primary">搜索</Button>
        </Col>
      </Row>
      <Row gutter={[0, 8]}>
        <Col span={24}>
          <Table bordered style={tableStyle} dataSource={dataSource} columns={columns} pagination={false} />
        </Col>
      </Row>
      <Row>
        <Col span={12} className="pagination">
          <Pagination defaultCurrent={1} total={50} />
        </Col>
      </Row>
    </>
  )
}

export default Brand
