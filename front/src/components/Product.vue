<template>
    <div class="product">
        <v-card class="mx-auto" hover>
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title class="display-1 text--primary mb-1">{{ product.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ product.detail}}</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar
                        tile
                        size="80"
                >
                    <v-img
                            :src="product.sprite"
                            aspect-ratio="1"
                    ></v-img>
                </v-list-item-avatar>
            </v-list-item>

            <v-col class="d-flex" cols="12" sm="6">
                    <v-select

                      :items= (v-for="taste.name in product.tastes")
                      label="Select taste"
                      solo
                    ></v-select>

            </v-col>
            <v-col class="text-right">
                price: {{product.price}} &#8364;
            </v-col>


            <v-card-actions>
                <v-chip v-for="category in product.categories" class="mx-1" :key="category">{{ category }}</v-chip>
                <v-spacer></v-spacer>
                <v-btn text icon color="blue" @click="startEditProduct">
                    <v-icon>edit</v-icon>
                </v-btn>
                <v-btn text icon color="red" @click="deleteProduct">
                    <v-icon>delete</v-icon>
                </v-btn>
                <v-btn text icon color="green" @click="">
                    <v-icon>shopping_cart</v-icon>
                </v-btn>


<!--                <a-->
<!--                :href="product.label"><v-icon text icon color="green" >note</v-icon>-->
<!--                </a>-->


            </v-card-actions>
        </v-card>

        <v-row justify="center">
            <v-dialog v-model="edit" persistent max-width="600px">
                <v-card v-if="product_edited">
                    <v-card-title class="mb-1">
                        <span class="display-1">{{ product.name }}</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
<!--                                <v-col cols="12" sm="6" md="4" v-for="stat in Object.keys(product_edited.stats)" :key="stat">-->
<!--                                    <v-text-field-->
<!--                                            :label="stat"-->
<!--                                            v-model="product_edited.stats[stat]"-->
<!--                                            outlined-->
<!--                                    ></v-text-field>-->
<!--                                </v-col>-->
                                <v-col cols="12">
                                    <v-select
                                            v-model="product_edited.categories"
                                            :items="categories"
                                            chips
                                            label="Types"
                                            multiple
                                            outlined
                                    ></v-select>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <div class="flex-grow-1"></div>
                        <v-btn color="grey darken-1" text @click="edit = false">Close</v-btn>
                        <v-btn color="primary" @click="editProduct">Save</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-row>
    </div>
</template>



<script>
    import axios from 'axios';

    export default {
        props: ['product'],
        data: () => ({
            edit: false,
            product_edited: null,
            categories: null,
            items:[
                'a',
                'b',
                'c',
            ],
            mytastes: null
        }),

        methods: {
            startEditProduct() {
                this.categories = [];
                this.product_edited = {
                    // stats: {},
                    categories: []
                };
                // Object.keys(this.product.stats).forEach((stat) => {
                //     this.product_edited.stats[stat] = this.product.stats[stat];
                // });
                this.product.categories.forEach((category) => {
                    this.product_edited.categories.push(category);
                    this.categories.push(category);
                });

                axios.get('http://localhost:8000/api/v1/categories').then((response) => {
                    this.categories = response.data;
                });

                this.edit = true;
            },
            editProduct() {
                axios.patch('http://localhost:8000/api/v1/product/' + this.product.name, this.product_edited).then(() => {
                    this.$emit('update');
                    // console.log(JSON.stringify(response.data));
                });
                // console.log("test")
                this.edit = false;
            },
            deleteProduct() {
                axios.delete('http://localhost:8000/api/v1/product/' + this.product.name).then(() => {
                    this.$emit('delete');
                });
            },
            getlitTastes()
            {

            }
        }
    };
</script>
