/**
 *  hideInMenu: true 在侧边栏中不显示
 *  access: [] 权限
 *  name: AdminLayout 后台管理工作台
 */

/*********************** 后台页面 ************************ */
import { PieChartOutlined, BarChartOutlined } from '@ant-design/icons'
const router: Array<object> = [
  {
    key: '/admin',
    layout: 'AdminLayout',
    children: [
      {
        key: '/home',
        icon: PieChartOutlined,
        title: '主页',
        component: 'Home',
      },
      {
        key: '/brand',
        icon: PieChartOutlined,
        title: '品牌',
        children: [
          {
            key: '/brand',
            title: '品牌列表',
            component: 'Brand',
          },
          {
            key: '/editBrand/:id?',
            title: '编辑品牌',
            component: 'EditBrand',
            hideInMenu: true,
          },
        ],
      },
      {
        key: '/product',
        icon: BarChartOutlined,
        title: '商品',
        component: 'ProductList',
      },
      {
        key: '/500',
        title: 'error_500',
        hideInMenu: true,
        component: 'Exception500',
      },
      {
        key: '/404',
        title: 'error_404',
        hideInMenu: true,
        component: 'Exception404',
      },
    ],
  },
]
export default router
