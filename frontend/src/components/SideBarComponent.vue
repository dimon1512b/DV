<template>
  <div>
    <aside>
      <img :src="require('../../build/static/vue/img/nissan_skyline.svg')" alt="nissan_skyline.svg">
      <div class="filter">
        <h3>Фільтрація</h3>
        <a class="home_button" href="#">
          <button @click="HomePage">Головна сторінка</button>
        </a>
        <form>
          <ul>
            <li>
              <select name="body_type" v-model="selectedBody">
                <option value="null"  disabled selected>Тип кузова</option>
                <option value="">Всі</option>
                <option v-for="body in all_data_types.body_type"
                        :key="body" :selected="body == selectedBody"
                        :value="body">{{body}}</option>
              </select>
            </li>
            <li>
              <select name="brand" v-model="selectedBrand">
                <option value="null" disabled selected>Марка</option>
                <option value="">Всі</option>
                <option v-for="brand in all_data_types.brand"
                        :key="brand"
                        :value="brand">{{brand}}</option>
              </select>
            </li>
            <li>
              <select name="model" v-model="selectedModel">
                <option value="null" disabled selected>Модель</option>
                <option value="">Всі</option>
                <option v-for="model in all_data_types.model"
                        :key="model" :selected="model == selectedModel"
                        :value="model">{{model}}</option>
              </select>
            </li>
            <input @click="getDataFilters()" type="button" value="Показати" class="show">
          </ul>
        </form>
      </div>

    </aside>
  </div>
</template>

<script>
export default {
  name: "SideBarComponent",
  data() {
    return {
      selectedBody: null,
      selectedBrand: null,
      selectedModel: null,
    }
  },
  props: {
    all_data_types: [],
    carData: {}
  },
  methods: {
    HomePage() { // good
      let filters = {}
      this.$emit('HomePage', filters)
    },
    getDataFilters() { // good
      let filters = {};
      if(this.selectedModel) {
        // console.log('select model');
        filters.model = this.selectedModel;
      }
      if(this.selectedBrand) {
        filters.brand = this.selectedBrand;
      }
      if(this.selectedBody) {
        filters.body_type = this.selectedBody;
      }
      console.log('filters before emit',filters);
      this.$emit('getDataFilters', filters);
      //   this.filters_from_side_bar.selectedModel}
      //   ${this.filters_from_side_bar.selectedBody}
      //   ${this.filters_from_side_bar.selectedBrand}
    },
    // pushDataToDetail() {
    //   console.log('data ===========sidebar==========', Object.entries(this.carData))
    //   console.log('data_types ===========sidebar==========', Object.entries(this.all_data_types))
    //   this.$emit('pushDataToDetail', this.carData)
    // }
  },
  // watch: {
  //   carData() {
  //     this.pushDataToDetail()
  //   }
}
</script>

<style scoped>
aside {
  background: #ffffff;
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 18%; /* Set the width of the sidebar */
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 20px;
  padding: 1%;
  color: #151515;
}

aside img {
  width: 205px;
  position: relative;
  top: -10px;
  left: 23px;
}

aside h3 {
  position: relative;
  top: -15px;
  left: 20px;
  font-size: 44px;
}

button {
  margin-left: 40px;
  background: red;
  color: #fff;
  width: 186px;
}

.show {
  position: relative;
  top: 15px;
  background: red;
  color: #fff;
  width: 186px;

  /*right: 25px;*/
}


select {
  width: 186px;
}


.filter li {
  list-style-type: none;
}

.filter {
  position: relative;
  right: 10px;
}
</style>