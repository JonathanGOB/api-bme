<template>
  <div id="app">
    <DropDownMenu @selected="SendToMenu"/>
    <GraphMenu ref="Graphman"/>
  </div>
</template>

<script>
import DropDownMenu from './components/DropDownMenu.vue'
import GraphMenu from "./components/GraphMenu";

export default {
  name: 'app',
  components: {
    GraphMenu,
    DropDownMenu
  },
  methods:{
    SendToMenu:function (value) {
        this.$refs.Graphman.getData(value);
    }
  }
}
</script>

<style>

</style>
