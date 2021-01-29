import { Tag, Button } from 'antd'

const BrandTagListColumns = [
  {
    title: '标签样式',
    key: 'name',
    width: 260,
    align: 'center' as 'center',
    render: (t: any) => <Tag color={t.color}>{t.content}</Tag>,
  },
  {
    title: '操作',
    dataIndex: 'serial_number',
    key: 'serial_number',
    width: 100,
    align: 'center' as 'center',
    className: 'column_serial_number',
    render: () => (
      <Button size="small" type="primary" danger>
        添加
      </Button>
    ),
  },
]

export default BrandTagListColumns
