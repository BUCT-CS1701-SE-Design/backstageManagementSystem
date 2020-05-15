<template>
  <div>
   <el-menu default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-submenu index="1">
        <el-menu-item index="1-1">ddd</el-menu-item>
      </el-submenu>
      <el-menu-item index="2">fff</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'Home',
  components: {
  }
}
</script>
