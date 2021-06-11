<template>
  <div class="search">
    <input v-model="search_request" type="text">
    <button @click="def_search_request(search_request)">Пошук</button>
  </div>
</template>

<script>

export default { // good
  name: "SearchComponent",
  data() { // good
    return {
      search_request: null
    }
  },
  methods: { // good
    def_search_request(data) { // good
      this.search_request = data
      this.$emit('def_search_request', {'search_request': this.search_request})
    }
  }
}
</script>

<style scoped>
.search {
  position: absolute;
  right: 20px;
}
.search input {
    width: 22vh;
}
</style>