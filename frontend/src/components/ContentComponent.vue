<template>
  <div class="content">
    <div class="search">
      <SearchComponent
        @def_search_request='pull_def_search_request'>
      </SearchComponent>
    </div>
    <div>
      <card
        v-for="car in cars"
        :key="car.id"
        :car="car"
        :all_data_types="all_data_types"
        @pushId="pullId"
        @pushCarData="pullCarData"
      ></card>
    </div>
    <div>
      <pagination
          :count_pages="count_pages"
          :current_page="current_page"
          @change_page="change_page"
      ></pagination>
    </div>
  </div>
</template>

<script>
import card from './CardComponent'
import pagination from './PaginationComponent'
import SearchComponent from "./SearchComponent";
// import {mapActions, mapGetters} from "index"
import axios from "axios";
export default {
  name: "ContentComponent",
  components: {
    card,
    pagination,
    SearchComponent
  },
  data() {
    return {
      cars: [], // full
      all_data_types: [], // full
      count_pages: 0,
      current_page: 0,
      changed_page: 1,
      content_filter: {}
    }
  },
  watch: {
    filters() {
      this.content_filter = this.filters
      console.log('this.content_filter from sideBar====', this.content_filter)
      this.getCardsData(this.content_filter);
    }
  },
  props: {
    filters: Object
  },
  methods: {
    pushAllDataTypes() {
      this.$emit('pushAllDataTypes', this.all_data_types)
    },
    change_page(page) {
      console.log('change_page in Content called')
      this.content_filter.page = page
      this.getCardsData(this.content_filter);
    },

    pullId(data) {
      alert(`id = ${data}`)
    },
    pullCarData(data) {
      console.log('data =========content==========', Object.entries(data))
      this.$emit('pushCarDataForMain', data)
    },
    pull_def_search_request(data) {
      this.content_filter = data
      this.getCardsData(this.content_filter)
    },
    getCardsData(params) {
      axios.get("http://127.0.0.1:8000/api/ajax_get_cars/", {params: params})
        //console.log(`filters = ${Object.entries(this.filters)}`)
        .then((response) => {
          this.cars = response.data.auto
          this.all_data_types = response.data.all_data_types
          this.count_pages = response.data.pages
          this.current_page = response.data.current_page
          console.log('!!!!!!count_pages ПОЛУЧЕН!!!!!!!!!', this.count_pages)
          console.log('!!!!!!current_page ПОЛУЧЕН!!!!!!!!!', this.current_page)
          // window.all_data_types_ = response.data.all_data_types
          this.pushAllDataTypes()

        })
        .catch((error) => {
          console.log(error)

      })
    }
  },
  mounted() {
    this.getCardsData();
  },

}
</script>

<style scoped>
body {
  background: #151515;
  color: white;
}
</style>