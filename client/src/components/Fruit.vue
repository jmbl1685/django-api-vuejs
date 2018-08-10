<template>
  <div class="hello"><br>
    <div v-for="fruit in fruits" :key="fruit._id">
      <img :src="fruit.img" class="fruit-img">
      <h5>{{fruit.name}}</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "Fruit",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      fruits: []
    };
  },
  created() {
    const url = "http://localhost:8000/fruit/?format=json";

    fetch(url)
      .then(res => res.json())
      .then(data => {
        this.fruits = data;
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.fruit-img{
  height: 200px;
  width: 200px;
}
</style>
