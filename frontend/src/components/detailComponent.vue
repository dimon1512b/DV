<template>
  <div class="detail">
    <aside>
<!--      <img :src="require('../../build/static/vue/img/nissan_skyline.svg')" alt="nissan_skyline.svg">-->
      <div class="filter">
        <h3>Фільтрація</h3>
        <a class="home_button" href="/static/vue/">
          <button>Головна сторінка</button>
        </a>
      </div>
    </aside>
    <div class="base_block">
      <div class="img_block">
        <img class="base_photo" :src="data_.photo_view" alt="">
      </div>
      <div class="data_block">
        <div class="full_name_block">
          <ul>
            <li>| {{ data_.brand }} |</li>
            <li>| {{ data_.model }} |</li>
            <li>| {{ data_.version }} |</li>
            <li>| {{ data_.year }} рік |</li>
          </ul>
        </div>
        <div class="price">
          <ul>
            <li>-----{{ data_.price_usd }}USD-----</li>
            <li>-----{{ data_.price_uah }}UAH-----</li>
          </ul>
        </div>
        <div class="another_data">
          <ul>
            <li>{{ data_.race }}</li>
            <li>Трансмісія - {{ data_.transmission }}</li>
            <li>Регіон - {{ data_.region }}</li>
            <li>Знаходиться у {{ data_.city }}</li>
            <li>Тип двигуна - {{ data_.engine_type }}</li>
            <li>Літраж - {{ data_.engine_capacity }}</li>
            <li>Номерний знак - {{ data_.plate_number }}</li>
            <li>VIN - {{ data_.vin_code }}</li>
            <li>Тип транспорта - {{ data_.type_of_transport }}</li>
            <li>Тип кузова - {{ data_.body_type }}</li>
            <li>Привід - {{ data_.drive_type }}</li>
            <li>Дата створення оголошення - {{ data_.date_created }}</li>
            <li>Дата створення в нашій базі - {{ data_.date_added_to_DB }}</li>
          </ul>
        </div>
      </div>
      <div class="description_block">
        <p>{{ data_.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "detailComponent",
  props: {},
  components: {
  },
  data() {
    return {
      data_: {},//window.currentCarData,
    }
  },
  methods: {
  },
  mounted() {
    this.data_ = JSON.parse(this.$route.params.car);
  }
}
console.log()
</script>

<style scoped>
.base_block {
  color: white;
}

.img_block {
   position: absolute;
   display: block;
   margin-left: 305px;
   margin-right: auto;
   background: #0B0B0B;
   width:400px;
   height:400px;
}

.img_block img {
   position: relative;
   top:50%;
   left:50%;
   transform:translate(-50%,-50%);
   width:360px;
   height:360px;
   object-fit:cover;
}
.full_name_block li {
    position: relative;
    display: inline-block;
}
.price li {
    position: relative;
    display: inline-block;
}
.another_data li {
    position: relative;
    list-style: none;
}


.data_block {
    display: block;
    margin-left: 750px;
    margin-right: auto;
    margin-top: 0px;
    background: #0B0B0B;
    width:493px;
    height:400px;
    padding: 0.1px;
}

.description_block {
    display: block;
    margin-left: 305px;
    margin-right: auto;
    margin-top: 0px;
    background: #0B0B0B;
    width:900px;
    height:180px;
    padding: 1.4%;
}

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
  left: 23px;
  font-size: 44px;
}

button {
  margin-left: 40px;
  background: red;
  color: #fff;
  width: 186px;
}
</style>