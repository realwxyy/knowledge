import React, { FC, useState, useEffect, useRef, useCallback } from 'react'
import { useParams, useHistory } from 'react-router-dom'
import { Spin, Form, Input, Upload, Button, Affix, Tag, Modal, Table, Tooltip } from 'antd'
import { LoadingOutlined, CameraFilled, QuestionCircleOutlined } from '@ant-design/icons'
import { uploadUrl, staticUrl } from '@config/path'
import { addBrand, saveBrand, queryBrandDetail } from '@api/brand'
import { queryAllTags } from '@api/tag'
import '@less/EditBrand.less'
// import { DraggableArea } from 'react-draggable-tags'
const { DraggableArea } = require('react-draggable-tags')

const layout = {
  labelCol: { span: 8, xs: 5, sm: 5, md: 4, lg: 3, xl: 2, xxl: 2 },
  wrapperCol: { span: 16, xs: 6, sm: 18, md: 18, lg: 16, xl: 10, xxl: 8 },
}

const validateMessages = {}

const EditBrand: FC = () => {
  const { id } = useParams() as any
  const history = useHistory()
  const [form] = Form.useForm()
  const formRef: any = useRef()
  const [loading, setLoading] = useState<boolean>(true)
  const [logoList, setLogoList] = useState<any[]>([])
  const [logoLoading, setLogoLoading] = useState<boolean>(false)
  const [brandStoryList, setBrandStoryList] = useState<any[]>([])
  const [brandStoryLoading, setBrandStoryLoading] = useState<boolean>(false)
  const [promotionalImageList, setPromotionalImageList] = useState<any[]>([])
  const [promotionalImageLoading, setPromotionalImageLoading] = useState<boolean>(false)
  const [tagList, setTagList] = useState<any>([])
  const [checkedTagList, setCheckedTagList] = useState<any>([])
  const [tagListLoading, setTagListLoading] = useState<boolean>(false)
  const [editTagDialog, setEditTagDialog] = useState<boolean>(false)
  const [previewVisible, setPreviewVisible] = useState<boolean>(false)
  const [previewTitle, setPreviewTitle] = useState<string>('')
  const [previewImage, setPreviewImage] = useState<string>('')
  // { uid: -1, url: ossUrl + 'brandLogo/fioSz0SX.jpeg', fileName: 'brandLogo/fioSz0SX.jpeg' }
  const BrandTagListColumns = [
    {
      title: '标签样式',
      key: 'name',
      width: 260,
      align: 'center' as 'center',
      render: (t: any) => <Tag color={t.color}>{t.name}</Tag>,
    },
    {
      title: '操作',
      key: 'serial_number',
      width: 100,
      align: 'center' as 'center',
      render: (item: any) => (
        <Button size="small" type="primary" danger onClick={() => addTag(item)}>
          添加
        </Button>
      ),
    },
  ]
  const logoUploadButton = (
    <div>
      {logoLoading ? <LoadingOutlined /> : <CameraFilled />}
      <div style={{ marginTop: 8 }}>Logo</div>
    </div>
  )
  const brandStoryUploadButton = (
    <div>
      {brandStoryLoading ? <LoadingOutlined /> : <CameraFilled />}
      <div style={{ marginTop: 8 }}>品牌故事</div>
    </div>
  )
  const promotionalImageUploadButton = (
    <div>
      {promotionalImageLoading ? <LoadingOutlined /> : <CameraFilled />}
      <div style={{ marginTop: 8 }}>宣传图</div>
    </div>
  )

  const onFinish = (values: any) => {
    let tags = checkedTagList.map((o: any) => o.id)
    let logo = logoList[0].fileName
    let story = brandStoryList[0].fileName
    let promotional_img = promotionalImageList[0].fileName
    let param = Object.assign({}, values, { tags, logo, story, promotional_img })
    if (id) {
      param = Object.assign({}, param, { id })
      saveBrand(param).then((res: any) => {
        console.log(res)
      })
    } else {
      addBrand(param).then((res: any) => {
        console.log(res)
      })
    }
    history.goBack()
  }

  const logoOnChange = (info: any) => {
    if (info.file.status === 'uploading') {
      setLogoLoading(true)
      return
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      setLogoList([{ uid: logoList.length + 1, url: staticUrl + info.file.response.data, fileName: info.file.response.data }])
    }
  }

  const brandStoryOnChage = (info: any) => {
    if (info.file.status === 'uploading') {
      setBrandStoryLoading(true)
      return
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      setBrandStoryList([{ uid: brandStoryList.length + 1, url: staticUrl + info.file.response.data, fileName: info.file.response.data }])
    }
  }

  const promotionImageOnChage = (info: any) => {
    if (info.file.status === 'uploading') {
      setPromotionalImageLoading(true)
      return
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      setPromotionalImageList([{ uid: promotionalImageList.length + 1, url: staticUrl + info.file.response.data, fileName: info.file.response.data }])
    }
  }

  const checkedOnChange = (tags: any) => {
    setCheckedTagList(tags)
  }
  //渲染每项
  const itemRender = ({ tag }: any) => {
    // return <div className="tag">{tag.content}</div>
    return <Tag color={tag.color}>{tag.name}</Tag>
  }

  // 渲染每项
  const itemListRender = ({ tag }: any) => (
    <div className="checked-tag-list">
      <Tag color={tag.color} closable onClose={(e) => tagOnClose(e, tag)}>
        {tag.name}
      </Tag>
    </div>
  )

  const tagOnClose = (e: any, tag: any) => {
    e.preventDefault()
    Modal.confirm({
      title: `删除确认`,
      content: `确认删除标签 [ ${tag.name} ] ?`,
      onOk: () => {
        let ctl = checkedTagList.filter((o: any) => o.id !== tag.id)
        setCheckedTagList(ctl)
      },
    })
  }

  const openEditTagDialog = () => {
    setEditTagDialog(true)
  }

  const addTag = (item: any) => {
    let ctl: any = checkedTagList
    let tl: any = tagList
    ctl.push(item)
    setCheckedTagList(ctl)
    setTagList(tl.filter((o: any) => !ctl.map((p: any) => p.id).includes(o.id)))
  }

  const getBrandDetail = useCallback(
    (id: number) => {
      queryBrandDetail({ id }).then((res: any) => {
        if (res.code === 0) {
          let data = res.data
          form.setFieldsValue(data)
          setCheckedTagList(data.tags)
          setLogoList([{ uid: 0, url: staticUrl + data.logo, fileName: data.logo }])
          setBrandStoryList([{ uid: 0, url: staticUrl + data.story, fileName: data.story }])
          setPromotionalImageList([{ uid: 0, url: staticUrl + data.promotional_img, fileName: data.promotional_img }])
        }
        setLoading(false)
      })
    },
    [form]
  )

  const getAllTags = () => {
    setTagListLoading(true)
    queryAllTags().then((res: any) => {
      if (res.code === 0) {
        let { data } = res
        data.forEach((o: any) => (o.key = o.id))
        setTagList(res.data)
      }
      setTagListLoading(false)
    })
  }

  const handleCancel = () => setPreviewVisible(false)

  const imagePreview = (file: any) => {
    console.log(file)
    let nameArr = file.fileName.split('/')
    setPreviewTitle(nameArr[nameArr.length - 1])
    setPreviewImage(file.url)
    setPreviewVisible(true)
  }

  useEffect(() => {
    if (id) {
      getBrandDetail(id)
    } else {
      setLoading(false)
    }
    getAllTags()
  }, [id, getBrandDetail])

  return (
    <>
      <div className="edit-brand-container">
        <Spin spinning={loading}>
          <Form {...layout} form={form} ref={formRef} name="brandForm" onFinish={onFinish} validateMessages={validateMessages}>
            <div className="sperate-info">基础信息</div>
            <Form.Item name="zh_name" label="中文名" rules={[{ required: true }]}>
              <Input allowClear />
            </Form.Item>
            <Form.Item name="en_name" label="英文名" rules={[{ required: true }]}>
              <Input allowClear />
            </Form.Item>
            <Form.Item name="code" label="编码" rules={[{ required: true }]}>
              <Input allowClear />
            </Form.Item>
            <Form.Item name="serial_number" label="序号">
              <Input allowClear />
            </Form.Item>
            <Form.Item label="特色">
              {/* <Input allowClear /> */}
              <div className="tag-tip">{checkedTagList.length > 1 ? '（拖拽可排序）' : ''}</div>
              <DraggableArea tags={checkedTagList} render={itemRender} onChange={checkedOnChange} />
              <Button onClick={openEditTagDialog}>{checkedTagList.length > 0 ? '编辑' : '添加'}</Button>
            </Form.Item>
            <div className="sperate-info">图片信息</div>
            <Form.Item
              label={
                <span>
                  Logo&nbsp;
                  <Tooltip title="上传大小不超过3M，支持jpg、jpeg、png格式，建议尺寸： 640*640 像素，1:1 亦可。">
                    <QuestionCircleOutlined />
                  </Tooltip>
                </span>
              }
            >
              <Upload listType="picture-card" className="logo-uploader" action={uploadUrl + 'brandLogo'} fileList={logoList} onChange={logoOnChange} maxCount={1} onPreview={imagePreview} onRemove={() => setLogoList([])}>
                {logoList.length >= 1 ? null : logoUploadButton}
              </Upload>
            </Form.Item>
            <Form.Item
              label={
                <span>
                  品牌故事&nbsp;
                  <Tooltip title="上传大小不超过3M，支持jpg、jpeg、png格式，建议尺寸： 750*180 像素，4:1 亦可。">
                    <QuestionCircleOutlined />
                  </Tooltip>
                </span>
              }
            >
              <Upload listType="picture-card" className="brand-story-uploader" action={uploadUrl + 'brandStory'} fileList={brandStoryList} onChange={brandStoryOnChage} maxCount={1} onPreview={imagePreview} onRemove={() => setBrandStoryList([])}>
                {brandStoryList.length >= 1 ? null : brandStoryUploadButton}
              </Upload>
            </Form.Item>
            <Form.Item
              label={
                <span>
                  宣传图&nbsp;
                  <Tooltip title="上传大小不超过3M，支持jpg、jpeg、png格式，建议尺寸： 750*180 像素，4:1 亦可。">
                    <QuestionCircleOutlined />
                  </Tooltip>
                </span>
              }
            >
              <Upload listType="picture-card" className="promotional-img-uploader" action={uploadUrl + 'brandPromotional'} fileList={promotionalImageList} onChange={promotionImageOnChage} maxCount={1} onPreview={imagePreview} onRemove={() => setPromotionalImageList([])}>
                {promotionalImageList.length >= 1 ? null : promotionalImageUploadButton}
              </Upload>
            </Form.Item>
            <div className="sperate-info">补充信息</div>
            <Form.Item name="preferential_conditions" label="优惠条件">
              <Input allowClear />
            </Form.Item>
            <Form.Item name="region" label="国家地区">
              <Input allowClear />
            </Form.Item>
            <Form.Item name="cooperation_conditions" label="合作规则">
              <Input.TextArea allowClear showCount maxLength={400} autoSize={{ minRows: 3, maxRows: 5 }} />
            </Form.Item>
            <Form.Item name="about_brand" label="关于品牌">
              <Input.TextArea allowClear showCount maxLength={600} autoSize={{ minRows: 3, maxRows: 5 }} />
            </Form.Item>
            <Form.Item name="promotional_word" label="宣传语">
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
      <Modal
        title="编辑特色"
        width="900px"
        maskClosable={false}
        visible={editTagDialog}
        onCancel={() => setEditTagDialog(false)}
        footer={
          <Button type="primary" onClick={() => setEditTagDialog(false)}>
            关闭
          </Button>
        }
      >
        <div className="edit-tag-container">
          <div className="left-tag-container">
            <div className="top-tip">{checkedTagList.length > 1 ? '（拖拽可排序）' : ''}</div>
            <div className="draggable-area">
              <DraggableArea isList tags={checkedTagList} render={itemListRender} onChange={checkedOnChange} />
            </div>
          </div>
          <div className="middle-container"></div>
          <div className="right-tag-container">
            <div className="search-area">
              <Input className="default-input" placeholder="输入标签内容以搜索" />
              <Button type="primary">搜索</Button>
            </div>
            <Table loading={tagListLoading} style={{ minHeight: 430, maxHeight: 430 }} scroll={{ y: 430 }} dataSource={tagList.filter((o: any) => !checkedTagList.map((p: any) => p.id).includes(o.id))} columns={BrandTagListColumns} pagination={false} />
            {/* <DraggableArea tags={tagList} render={itemRender} onChange={onChange} /> */}
          </div>
        </div>
      </Modal>
      <Modal visible={previewVisible} title={previewTitle} footer={null} onCancel={handleCancel} width="1100px">
        <img alt="example" style={{ width: '100%' }} src={previewImage} />
      </Modal>
    </>
  )
}

export default EditBrand
