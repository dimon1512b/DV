<template>
		<nav class="list-pages" >
			<ul v-if="count_pages > 1">
        <li v-for="p in shownPage"
            @click="change_page(p)"
            :key="p"
            class="page-num"
            :class="{ 'page-num-selected' : (p === current_page) }">
          <a>{{p}}</a>
        </li>
			</ul>
		</nav>
</template>

<script>
export default {
  name: "pagination",
  props: {
    count_pages: Number,
    current_page: Number
  },
  data() {
    return {
      // count_pages_from_content: this.count_pages,
      // current_page_from_content: this.current_page
    }
  },
  methods: {
    change_page(p) {
      console.log('change_page PAGINATOR was called. Данные переданы: page=', p)
      this.$emit('change_page', p)
    }
  },
  computed: {
    shownPage() {
      console.log('count_pages and current_page ПОЛУЧЕНЫ и составляют:', this.count_pages,
          this.current_page)
      let array_pages = [];
        for(let i = 1; i <= this.count_pages; i++) {
          console.log('i =', i)
          if ((i >= this.current_page - 2) && (i <= this.current_page + 2)) {
            console.log('TRUE', i,
                `Это значит что:${this.current_page -2}<=${i}<=${this.current_page + 2}`)
            array_pages.push(i);
          }
          else {
            console.log('FALSE', i,
                `Это значит что:${this.current_page -2}!<=${i}!<=${this.current_page + 2}`)
          }
        }
      console.log('array_pages На основе данных сформирован!!!========', array_pages)
      return array_pages;
    }
  },
  watch() {

  }


  // computed: {
  //   castom_range: function () {
  //     let arr = []
  //     arr.apply(1, {length: this.count_pages_from_content+1}).map(Number.call, Number)
  //     console.log('arr======', arr)
  //     return arr
  //   }
  // }
}
</script>

<style scoped>
.list-pages {
    position: relative;
    margin-left: 460px;
    height: 45%;
    width: 50%;
    text-align: center;
}

.list-pages a {
	color: #fff;
	font-size: 24px;
	text-decoration: none;
}
.list-pages .page-num, .page-num-selected {
	display: inline-block;
	width: 60px;
	height: 30px;
	padding: 0 0 0 0;
	border: 1px solid #d0d0d0;
	border-radius: 14px;
}
.list-pages .page-num:hover {
	box-shadow:0px 0px 3px 3px red;
}
.list-pages .page-num-selected {
	border: none;
	color: #fff;
	font-size: 20px;
}
.list-pages .page-num-selected:hover {
	box-shadow: none;
}

select {
    width: 186px;
}
</style>