<template>
    <div class="product">
        <v-card class="mx-auto" hover>
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title class="display-1 text--primary mb-1">{{ product.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ product.stats }}</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar
                        tile
                        size="80"
                >
                    <v-img
                            :src="product.sprite_front"
                            aspect-ratio="1"
                    ></v-img>
                </v-list-item-avatar>
            </v-list-item>

            <v-card-actions>
                <v-chip v-for="type in product.types" class="mx-1" :key="type">{{ type }}</v-chip>
                <v-spacer></v-spacer>
                <v-btn text icon color="blue" @click="">
                    <v-icon>edit</v-icon>
                </v-btn>
                <v-btn text icon color="red" @click="">
                    <v-icon>delete</v-icon>
                </v-btn>
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
                                <v-col cols="12" sm="6" md="4" v-for="stat in Object.keys(product_edited.stats)" :key="stat">
                                    <v-text-field
                                            :label="stat"
                                            v-model="product_edited.stats[stat]"
                                            outlined
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-select
                                            v-model="product_edited.types"
                                            :items="types"
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
        //props: ['name'],
        props: ['product'],
        data: () => ({
            //product: null
            edit: false,
            product_edited: null,
            category: null,
        }),


// /*        methods: {
//             startEditProduct() {
//                 this.types = [];
//                 this.product_edited = {
//                     stats: {},
//                     types: []
//                 };
//                 Object.keys(this.product.stats).forEach((stat) => {
//                     this.product_edited.stats[stat] = this.product.stats[stat];
//                 });
//                 this.product.types.forEach((type) => {
//                     this.product_edited.types.push(type);
//                     this.types.push(type);
//                 });
//
//                 axios.get('http://localhost:8000/api/v1/types').then((response) => {
//                     this.types = response.data;
//                 });
//
//                 this.edit = true;
//             },
//             editProduct() {
//                 axios.patch('http://localhost:8000/api/v1/product/' + this.product.name, this.product_edited).then(() => {
//                     this.$emit('update');
//                     // console.log(JSON.stringify(response.data));
//                 });
//                 // console.log("test")
//                 this.edit = false;
//             },
//             deleteProduct() {
//                 axios.delete('http://localhost:8000/api/v1/product/' + this.product.name).then(() => {
//                     this.$emit('delete');
//                 });
//             }*/
//         }

/*        created() {
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
        }*/



    };
</script>
