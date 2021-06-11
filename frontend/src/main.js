import * as Vue from 'vue';
import * as VueRouter from 'vue-router';
import MainComponent from "./components/MainComponent";
import detailComponent from "./components/detailComponent";
import App from "./App";



const routes = [
        {
            path: '/static/vue/',
            name: 'main',
            component: MainComponent,
            props: true
        },
        {
            path: '/static/vue/car/:id',
            name: 'detail',
            component: detailComponent,
            props: true
        }
];

const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
});

Vue.createApp(App).use(router).mount('#app');
