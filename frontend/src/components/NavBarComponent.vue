<template>
  <nav class="navbar navbar-light bg-light">
    <div class="container">
      <form class="d-flex">
        <input class="form-control me-2" type="search"
               placeholder="Пошук" aria-label="Search"
               v-model="search_request">
        <button class="btn btn-outline-success" type="submit"
                @click="def_search_request(search_request)">Пошук</button>
      </form>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBarComponent",
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
nav {
  float: right;
  border-radius: 10px;
}
btn {
  border-color: red;
}
</style>