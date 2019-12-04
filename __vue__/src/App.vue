<template>
  <div id="app">
    <DropDownMenu/>
  </div>
</template>

<script>
import DropDownMenu from './components/DropDownMenu.vue'


export default {
  name: 'app',
  components: {
    DropDownMenu
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
