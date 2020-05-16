<template>
  <div>
     <router-link to="Signin">Home</router-link>
    <router-view></router-view>
    <Backsys/>
  </div>
</template>

<script>
import Backsys from './components/Backsys.vue'
export default {
  name: 'app',
  components: {
    Backsys
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
