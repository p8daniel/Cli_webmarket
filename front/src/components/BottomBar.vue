<template>
        <!-- footbar -->
        <v-footer
            color="#4CAF50"
            padless
        >
            <v-row
              justify="center"
              no-gutters
            >
              <v-btn
                v-for="icon in icons"
                :key="icon"
                color="white"
                text
                rounded
                class="my-2"
              >
                  <v-icon >{{ icon }}</v-icon>
              </v-btn>
              <v-col
                class="#4CAF50 py-4 text-center white--text"
                cols="12"
              >
                {{ new Date().getFullYear() }} — <strong>Cli_webmarket</strong>
              </v-col>
            </v-row>
        </v-footer>



<!--    <v-card color="#4CAF50" height="60px" class="white hidden-sm-and-up" flat>-->
<!--    <v-bottom-nav-->
<!--      :active.sync="bottomNav"-->
<!--      :value="true"-->
<!--      app-->
<!--      color="white"-->
<!--      class="elevation-2"-->

<!--    >-->
<!--      <v-btn-->
<!--        color="#518FF5"-->
<!--        flat-->
<!--        value="Home"-->
<!--        router-->
<!--        to="/home"-->
<!--      >-->
<!--        <span>Home</span>-->
<!--        <v-icon>dashboard</v-icon>-->
<!--      </v-btn>-->

<!--      <v-btn-->
<!--        color="#518FF5"-->
<!--        flat-->
<!--        value="events"-->
<!--        router-->
<!--        to="/events"-->
<!--      >-->
<!--        <span>Events</span>-->
<!--        <v-icon>rounded_corner</v-icon>-->
<!--      </v-btn>-->

<!--      <v-btn-->
<!--        color="#518FF5"-->
<!--        flat-->
<!--        value="team"-->
<!--        router-->
<!--        to="/team"-->
<!--      >-->
<!--        <span>Team</span>-->
<!--        <v-icon>group</v-icon>-->
<!--      </v-btn>-->

<!--      <v-btn-->
<!--        color="#518FF5"-->
<!--        flat-->
<!--        value="about"-->
<!--        router-->
<!--        to="/about"-->
<!--      >-->
<!--        <span>About</span>-->
<!--        <v-icon>toc</v-icon>-->
<!--      </v-btn>-->



<!--      &lt;!&ndash; <v-btn-->
<!--        color="#518FF5"-->
<!--        flat-->
<!--        value="contact"-->
<!--        router-->
<!--        to="/contact"-->
<!--      >-->
<!--        <span>Contant</span>-->
<!--        <v-icon>person</v-icon>-->
<!--      </v-btn> &ndash;&gt;-->

<!--    </v-bottom-nav>-->
<!--  </v-card>-->

</template>

<script>
    export default {
        name: "BottomBar",

    data () {
         return {
    //     bottomNav: 'recent',
    //      links: [
    //          { title: 'Home', icon: 'dashboard', route:"/home" },
    //         { title: 'Attending', icon: 'rounded_corner', route:"/attending" },
    //         { title: 'Sessions', icon: 'toc', route:"/sessions" },
    //         { title: 'Speakers', icon: 'group', route:"/speakers" }
      //  ],
             icons: [
                    'fab fa-facebook',
                 'fab fa-twitter',
                 'fab fa-google-plus',
                 'fab fa-linkedin',
                 'fab fa-instagram',


             ]
       }
    }
    }
</script>

<style scoped>

</style>