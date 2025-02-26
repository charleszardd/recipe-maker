<template>
  
      <v-text-field
        v-model="message"
        label="Enter your ingredients..."
        prepend-inner-icon="mdi-carrot"
        clearable
        auto-grow
        max-height="900"
        variant="outlined"
        rows="1"
        outlined
        max-width="600"
        class="custom-textarea"
      >
        <template v-slot:append-inner>
          <Button @click="generateRecipe">
            Generate Recipe
          </Button>
        </template>
      </v-text-field>

  </template>
  
  <script setup>
//   import { ref } from "vue";
  
//   const message = ref("");
  
//   const generateRecipe = () => {
//     console.log("Generating recipe with ingredients:", message.value);
//   };
  </script>
  
  <style scoped>

  </style>
  