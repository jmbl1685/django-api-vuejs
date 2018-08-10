<template>
  <div id="app">
    <img src="./assets/logo.png" height="50">
    <Fruit/>
  </div>
</template>

<script>
import Fruit from './components/Fruit'

export default {
  name: 'App',
  components: {
    Fruit
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
