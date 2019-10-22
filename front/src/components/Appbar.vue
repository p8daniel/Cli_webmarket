<template>

    <v-app>

        <v-navigation-drawer v-model="drawer" app temporary>
        <v-list>

                <v-list-item>
        <v-list-item-content>
        <v-list-item-title>Menu</v-list-item-title>
      </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

        </v-list>
        </v-navigation-drawer>


    <v-app-bar
                app
                color="#4CAF50"
                dark
                shrink-on-scroll
                prominent
                src="@/assets/herbalife-shake-stro.jpg"
                fade-img-on-scroll
        >
           <!-- <template v-slot:img="{ props }">
                <v-img
                        v-bind="props"
                        gradient="to top right, rgba(255,255,143,.9), rgba(255,255,255,.2)"
                ></v-img>
            </template>-->

            <v-app-bar-nav-icon @click="drawer =! drawer"></v-app-bar-nav-icon> <!-- Add the menu symbol on the left -->

            <v-toolbar-title style="width: 40%">
                <v-row no-gutters>
                    <v-col cols="1" align-self="center">
                        <v-img
                                src="@/assets/logo.jpg"
                                aspect-ratio="1"
                                max-width="30"
                        ></v-img>
                    </v-col>
                    <v-col cols="11">
                        <span class="headline font-weight-bold">Webmarket</span>
                    </v-col>
                </v-row>

            </v-toolbar-title>
            <!--            <v-toolbar-title class="headline text-uppercase">
                <span>Webmarket</span>
            </v-toolbar-title>-->
            <div class="flex-grow-1"></div>

            <v-slide-x-transition>
                <v-text-field
                        v-if="searchAvailable"
                        class="mr-2"
                        label="Search ..."

                        v-model="search_product"
                        clearable
                        single-line
                        light
                        solo
                        @keyup.enter="submit_search"
                >
                </v-text-field>

            </v-slide-x-transition>

            <v-btn icon>
                <v-icon @click="searchProducts">mdi-magnify</v-icon>
            </v-btn>

            <v-btn icon>
                <v-icon>mdi-heart</v-icon>
            </v-btn>
                    <v-spacer></v-spacer>

<!--            <v-btn icon> &lt;!&ndash; add the three dot botton &ndash;&gt;-->
<!--                <v-icon>mdi-dots-vertical</v-icon>-->
<!--            </v-btn>-->

            <v-btn icon href="/basket">
                <v-badge left color="green">
                    <span slot="badge"></span>
                <v-icon>shopping_cart</v-icon>
                    Basket
            </v-badge>

            </v-btn>

            <template v-slot:extension> <!-- make the top image larger and add menues -->
                <v-tabs
                        align-with-title
                        background-color="transparent"
                >

                    <v-menu >
                          <template v-slot:activator="{ on }">

                            <v-btn
                                   text
                              v-on="on"
                                   @click="getCategories"
                            >
                              Categories
                            </v-btn>

                          </template>

                        <v-list>
                            <v-list-item

                              v-for="(category, index) in categories"
                              :key="index"
                              :item="category"

                              @click="printsomething"
                            >
                              <v-list-item-title v-model="search_category">{{ category }}</v-list-item-title>
                            </v-list-item>
                          </v-list>
                        </v-menu>


                        <v-menu>

                        <template v-slot:activator="{ on }">
                        <v-btn text

                              v-on="on"
                                   @click="getProducts"
                        >
<!--                            <v-icon left>expand_more</v-icon>-->
                              Products

                              </v-btn>
                        </template>


                          <v-list>
                            <v-list-item

                              v-for="(product, index) in products"
                              :key="index"
                            >
                              <v-list-item-title>{{ product.name }}</v-list-item-title>
                            </v-list-item>
                          </v-list>
                        </v-menu>

                </v-tabs>
            </template>

            <v-spacer></v-spacer>
        <v-btn text rounded href="/">Home</v-btn>


<!--            <v-row justify="center">-->
            <v-btn
                    text
                    rounded
                  @click.stop="logindialog = true"
                >
                  Login
            </v-btn>

                <v-dialog
                  v-model="logindialog"
                  max-width="290"
                >
<!--                  <v-card>-->
<!--                    <v-card-title class="headline">Use Google's location service?</v-card-title>-->

                                        <!--login Module-->
                    <v-card width="400" class="ms-auto mt-5">
                    <v-card-title>
                        <h1 class="display-1">Login</h1>
                    </v-card-title>
                        <v-card-text>
                            <v-form>
                                <v-text-field
                                label="Username"
                                prepend-icon="mdi-account-circle"/>
                                <v-text-field
                                    :type="showPassword ? 'text': 'password'"
                                    label="Password"
                                    prepend-icon="mdi-lock"
                                    :append-icon="showPassword ? 'mdi-eye': 'mdi-eye-off'"
                                    @click:append="showPassword = !showPassword"
                                />
                            </v-form>
                        </v-card-text>
                        <v-card-action>
                            <v-btn color="success" href="/register">Register</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn color="info">Login</v-btn>
                        </v-card-action>

                    </v-card>

                </v-dialog>



        </v-app-bar>

    </v-app>
</template>

<script>

    import axios from 'axios';

    export default {
        name: "Navbar.vue",




    data: () => ({//

        categories: null,
        search_product: "",
        search_category:"",
        products: null,
        showPassword: false, //for the login
        links: [
            'Home',
            'Login'
        ],
        drawer: false,


        searchAvailable: false,
        logindialog: false,
        items: [{
            icon:'perm_identity',
            href: '#',
            title: 'Account'
        }]



    }),

        methods: {

            getCategories() {
                axios.get('http://localhost:8000/api/v1/categories').then((response) => {
                    this.categories = response.data;
                });
            }
            ,

            getProducts() {
                let params = {query: "", query2: ""};
                axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
                    this.products = response.data;
                });

            },
            searchProducts() {

                this.searchAvailable = !this.searchAvailable

                // debugger;
            },
            printsomething() {
                // eslint-disable-next-line no-console
                console.log(this.search_category)
            },
            submit_search() {

                this.$emit("inputData", this.search_product)
            }

    }
    };

</script>

<style scoped>

</style>