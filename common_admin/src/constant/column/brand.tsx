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
]

export default BrandListColumns
