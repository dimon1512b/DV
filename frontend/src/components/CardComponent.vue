<template>
  <div class="card">
    <div class="photo_card">
      <img :src="car.photo_card">
    </div>
    <div class="description_card">
      <div class="full_name_car">
        <a @click="goToDetail(car)" target="_blank">
          <ul class="name_car">
            <li class="brand">-{{car.brand}}-</li>
            <li class="model">-{{car.model}}-</li>
            <li class="version">-{{car.version}}-</li>
            <li class="year">-{{car.year}}-</li>
          </ul>
        </a>
      </div>

      <div class="price_usd_uah">
        <ul>
          <li class="price_usd">-----{{car.price_usd}}#USD-----</li>
          <li class="price_uah">-----{{car.price_uah}}#UAH-----</li>
        </ul>
      </div>
      <div class="race_city">
        <ul>
          <li class="race">{{ car.race }}/</li>
          <li class="city">Знаходиться в {{ car.city }}</li>
        </ul>
      </div>

      <div class="engine_trans">
        <ul>
          <li class="engine_type">{{ car.engine_type }}/</li>
          <li class="engine_capacity">{{ car.engine_capacity }}/</li>
          <li class="transmission">{{ car.transmission }}</li>
        </ul>
      </div>

      <div class="pl_num_vin">
        <ul>
          <li class="pl_num">Номерний знак{{ car.plate_number }}/</li>
          <li class="vin">VIN{{ car.vin_code }}/</li>
        </ul>
      </div>

      <div class="date_created">
        <ul>
          <li>{{ car.date_created }}</li>
        </ul>
      </div>
      <li class="send_id">
        <button @click="pushId(car.id)">Отправить id!!!
        </button>
      </li>
    </div>
  </div>
</template>

<script>

export default {
  name: "CardComponent",
  props: {
    car: Object,
    all_data_types: {}
  },
  methods: {
    pushId(data) {
      this.$emit('pushId', data)
    },
    goToDetail(data) {
      // let car = this.car
      console.log('data =========card==========', data)
      this.$emit('pushCarData', data)
      // window.currentCarData = data
      this.$router.push({name: 'detail', params: {id: data.id, car: JSON.stringify(data)}})
    }
  },
  data() {
    return {

    }
  }
}
// {path: `/static/vue/car/${this.car.id}`,
</script>

<style scoped>
  .card {
      background: #0B0B0B;
      float: right;
      margin-top: 50px;
      margin-right: 235px;
      margin-bottom: 50px;
      width: 44%;
      padding: 1%;
      color: #ffffff;
  }


  .photo_card img {
    position: relative;
  }
  .full_name_car li, .race_city li, .price_usd_uah li, .engine_trans li, .pl_num_vin li, .date_created li, .send_id {
      display: inline-block;
      font-size: 15px;
  }

  .send_id button {
    margin-left: 40px;
  }

  .price_usd_uah {
    width: 200px;
  }

  .photo_card img { float: right; }
  .brand { color: red; }
  .full_name_car a { text-decoration: none; color: white; }
  .full_name_car a:visited { color: #6C8CD5; }
  .full_name_car a:hover { color: red; }
  .full_name_car a:hover, .model:hover {
    color: red;
    transform: scale(1.10);
  }
  .send_id {
  }
</style>