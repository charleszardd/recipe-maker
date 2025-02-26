<template>
    <v-container fluid class="bg-main recipe-container main-font text-black">
      <v-row class="d-flex justify-center">
        <v-col class="text-center d-flex justify-center flex-column">
          <h1 class="text-h3 font-weight-bold mb-3">Create Delicious Recipes with AI</h1>
          <p class="text-grey-darken-1">
            Transform your ingredients into amazing dishes with our smart generator.
          </p>
          <p class="text-grey-darken-1">Perfect for home cooks and professionals alike.</p>
          <div class="mt-5">
            <Button height="45" elevation="5"  width="150" variant="outlined" class="mr-5 rounded-lg">Watch Demo</Button>
            <Button height="45" elevation="5" width="150" to="/create-recipe" class="rounded-lg">Create Recipe</Button>
          </div>
  
          <v-row class="d-flex justify-center mt-10">
            <v-col cols="12" md="8" lg="6" class="d-flex justify-center">
              <v-card
                elevation="10"
                class="card rounded-lg bg-grey-lighten-3 mt-5 d-flex flex-column align-center justify-center"
                height="auto"
                max-width="650"
                width="100%"
              >

                <div class="chat-wrapper d-flex align-center justify-center w-100">
                  <chat-container />
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <style scoped>
  .chat-wrapper {
    display: flex;
    width: 100%;
    padding-top: 1rem;
  }

  .recipe-container{
    padding-top: 5rem;
    height: 100vh;
    display: flex;
    align-items: center;
  }
  </style>
  