<template>
    <v-app>
        <v-app-bar
                app
                color="#ff928f"
                dark
                shrink-on-scroll
                prominent
                src="./assets/herbalife-shake-stro.jpg"
                fade-img-on-scroll
        >
           <!-- <template v-slot:img="{ props }">
                <v-img
                        v-bind="props"
                        gradient="to top right, rgba(255,255,143,.9), rgba(255,255,255,.2)"
                ></v-img>
            </template>-->

            <v-app-bar-nav-icon></v-app-bar-nav-icon> <!-- Add the menu symbol on the left -->

            <v-toolbar-title style="width: 30%">
                <v-row no-gutters>
                    <v-col cols="1" align-self="center">
                        <v-img
                                src="./assets/logo.jpg"
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
                        prepend-inner-icon="search"
                        v-model="search"
                        clearable
                        single-line
                        light
                        solo
                >
                </v-text-field>
            </v-slide-x-transition>

            <v-btn icon>
                <v-icon @click="searchAvailable = !searchAvailable">mdi-magnify</v-icon>
            </v-btn>

            <v-btn icon>
                <v-icon>mdi-heart</v-icon>
            </v-btn>

            <v-btn icon> <!-- add the three dot botton -->
                <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>

            <template v-slot:extension> <!-- make the top image larger and add menues -->
                <v-tabs
                        align-with-title
                        background-color="transparent"
                >
                    <v-tab>Products</v-tab>
                    <v-tab>Category</v-tab>
                    <v-tab>Users</v-tab>
                </v-tabs>
            </template>

            <v-spacer></v-spacer>
            <v-btn text rounded>Home</v-btn>
            <v-btn text rounded>Login</v-btn>
        </v-app-bar>

        <v-content>
            <v-container>
                <product-list :search="search"></product-list>
            </v-container>


  <v-row justify="center">
    <v-btn
      color="primary"
      dark
      @click.stop="logindialog = true"
    >
      Open Dialog
    </v-btn>

    <v-dialog
      v-model="logindialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Use Google's location service?</v-card-title>

        <v-card-text>
          Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
        </v-card-text>

        <v-card-actions>
          <div class="flex-grow-1"></div>

          <v-btn
            color="green darken-1"
            text
            @click="logindialog = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="logindialog = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>



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
                    <v-btn color="success">Register</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn color="info">Login</v-btn>
                </v-card-action>
            </v-card>




<!--            <v-layout class="my-3 mx-5">
                <v-flex xs10>
                    <v-text-field
                            solo
                            label="Search ..."
                            prepend-inner-icon="mdi-magnify"
                            v-model="search">
                        >
                    </v-text-field>
                </v-flex>
                <v-flex xs2 class="ml-2 mt-1">
                    <v-btn block large @click="searchProducts" color="pink">Search</v-btn>
                </v-flex>
            </v-layout> -->


            <Product name="Formula_1"/>
<!--            <Product name="Niteworks"/>-->
            <Product :name="product.name" v-for="product in products" :key="product.name"/>
            <router-view></router-view>
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
    import Product from './components/Product';

    export default {
        name: 'App',
        components: {
            Product,
            // ProductList

        },
        data: () => ({//
            search: null,
            products: [],
            showPassword: false, //for the login
            links: [
                'Home',
                'Login'
            ],

            searchAvailable: false,
            search: null,
            logindialog: false,


        }),
        created() {

        },

        methods:{
            searchProducts()  {
                let params = {query: this.search};
                axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
                    this.products = response.data;
                });
            }
        }


    };
</script>
