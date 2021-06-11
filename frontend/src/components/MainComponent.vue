<template>
  <div class="base">
    <contents
        :filters="filters"
        @pushAllDataTypes = "pullAllDataTypes"
        @pushCarDataForMain="pullCarDataForMain"
    ></contents>
    <sidebar
        @getDataFilters="getDataFilters"
        @HomePage="getDataFilters"
        :all_data_types = "all_data_types"
        :carData="carData"
    ></sidebar>
  </div>
</template>

<script>

import sidebar from "./SideBarComponent";
import contents from "./ContentComponent"
export default {
  name: "MainComponent",
  components: {
    sidebar,
    contents
  },
  data() {
    return {
      filters: {},
      all_data_types: [],
      carData: {}
    }
  },
  methods: {
    pullAllDataTypes(data) {
      this.all_data_types = data
    },
    getDataFilters(data) {
      this.filters = data;
    },
    pullCarDataForMain(data) {
      console.log('data =========main=============', Object.entries(data))
      this.carData = data
    }
  }
}

</script>

<style>
body {
  background-color: #151515;
}
</style>
<style scoped>

</style>