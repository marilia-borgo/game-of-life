<template>
  <v-app>
    <v-card flat>
    <v-toolbar
      color="red darken-4"
      dark
      extended
      flat
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
    </v-toolbar>

    <v-card
      class="mx-auto"
      max-width="700"
      style="margin-top: -64px;"
    >
      <v-toolbar flat>
        <v-toolbar-title class="grey--text">
          Conway’s Game Of Life
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon href="https://github.com/marilia-borgo/game-of-life">
          <v-img src="../src/assets/github.png"  height="37px"
           width="37px"/> 
        </v-btn>

      </v-toolbar>

      <v-divider></v-divider>
      <v-main
    class="mt-8 mx-8"
    >
      <HelloWorld/>
    </v-main>
      <v-card-text style="height: 200px;"></v-card-text>
    </v-card>
  </v-card>
   
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
