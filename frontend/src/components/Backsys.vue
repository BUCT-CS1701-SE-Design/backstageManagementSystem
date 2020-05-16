<template>
    <div>
    <Signin/>
    <Nav/>
  </div>
</template>

<script>
import Nav from './Nav.vue'
import Signin from './Signin.vue'
// @ is an alias to /src
export default {
  name: 'Backsys',
  components: {
    Nav,
    Signin
  }
}
</script>
