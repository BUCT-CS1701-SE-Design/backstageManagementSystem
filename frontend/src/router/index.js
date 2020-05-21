import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: '博物馆后台管理系统',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '博物馆后台管理系统', icon: 'dashboard' }
    }]
  },
  {
    path: '/users',
    component: Layout,
    children: [
      {
        path: 'users',
        name: 'users',
        component: () => import('@/views/users/index'),
        meta: { title: '用户管理', icon: 'form' }
      }
    ]
  },
  {
    path: '/datas',
    component: Layout,
    redirect: '/datas/museums',
    name: 'datas',
    meta: { title: '数据管理', icon: 'form' },
    children: [
      {
        path: 'museums',
        name: 'museums',
        component: () => import('@/views/museums/index'),
        meta: { title: '博物馆信息' }
      },
      {
        path: 'exhibitions',
        name: 'exhibitions',
        component: () => import('@/views/exhibitions/index'),
        meta: { title: '展览信息' }
      },
      {
        path: 'collections',
        name: 'collections',
        component: () => import('@/views/collections/index'),
        meta: { title: '藏品信息' }
      },
      {
        path: 'news',
        name: 'news',
        component: () => import('@/views/news/index'),
        meta: { title: '新闻信息' }
      },
      {
        path: 'explainations',
        name: 'explainations',
        component: () => import('@/views/explainations/index'),
        meta: { title: '讲解信息' }
      },
      {
        path: 'comments',
        name: 'comments',
        component: () => import('@/views/comments/index'),
        meta: { title: '评论信息' }
      },
      {
        path: 'sql_log',
        name: 'sql_log',
        component: () => import('@/views/sql_log/index'),
        meta: { title: '数据库操作日志' }
      }

    ]
  },
  {
    path: '/reviewexplain',
    component: Layout,
    redirect: '/reviewexplain/reviewing',
    name: 'checkexp',
    meta: { title: '讲解审核', icon: 'example' },
    children: [
      {
        path: 'reviewing',
        name: 'reviewing',
        component: () => import('@/views/reviewexplain/reviewing'),
        meta: { title: '未审核', icon: 'form' }
      },
      {
        path: 'reviewed',
        name: 'reviewed',
        component: () => import('@/views/reviewexplain/reviewed'),
        meta: { title: '已审核', icon: 'form' }
      }
    ]
  },
  {
    path: '/database',
    component: Layout,
    redirect: '/database/files',
    name: 'database',
    meta: { title: '数据库管理', icon: 'example' },
    children: [
      {
        path: 'files',
        name: 'files',
        component: () => import('@/views/database/files'),
        meta: { title: '文件备份与恢复', icon: 'table' }
      },
      {
        path: 'workbench',
        name: 'workbench',
        component: () => import('@/views/database/workbench'),
        meta: { title: '数据库备份与恢复', icon: 'tree' }
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
