<template>
    <v-app>

        <Appbar @search="searchProducts">
        </Appbar>

        <v-content>
            <v-container>
                <product-list :search="search"></product-list>
            </v-container>


<!--            <Product name="Formula_1"/>-->
<!--&lt;!&ndash;            <Product name="Niteworks"/>&ndash;&gt;-->
<!--            <Product :name="product.name" v-for="product in products" :key="product.name"/>-->
<!--            <router-view></router-view>-->
        </v-content>



    <BottomBar/>


    </v-app>


</template>


<script>
    import axios from 'axios';
    // import Product from './components/Product';
    import ProductList from './components/ProductList';
    import Appbar from "./components/Appbar";
    import BottomBar from "./components/BottomBar";




    export default {
        name: 'App',
        components: {
                //Product,
                ProductList,
                Appbar,
                BottomBar

            },
            data: () => ({//
                search: null,
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
            searchProducts()  {
                let params = {query: this.search};
                axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
                    this.products = response.data;
                    console.log(this.products)
                });
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
        }


        };
</script>
