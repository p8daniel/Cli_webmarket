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
      :rules="emailRules"
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

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="RegisterClientt"
    >
      Submit
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
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

                console.log("newclient")

                // axios.post('http://localhost:8000/api/v1/client/' + this.client.name, this.product_edited).then(() => {
                //     this.$emit('client added');
                    // console.log(JSON.stringify(response.data));
                // });

            }

        }



    }
</script>

<style scoped>

</style>