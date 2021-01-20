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
      // {
      //   key: '/materialLibrary',
      //   icon: PieChartOutlined,
      //   title: '主页',
      //   component: 'MaterialLibrary',
      // },
      {
        key: '/article',
        icon: BarChartOutlined,
        title: '文章',
        children: [
          { key: '/index', title: '文章管理', component: 'Article' },
          {
            key: '/editArticle/:id?',
            title: '编辑文章',
            component: 'EditArticle',
            hideInMenu: true,
          },
        ],
      },
      {
        key: '/component',
        icon: BarChartOutlined,
        title: '组件',
        children: [
          { key: '/index', title: '组件管理', component: 'Component' },
        ],
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
