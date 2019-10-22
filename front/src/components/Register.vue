<template>

 <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="newclient.name"
      :counter="10"
      :rules="nameRules"
      label="First name"
      required
    ></v-text-field>

         <v-text-field
      v-model="newclient.surname"
      :counter="10"
      :rules="nameRules"
      label="Last name"
      required
    ></v-text-field>

    <v-text-field
      v-model="newclient.email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

     <v-text-field
      v-model="newclient.password"
      :rules="passwordRules"
      label="Password"
      required
    ></v-text-field>

<!--    <v-select-->
<!--      v-model="select"-->
<!--      :items="items"-->
<!--      :rules="[v => !!v || 'Item is required']"-->
<!--      label="Item"-->
<!--      required-->
<!--    ></v-select>-->

<!--    <v-checkbox-->
<!--      v-model="checkbox"-->
<!--      :rules="[v => !!v || 'You must agree to continue!']"-->
<!--      label="Do you agree?"-->
<!--      required-->
<!--    ></v-checkbox>-->

    <v-btn
      color="success"
      class="mr-4"
      @click="RegisterClientt"
    >
      Submit
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click=""
      href="/"
    >
      Cancel
    </v-btn>

<!--    <v-btn-->
<!--      color="warning"-->
<!--      @click="resetValidation"-->
<!--    >-->
<!--      Reset Validation-->
<!--    </v-btn>-->
  </v-form>



</template>

<script>
    import axios from 'axios';

    export default {
        // name: "Register.vue",
        data: () => ({
            newclient: {
                "name":"",
                "surname":"",
                "email":"",
                "password":"",
            }

        }),

        // components: {
        //     Client,
        // },

        methods: {
            RegisterClientt() {
                // eslint-disable-next-line no-console
                console.log(this.newclient)

                axios.post('http://localhost:8000/api/v1/client/', this.newclient).then(() => {
                this.$emit('client added');
                    // console.log(JSON.stringify(response.data));
                });

            }

        }



    }
</script>

<style>

</style>