import {createStore} from 'vuex'

const store = createStore({
    state: {
        detailData: '1234567890'
    },
    getters: {

    },
    mutations: {

    },
    actions: {

    }
})

export default store



// let index = new Vuex.Store({ // хранилище
//     state: {
//         cars: []
//     }, // состояние
//     mutations: {
//         SET_CARS_TO_STATE: (state, cars) => {
//             state.cars = cars;
//         }
//     }, // меняют состояние
//     actions: {
//         GET_CARS_FROM_API({commit}) {
//             return axios("http://127.0.0.1:8000/api/ajax_get_cars/", {
//                 method: "GET"
//             })
//                 .then((cars) => {
//                     commit('SET_CARS_TO_STATE', cars);
//                     return cars
//                 })
//                 .catch((error) => {
//                     console.log(error)
//                     return error
//                 })
//
//         }
//     }, // Ассинхронные действия по отношению к мутациям
//     getters: {
//         CARS(state) {
//             return state.cars
//         }
//     }, // Короткий путь до получения данных в state
// })
// export default index;