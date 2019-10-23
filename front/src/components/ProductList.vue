<template>
    <v-slide-y-transition
            mode="in-out"
            class="row py-2"
            group
            tag="div"
    >
        <v-col cols="6" v-for="product in products" :key="product.name">
            <Product :product="product" @delete="deleteProduct(product)"
                     @update="updateProduct(product)"/>
        </v-col>
    </v-slide-y-transition>
</template>

<script>
    import axios from 'axios';
    import Product from './Product';


    export default {
        name: "ProductList",
        // props: ['search','search_category'],
        props:{
            search: {
                type: String,
                default: ""
            },
            search_category: {
                type: String,
                default: ""

            }
        },
        data: () => ({
            products: [],
            // search: this.$router.params.search,
            // search_category: this.$router.params.search_category

        }),
        components: {
            Product,
        },
        watch: {
            search() {
                this.searchProducts();
            }
        },
        created() {
            this.searchProducts();

        },
        methods: {
            searchProducts() {
                let search = this.search;
                if (!search) {
                    search = "";
                }
                let search_category = this.search_category;
                if (!search_category) {
                    search_category = "";
                }

                let params = {query: search,query2: search_category};
                axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
                    this.products = response.data;
                });
            },
            updateProduct(product) {
                axios.get('http://localhost:8000/api/v1/product/' + product.name).then((response) => {
                    let index_of_product = this.products.indexOf(product);

                    let new_product = response.data;
                    this.products.splice(index_of_product, 1, new_product);
                });
            },
            deleteProduct(product) {
                let index_of_product = this.products.indexOf(product);
                this.products.splice(index_of_product, 1);
            }
        }
    }
</script>

<style scoped>

</style>