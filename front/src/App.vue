<template>
    <v-app>

        <Appbar />

        <v-content>
            <v-container>
                <product-list :search="search"></product-list>
            </v-container>


<!--            <Product name="Formula_1"/>-->
<!--&lt;!&ndash;            <Product name="Niteworks"/>&ndash;&gt;-->
<!--            <Product :name="product.name" v-for="product in products" :key="product.name"/>-->
<!--            <router-view></router-view>-->
        </v-content>



    <!-- footbar -->
        <v-footer
    color="primary lighten-1"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
      <v-col
        class="primary lighten-2 py-4 text-center white--text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Vuetify test</strong>
      </v-col>
    </v-row>
    </v-footer>


    </v-app>


</template>


<script>
    import axios from 'axios';
    // import Product from './components/Product';
    import ProductList from './components/ProductList';
    import Appbar from "./components/Appbar";

    export default {
        name: 'App',
        components: {
                //Product,
                ProductList,
                Appbar

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

        // methods:{
        //     // searchProducts()  {
        //     //     let params = {query: this.search};
        //     //     axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
        //     //         this.products = response.data;
        //     //         console.log(this.products)
        //     //     });
        //     // },
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
