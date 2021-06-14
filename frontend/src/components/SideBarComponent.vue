<template>
  <div class="col">
    <aside>
      <img :src="require('../../build/static/vue/img/nissan_skyline.svg')" alt="nissan_skyline.svg">
      <div class="filter">
        <h3>Фільтрація</h3>
        <button class="btn" @click="HomePage">Головна сторінка</button>
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
          </ul>
        </form>
        <button @click="getDataFilters()" type="button" class="btn">Показати</button>
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
  background: rgba(200,200,224,0.2);
  border-radius: 10px;
  height: 100vh; /* Full-height: remove this if you want "auto" height */
  display: block;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding: 1%;
  color: white;
  border-right: #0B0B0B solid;
}

aside img {
  width: 75%;
  position: relative;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.filter {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.btn, option {
  margin-right: 10px;
  margin-left: 10px;
  width: 100%;
}
h3 {
  margin-left: auto;
  margin-right: auto;
}
.btn {
  color: white;
}

ul li {
  list-style-type: none;
}

</style>