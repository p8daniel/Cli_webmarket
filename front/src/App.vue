<template>
        <v-app>

        <Appbar @inputData="updateSearch" @inputData2="updateSearch2"/>


        <v-content>
            <v-container>
<!--                <product-list :search="search" :search_category="search_category"></product-list>-->
                <router-view :to="{ name: 'Home', params: {search:this.search, search_category:this.search_category}}"> </router-view>




            </v-container>


        </v-content>



        <BottomBar/>


    </v-app>


</template>


<script>
    // import axios from 'axios';
    // import Product from './components/Product';
    //import ProductList from './components/ProductList';
    import Appbar from "./components/Appbar";
    import BottomBar from "./components/BottomBar";




    export default {
        name: 'App',
        components: {
                //Product,
               // ProductList,
                Appbar,
                BottomBar

            },
            data: () => ({//
                search: "",
                search_category: "",
                categories: null,
                products: null,
                showPassword: false, //for the login
                links: [
                    'Home',
                    'Login'
                ],

                searchAvailable: false,
                logindialog: false,



            }),
            created() {

            },


             methods:{
                updateSearch(variable) {
                    this.search=variable
                },
                updateSearch2(variable) {
                    this.search_category=variable
                }

                // searchProducts()  {
                //
                //
                //     let params = {query: this.search, query2: this.search_category};
                //     axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
                //     this.products = response.data;
                //         console.log(this.products)
                //     });
            },
        //     getCategories() {
        //         axios.get('http://localhost:8000/api/v1/categories').then((response) => {
        //             this.categories = response.data;
        //         });
        //     },
        //
        //     getProducts() {
        //         let params = {query: ""};
        //         axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
        //             this.products = response.data;
        //         });
        //
        //     }
        // }


        };
</script>
