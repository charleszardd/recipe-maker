<template>
    <v-container class="text-black main-font">
      <v-row justify="center">
        <v-col cols="12" md="8">
          <h1 class="text-center mb-5">Create New Recipe</h1>
  
          <v-form class="pb-10" @submit.prevent="submitRecipe">
            <v-text-field 
              label="Recipe Name" 
              v-model="recipe.name" 
              variant="outlined" 
              class="mb-5"
              required
            ></v-text-field>
  
            <v-row>
              <v-col cols="12" md="6">
                <p>Difficulty Level</p>
                <v-autocomplete
                  v-model="recipe.difficulty"
                  :items="difficulty"
                  label="Choose Difficulty"
                  placeholder="Select..."
                  variant="outlined"
                  required
                ></v-autocomplete>
              </v-col>
  
              <v-col cols="12" md="6">
                <p>Category</p>
                <v-autocomplete
                  v-model="recipe.category"
                  :items="categories"
                  label="Choose Category"
                  placeholder="Select..."
                  variant="outlined"
                  required
                ></v-autocomplete>
              </v-col>
            </v-row>
  
            <p>Ingredients</p>
            <v-textarea
              label="Ingredients (one per line)"
              v-model="recipe.ingredients"
              variant="outlined"
              class="mb-5"
              required
            ></v-textarea>
  
            <p>Instructions</p>
            <v-textarea
              label="Cooking Instructions"
              v-model="recipe.instructions"
              variant="outlined"
              class="mb-5"
              required
            ></v-textarea>
  
            <v-row>
              <v-col cols="6" md="3">
                <p>Calories</p>
                <v-text-field
                  label="Calories (kcal)"
                  v-model="recipe.calories"
                  type="number"
                  variant="outlined"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="6" md="3">
                <p>Protein</p>
                <v-text-field
                  label="Protein (g)"
                  v-model="recipe.protein"
                  type="number"
                  variant="outlined"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="6" md="3">
                <p>Carbs</p>
                <v-text-field 
                  label="Carbs (g)" 
                  v-model="recipe.carbs"
                  type="number"
                  variant="outlined"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="6" md="3">
                <p>Fats</p>
                <v-text-field 
                  label="Fats (g)" 
                  v-model="recipe.fats"
                  type="number"
                  variant="outlined"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
  
            <p class="mt-5 mb-2">Recipe Image</p>
            <div
              class="upload-container"
              @click="triggerFileUpload"
              @dragover.prevent
              @drop="handleDrop"
            >
              <input
                type="file"
                ref="fileInput"
                accept="image/*"
                class="d-none"
                @change="handleFileUpload"
              />
              <v-icon size="40" class="mb-2">mdi-cloud-upload</v-icon>
              <p class="text-subtitle-1">Click or drag an image here to upload</p>
              <p v-if="recipe.image" class="mt-2 text-success">{{ recipe.image.name }}</p>
            </div>
  
            <div class="d-flex justify-end mt-7">
              <Button variant="outlined" to="/recipes" class="mr-5 rounded-lg" height="45">Cancel</Button>
              <Button class="rounded-lg" height="45" @click="submitRecipe">Create Recipe</Button>
            </div>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import axios from "axios";
  
  const recipe = ref({
    name: "",
    difficulty: "",
    category: "",
    ingredients: "",
    instructions: "",
    calories: "",
    protein: "",
    carbs: "",
    fats: "",
    image: null,
  });
  
  const difficulty = ["Easy", "Medium", "Hard"];
  const categories = ["Breakfast", "Lunch", "Dinner", "Dessert", "Snack"];
  const fileInput = ref(null);
  
  const triggerFileUpload = () => {
    fileInput.value.click();
  };
  
  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      recipe.value.image = file;
    }
  };
  
  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
      recipe.value.image = file;
    }
  };
  
  const submitRecipe = async () => {
    try {
      const formData = new FormData();
      formData.append("name", recipe.value.name);
      formData.append("difficulty", recipe.value.difficulty);
      formData.append("category", recipe.value.category);
      formData.append("ingredients", recipe.value.ingredients);
      formData.append("instructions", recipe.value.instructions);
      formData.append("calories", recipe.value.calories);
      formData.append("protein", recipe.value.protein);
      formData.append("carbs", recipe.value.carbs);
      formData.append("fats", recipe.value.fats);
      if (recipe.value.image) {
        formData.append("image", recipe.value.image);
      }
  
      await axios.post("/api/recipes/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
  
      alert("Recipe added successfully!");
  
      recipe.value = {
        name: "",
        difficulty: "",
        category: "",
        ingredients: "",
        instructions: "",
        calories: "",
        protein: "",
        carbs: "",
        fats: "",
        image: null,
      };
    } catch (error) {
      console.error("Error adding recipe:", error);
    }
  };
  </script>
  
  <style scoped>
  .upload-container {
    width: 100%;
    height: 150px;
    border: 2px dashed #ccc;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: 0.3s;
    text-align: center;
  }
  
  .upload-container:hover {
    border-color: #42a5f5;
    background: rgba(66, 165, 245, 0.1);
  }
  </style>
  