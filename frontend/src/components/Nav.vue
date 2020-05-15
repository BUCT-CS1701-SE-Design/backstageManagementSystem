<template>
    <div>
        <el-menu default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">博物馆应用平台-后台管理系统</el-menu-item>
      <el-submenu index="2">
        <template slot="title">用户管理</template>
        <el-menu-item index="2-1">用户管理</el-menu-item>
      </el-submenu>
       <el-submenu index="3">
        <template slot="title">讲解审核</template>
        <el-menu-item index="3-1">未审核</el-menu-item>
        <el-menu-item index="3-2">已审核</el-menu-item>
      </el-submenu>
       <el-submenu index="4">
        <template slot="title">数据管理</template>
        <el-menu-item index="4-1">博物馆</el-menu-item>
        <el-menu-item index="4-2">展览</el-menu-item>
        <el-menu-item index="4-3">藏品</el-menu-item>
        <el-menu-item index="4-4">新闻</el-menu-item>
        <el-menu-item index="4-5">讲解</el-menu-item>
        <el-menu-item index="4-6">操作日志</el-menu-item>
      </el-submenu>
       <el-submenu index="5">
        <template slot="title">系统管理</template>
        <el-menu-item index="5-2">文件备份与恢复</el-menu-item>
        <el-menu-item index="5-3">数据库备份与恢复</el-menu-item>
      </el-submenu>
      <el-menu-item index="3"></el-menu-item>
      <el-menu-item index="4"></el-menu-item>
      <el-menu-item index="5"></el-menu-item>
    </el-menu>
    </div>
</template>
<script>
// @ is an alias to /src
export default {
  name: 'Nav',
  components: {
  }
}
</script>
