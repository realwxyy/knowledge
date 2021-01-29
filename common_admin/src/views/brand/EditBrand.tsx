import React, { FC, useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { Spin, Form, Input, Upload, Button, Affix, Tag, Modal, Table } from 'antd'
import { LoadingOutlined, PlusOutlined } from '@ant-design/icons'
import { BrandTagListColumns } from '@/constant/column'
import { oss, ossUrl } from '@config/path'
import '@less/EditBrand.less'
// import { DraggableArea } from 'react-draggable-tags'
const { DraggableArea } = require('react-draggable-tags')

const layout = {
  labelCol: { span: 8, xs: 5, sm: 5, md: 4, lg: 3, xl: 2, xxl: 2 },
  wrapperCol: { span: 16, xs: 6, sm: 18, md: 18, lg: 16, xl: 10, xxl: 8 },
}

const data = [
  { id: 1, content: '紧致轮廓', color: '#006699' },
  { id: 2, content: '淡化细纹', color: '#0099CC' },
  { id: 3, content: '敏感肌肤适用', color: '#00CCCC' },
  { id: 4, content: '减轻异味和瘙痒', color: '#339966' },
  { id: 5, content: '瑞士原装进口', color: '#33FFFF' },
  { id: 6, content: '德国专业抗衰', color: '#6633CC' },
  { id: 7, content: '欧洲植物精油领导品牌', color: '#6699FF' },
  { id: 8, content: '全球十大精油品牌', color: '#6699CC' },
  { id: 9, content: '德国殿堂级抗衰品牌', color: '#996699' },
]

const checkData = [
  { id: 10, content: '德国美容SPA集团排名前三klapp集团旗下', color: '#99CCCC' },
  { id: 11, content: '高端护肤', color: '#CC0066' },
  { id: 12, content: '关注热销品、喜欢有网红推荐的客户', color: '#CC66FF' },
  { id: 13, content: '性价比高', color: '#CC9999' },
  { id: 14, content: '毛利率高', color: '#CCFF33' },
  { id: 15, content: '瑞士小众高端香水', color: '#FF3366' },
  { id: 16, content: '香水与艺术的完美融合', color: '#990099' },
  { id: 17, content: '法国曼氏集团专业调香师调配', color: '#330000' },
  { id: 18, content: 'cherry', color: '#FF6600' },
  { id: 19, content: 'peach', color: '#FFCCCC' },
]

const validateMessages = {}

const EditBrand: FC = () => {
  const { id } = useParams() as any
  const [loading, setLoading] = useState<boolean>(true)
  const [logoList, setLogoList] = useState<any[]>([])
  const [logoLoading, setLogoLoading] = useState<boolean>(false)
  const [brandStoryList, setBrandStoryList] = useState<any[]>([])
  const [brandStoryLoading, setBrandStoryLoading] = useState<boolean>(false)
  const [promotionalImageList, setPromotionalImageList] = useState<any[]>([])
  const [promotionalImageLoading, setPromotionalImageLoading] = useState<boolean>(false)
  const [tagList, setTagList] = useState<any[]>(data)
  const [checkedTagList, setCheckedTagList] = useState<any[]>(checkData)
  const [tagListLoading, setTagListLoading] = useState<boolean>(false)
  // { uid: -1, url: ossUrl + 'brandLogo/fioSz0SX.jpeg', fileName: 'brandLogo/fioSz0SX.jpeg' }
  const logoUploadButton = (
    <div>
      {logoLoading ? <LoadingOutlined /> : <PlusOutlined />}
      <div style={{ marginTop: 8 }}>Logo</div>
    </div>
  )
  const brandStoryUploadButton = (
    <div>
      {brandStoryLoading ? <LoadingOutlined /> : <PlusOutlined />}
      <div style={{ marginTop: 8 }}>品牌故事</div>
    </div>
  )
  const promotionalImageUploadButton = (
    <div>
      {promotionalImageLoading ? <LoadingOutlined /> : <PlusOutlined />}
      <div style={{ marginTop: 8 }}>宣传图</div>
    </div>
  )

  const onFinish = (values: any) => {
    console.log(values)
  }

  const logoOnChange = (info: any) => {
    if (info.file.status === 'uploading') {
      setLogoLoading(true)
      return
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      setLogoList([{ uid: logoList.length + 1, url: ossUrl + info.file.response.data, fileName: info.file.response.data }])
    }
  }

  const brandStoryOnChage = (info: any) => {
    if (info.file.status === 'uploading') {
      setBrandStoryLoading(true)
      return
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      setBrandStoryList([{ uid: brandStoryList.length + 1, url: ossUrl + info.file.response.data, fileName: info.file.response.data }])
    }
  }

  const promotionImageOnChage = (info: any) => {
    if (info.file.status === 'uploading') {
      setPromotionalImageLoading(true)
      return
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      setPromotionalImageList([{ uid: promotionalImageList.length + 1, url: ossUrl + info.file.response.data, fileName: info.file.response.data }])
    }
  }

  //拖拽结束后触发的函数,返回已经改变的data
  const onChange = (tags: any) => {
    // console.log(tags)
    setTagList(tags)
  }

  const checkedOnChange = (tags: any) => {
    setCheckedTagList(tags)
  }
  //渲染每项
  const itemRender = ({ tag, index }: any) => {
    // return <div className="tag">{tag.content}</div>
    return (
      <Tag color={tag.color} closable onClose={(e) => tagOnClose(e, tag)}>
        {tag.content}
      </Tag>
    )
  }

  const tagOnClose = (e: any, tag: any) => {
    e.preventDefault()
    Modal.confirm({
      title: `删除确认`,
      content: `确认删除标签 [ ${tag.content} ] ?`,
      onOk: () => {
        setTagList(tagList.filter((o: any) => o.id !== tag.id))
      },
    })
  }

  useEffect(() => {
    if (id) {
    } else {
      setLoading(false)
    }
  }, [id])

  return (
    <>
      <div className="edit-brand-container">
        <Spin spinning={loading}>
          <Form {...layout} name="brandForm" onFinish={onFinish} validateMessages={validateMessages}>
            <div className="sperate-info">基础信息</div>
            <Form.Item name={['brandForm', 'zh_name']} label="中文名" rules={[{ required: true }]}>
              <Input allowClear />
            </Form.Item>
            <Form.Item name={['brandForm', 'en_name']} label="英文名" rules={[{ required: true }]}>
              <Input allowClear />
            </Form.Item>
            <Form.Item name={['brandForm', 'age']} label="编码" rules={[{ required: true }]}>
              <Input allowClear />
            </Form.Item>
            <Form.Item name={['brandForm', 'serial_number']} label="序号">
              <Input allowClear />
            </Form.Item>
            <Form.Item label="特色">
              {/* <Input allowClear /> */}
              <div className="tag-tip">（拖拽可排序）</div>
              <DraggableArea style={{ transition: '0.3s' }} tags={tagList} render={itemRender} onChange={onChange} />
              <Button>添加</Button>
            </Form.Item>
            <div className="sperate-info">图片信息</div>
            <Form.Item label="Logo">
              <Upload listType="picture-card" className="logo-uploader" action={oss} fileList={logoList} onChange={logoOnChange} maxCount={1}>
                {logoList.length >= 1 ? null : logoUploadButton}
              </Upload>
            </Form.Item>
            <Form.Item label="品牌故事">
              <Upload listType="picture-card" className="brand-story-uploader" action={oss} fileList={brandStoryList} onChange={brandStoryOnChage} maxCount={1}>
                {brandStoryList.length >= 1 ? null : brandStoryUploadButton}
              </Upload>
            </Form.Item>
            <Form.Item label="宣传图">
              <Upload listType="picture-card" className="promotional-img-uploader" action={oss} fileList={promotionalImageList} onChange={promotionImageOnChage} maxCount={1}>
                {promotionalImageList.length >= 1 ? null : promotionalImageUploadButton}
              </Upload>
            </Form.Item>
            <div className="sperate-info">补充信息</div>
            <Form.Item name={['brandForm', 'preferential_conditions']} label="优惠条件">
              <Input allowClear />
            </Form.Item>
            <Form.Item name={['brandForm', 'region']} label="国家地区">
              <Input allowClear />
            </Form.Item>
            <Form.Item name={['brandForm', 'cooperation_conditions']} label="合作规则">
              <Input.TextArea allowClear showCount maxLength={400} autoSize={{ minRows: 3, maxRows: 5 }} />
            </Form.Item>
            <Form.Item name={['brandForm', 'about_brand']} label="关于品牌">
              <Input.TextArea allowClear showCount maxLength={600} autoSize={{ minRows: 3, maxRows: 5 }} />
            </Form.Item>
            <Form.Item name={['brandForm', 'promotional_word']} label="宣传语">
              <Input.TextArea allowClear showCount maxLength={100} autoSize={{ minRows: 3, maxRows: 5 }} />
            </Form.Item>
            <Affix offsetBottom={1}>
              <div className="floating-bar">
                <Button type="primary" htmlType="submit">
                  提交
                </Button>
              </div>
            </Affix>
          </Form>
        </Spin>
      </div>
      <Modal title="编辑特色" width="900px" visible={true}>
        <div className="edit-tag-container">
          <div className="left-tag-container">
            <div className="top-tip">（拖拽可排序）</div>
            <div className="draggable-area">
              <DraggableArea isList tags={checkedTagList} render={itemRender} onChange={checkedOnChange} />
            </div>
          </div>
          <div className="middle-container"></div>
          <div className="right-tag-container">
            <div className="search-area">
              <Input className="default-input" placeholder="输入标签内容以搜索" />
              <Button type="primary" danger>
                搜索
              </Button>
            </div>
            <Table loading={tagListLoading} style={{ minHeight: 430, maxHeight: 430 }} scroll={{ y: 430 }} dataSource={tagList} columns={BrandTagListColumns} pagination={false} />
            {/* <DraggableArea tags={tagList} render={itemRender} onChange={onChange} /> */}
          </div>
        </div>
      </Modal>
    </>
  )
}

export default EditBrand
