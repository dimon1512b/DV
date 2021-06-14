<template class="container">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <NavBarComponent
            @def_search_request='pull_def_search_request'>
        </NavBarComponent>
      </div>
      <div class="col-3 position-fixed">
        <sidebar
            @getDataFilters="getDataFilters"
            @HomePage="getDataFilters"
            :all_data_types="all_data_types"
            :carData="carData"
        ></sidebar>
      </div>
      <div class="col">
        <card
            v-for="car in cars"
            :key="car.id"
            :car="car"
            @pushId="pullId"
        ></card>
      </div>

    </div>
    <div class="row">
      <div class="col">
        <pagination
            :count_pages="count_pages"
            :current_page="current_page"
            @change_page="change_page"
        ></pagination>
      </div>
    </div>
  </div>
</template>

<script>

import sidebar from "./SideBarComponent";
import card from './CardComponent'
import pagination from './PaginationComponent'
import NavBarComponent from "./NavBarComponent";
import axios from "axios";

export default {
  name: "MainComponent",
  components: {
    sidebar,
    card,
    pagination,
    NavBarComponent
  },
  data() {
    return {
      cars: {}, // good
      filters: {}, // good
      all_data_types: [], // good
      carData: {},
      count_pages: {}, // good
      current_page: {} // good
    }
  },
  methods: {
    // pullAllDataTypes(data) {
    //   this.all_data_types = data
    // },
    pullId(data) { // good
      alert(`ID = ${data}`)
    },
    pull_def_search_request(data) { // good
      this.filters = data
    },
    getDataFilters(data) { // good
      this.filters = data;
    },
    change_page(page) { // good
      console.log('change_page in MAIN called')
      this.filters.page = page
      console.log('Filter was changed', this.filters)
      this.getCardsData(this.filters)
    },
    getCardsData(params) { // good
      axios.get("http://127.0.0.1:8000/api/ajax_get_cars/", {params: params})
          //console.log(`filters = ${Object.entries(this.filters)}`)
          .then((response) => { // good
            this.cars = response.data.auto // good
            this.all_data_types = response.data.all_data_types // good
            this.count_pages = response.data.pages // good
            this.current_page = response.data.current_page // good
            console.log('!!!!!!count_pages ПОЛУЧЕН!!!!!!!!!', this.count_pages) // good
            console.log('!!!!!!current_page ПОЛУЧЕН!!!!!!!!!', this.current_page) // good
            // this.pushAllDataTypes()

          })
          .catch((error) => { // good
            console.log(error)

          })
    }
  },
  mounted() { // good
    this.getCardsData(this.filters)
  },
  watch: {
    filters() { // good
      console.log('WATCH IN MAIN WAS CALLED')
      this.getCardsData(this.filters)
    }
  }
}

</script>

<style>

</style>
