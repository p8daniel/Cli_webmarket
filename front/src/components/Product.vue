<template>
    <v-container>
        <v-layout v-if="product !== null">
            <v-flex xs12>
                <v-card class="mx-auto">
                    <v-list-item three-line>
                            <v-list-item-content>

                                <v-card-title>{{ product.name }}</v-card-title>
                                <v-card-text>{{ product.categories }}</v-card-text>
                            </v-list-item-content>
                            <v-list-item-avatar
                                tile
                                size="100"
                        >
                            <v-img
                                    :src="product.sprite"
                                    aspect-ratio="1"
                            ></v-img>
                            </v-list-item-avatar>
                        </v-list-item>

                        <v-card-actions>

                            <v-chip v-for="type in product.categories" class="mx-1">{{ type }}</v-chip>
                            <v-spacer></v-spacer>

                            <v-btn text icon color="red" @click="deleteProduct">
                                <v-icon>mdi-delete</v-icon>
                            </v-btn>

                        </v-card-actions>

                    </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>



<script>
    import axios from 'axios';

    export default {
        props: ['name'],
        data: () => ({
            product: null
        }),
        created() {
            axios.get('http://localhost:8000/api/v1/product/' + this.name).then((response) => {
                this.product = response.data;
            }).catch(function (error) {
    // handle error
    console.log(error);});
        },
        methods: {
            deleteProduct() {
                axios.delete('http://localhost:8000/api/v1/product/' + this.name).then((response) => {
                });
            }
        }



    };
</script>
