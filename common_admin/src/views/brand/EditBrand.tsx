import React, { FC, useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { Spin, Form, Input, Upload, Button } from 'antd'
import { LoadingOutlined, PlusOutlined } from '@ant-design/icons'
import { oss, ossUrl } from '@config/path'
import '@less/EditBrand.less'

const layout = {
  labelCol: { span: 8, xs: 5, sm: 5, md: 4, lg: 3, xl: 2, xxl: 2 },
  wrapperCol: { span: 16, xs: 6, sm: 18, md: 18, lg: 16, xl: 10, xxl: 8 },
}

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
              <Input />
            </Form.Item>
            <Form.Item name={['brandForm', 'age']} label="编码" rules={[{ required: true }]}>
              <Input />
            </Form.Item>
            <Form.Item name={['brandForm', 'en_name']} label="英文名" rules={[{ required: true }]}>
              <Input />
            </Form.Item>
            <Form.Item name={['brandForm', 'tags']} label="特色">
              <Input />
            </Form.Item>
            <Form.Item name={['brandForm', 'serial_number']} label="序号">
              <Input />
            </Form.Item>
            <div className="sperate-info">图片信息</div>
            <Form.Item name={['brandForm', 'logo']} label="logo">
              <Upload listType="picture-card" className="logo-uploader" action={oss} fileList={logoList} onChange={logoOnChange} maxCount={1}>
                {logoList.length >= 1 ? null : logoUploadButton}
              </Upload>
            </Form.Item>
            <Form.Item name={['brandForm', 'brand_story']} label="品牌故事">
              <Upload listType="picture-card" className="brand-story-uploader" action={oss} fileList={brandStoryList} onChange={brandStoryOnChage} maxCount={1}>
                {brandStoryList.length >= 1 ? null : brandStoryUploadButton}
              </Upload>
            </Form.Item>
            <Form.Item name={['brandForm', 'promotional_img']} label="宣传图">
              <Upload listType="picture-card" className="promotional-img-uploader" action={oss} fileList={promotionalImageList} onChange={promotionImageOnChage} maxCount={1}>
                {promotionalImageList.length >= 1 ? null : promotionalImageUploadButton}
              </Upload>
            </Form.Item>
            <div className="sperate-info">补充信息</div>
            <Form.Item name={['brandForm', 'preferential_conditions']} label="优惠条件">
              <Input />
            </Form.Item>
            <Form.Item name={['brandForm', 'region']} label="国家地区">
              <Input />
            </Form.Item>
            <Form.Item name={['brandForm', 'promotional_word']} label="宣传语">
              <Input.TextArea maxLength={100} />
            </Form.Item>
            <Form.Item name={['brandForm', 'cooperation_conditions']} label="合作规则">
              <Input.TextArea maxLength={400} />
            </Form.Item>
            <Form.Item name={['brandForm', 'about_brand']} label="关于品牌">
              <Input.TextArea maxLength={600} />
            </Form.Item>
            <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
          </Form>
        </Spin>
      </div>
    </>
  )
}

export default EditBrand
