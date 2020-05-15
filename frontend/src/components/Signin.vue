<template>
  <div>
      <el-form :rules="rules" :model="loginForm" class="loginRoot">
      <h3 class="loginTitle">系统博物馆导览系统登陆</h3>
      <el-form-item prop="username">
        <el-input type="text" v-model="loginForm.username" auto-complete="off" placeholder="请输入用户名"/>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="text" v-model="loginForm.password" auto-complete="off" placeholder="请输入密码"/>
      </el-form-item>
      <el-button type="primary" style="width: 100%">登陆</el-button>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Signin',
  components: {
  }
}
</script>

<style>

</style>
