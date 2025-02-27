<template>
  <v-container class="main-font text-black">
    <v-row class="justify-space-between mt-5 px-3" align="center">
      <h1>Recipes</h1>
      <Button
        height="45"
        to="/create-recipe"
        class="rounded-lg"
        icon="mdi-plus"
        :noSpacing="false"
        >Create Recipe</Button
      >
    </v-row>

    <v-row>
      <v-col v-for="recipe in recipes" :key="recipe.id" cols="12" md="4">
        <v-card class="rounded-lg bg-grey-lighten-3" elevation="5">
          <div
            class="image-container"
            @mouseenter="recipe.isHovering = true"
            @mouseleave="recipe.isHovering = false"
          >
            <v-img
              :src="getImageUrl(recipe.image)"
              cover
              height="200"
              class="rounded-t-lg"
            />

            <div v-if="recipe.isHovering" class="hover-actions">
              <v-btn
                icon="mdi-pencil"
                class="text-grey-darken-4"
                @click="openEditModal(recipe)"
              />
              <v-btn
                icon="mdi-delete"
                class="text-grey-darken-4"
                @click="deleteRecipe(recipe.id)"
              />
            </div>
            <v-col>
              <v-row class="d-flex justify-space-between" align="center">
                <v-card-title class="text-h6 font-weight-bold">
                  {{ recipe.name }}
                </v-card-title>
                <v-icon class="mr-3 text-grey-darken-2"
                  >mdi-heart-outline</v-icon
                >
              </v-row>
            </v-col>

            <v-card-subtitle class="mb-3 text-grey-darken-2">
              <v-chip class="mr-2 text-grey-darken-4" label>{{ recipe.category }}</v-chip>
              <v-chip :color="getDifficultyColor(recipe.difficulty)" label>
                {{ recipe.difficulty }}
              </v-chip>
            </v-card-subtitle>

            <v-card-text class="py-0">
              <p class="text-subtitle-1 font-weight-medium">Ingredients:</p>
              <ul class="pl-3">
                <li
                  v-for="ingredient in recipe.ingredients.split('\n')"
                  :key="ingredient"
                  class="text-body-2 text-grey-darken-2"
                >
                  {{ ingredient }}
                </li>
              </ul>
            </v-card-text>

            <v-card-text>
              <p class="text-subtitle-1 font-weight-medium">Instructions:</p>
              <p class="text-body-2 text-grey-darken-2">
                {{ recipe.instructions }}
              </p>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-text>
              <p class="text-subtitle-1 font-weight-medium">Nutrition Info</p>
              <v-row>
                <v-col cols="6" sm="3" class="text-center">
                  <v-card
                    height="55"
                    flat
                    class="pa-2 text-body-2"
                    :color="getNutritionColor('calories', recipe.calories)"
                  >
                    <v-col class="px-0 py-0">
                      <v-card-subtitle
                        class="text-subtitle-1 font-weight-bold px-0 py"
                      >
                        {{ recipe.calories }}g
                      </v-card-subtitle>
                      <v-card-subtitle class="py-0 px-0">kcal</v-card-subtitle>
                    </v-col>
                  </v-card>
                </v-col>

                <v-col cols="6" sm="3" class="text-center">
                  <v-card
                    height="55"
                    flat
                    class="pa-2 text-body-2"
                    :color="getNutritionColor('protein', recipe.protein)"
                  >
                    <v-col class="px-0 py-0">
                      <v-card-subtitle
                        class="text-subtitle-1 font-weight-bold px-0 py"
                      >
                        {{ recipe.protein }}g
                      </v-card-subtitle>
                      <v-card-subtitle class="py-0 px-0"
                        >protein</v-card-subtitle
                      >
                    </v-col>
                  </v-card>
                </v-col>

                <v-col cols="6" sm="3" class="text-center">
                  <v-card
                    height="55"
                    flat
                    class="pa-2 text-body-2"
                    :color="getNutritionColor('fats', recipe.fats)"
                  >
                    <v-col class="px-0 py-0">
                      <v-card-subtitle
                        class="text-subtitle-1 font-weight-bold px-0 py"
                      >
                        {{ recipe.fats }}g
                      </v-card-subtitle>
                      <v-card-subtitle class="py-0 px-0">fats</v-card-subtitle>
                    </v-col>
                  </v-card>
                </v-col>

                <v-col cols="6" sm="3" class="text-center">
                  <v-card
                    height="55"
                    flat
                    class="pa-2 text-body-2"
                    :color="getNutritionColor('carbs', recipe.carbs)"
                  >
                    <v-col class="px-0 py-0">
                      <v-card-subtitle
                        class="text-subtitle-1 font-weight-bold px-0 py"
                      >
                        {{ recipe.carbs }}g
                      </v-card-subtitle>
                      <v-card-subtitle class="py-0 px-0">carbs</v-card-subtitle>
                    </v-col>
                  </v-card>
                </v-col>
              </v-row>
            </v-card-text>
          </div>
        </v-card>
      </v-col>
    </v-row>

    <v-dialog v-model="editModalOpen" max-width="800" persistent>
      <v-card class="pa-4">
        <v-card-title class="text-h5 font-weight-bold">
          <v-row align="center">
            <v-col>Edit Recipe</v-col>
            <v-col cols="auto">
              <v-btn
                icon="mdi-close"
                variant="text"
                @click="closeEditModal"
              ></v-btn>
            </v-col>
          </v-row>
        </v-card-title>

        <v-divider class="mb-4"></v-divider>

        <v-card-text>
          <v-form ref="editForm" @submit.prevent="updateRecipe">
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="editedRecipe.name"
                  label="Recipe Name"
                  variant="outlined"
                  required
                  class="mb-4"
                ></v-text-field>

                <v-select
                  v-model="editedRecipe.category"
                  :items="categories"
                  label="Category"
                  variant="outlined"
                  class="mb-4"
                ></v-select>

                <v-select
                  v-model="editedRecipe.difficulty"
                  :items="difficulties"
                  label="Difficulty"
                  variant="outlined"
                  class="mb-4"
                ></v-select>

                <v-file-input
                  label="Recipe Image"
                  variant="outlined"
                  :prepend-icon="false"
                  prepend-inner-icon="mdi-image"
                  accept="image/*"
                  class="mb-4"
                  @change="handleImageUpload"
                ></v-file-input>

                <v-row>
                  <v-col cols="6">
                    <v-text-field
                      v-model="editedRecipe.calories"
                      label="Calories"
                      type="number"
                      variant="outlined"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field
                      v-model="editedRecipe.protein"
                      label="Protein (g)"
                      type="number"
                      variant="outlined"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col cols="6">
                    <v-text-field
                      v-model="editedRecipe.fats"
                      label="Fats (g)"
                      type="number"
                      variant="outlined"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field
                      v-model="editedRecipe.carbs"
                      label="Carbs (g)"
                      type="number"
                      variant="outlined"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-col>

              <v-col cols="12" md="6">
                <v-textarea
                  v-model="editedRecipe.ingredients"
                  label="Ingredients (one per line)"
                  variant="outlined"
                  rows="6"
                  class="mb-4"
                  placeholder="1 cup flour
  2 eggs
  1/2 tsp salt"
                ></v-textarea>

                <v-textarea
                  v-model="editedRecipe.instructions"
                  label="Instructions"
                  variant="outlined"
                  rows="8"
                  placeholder="Step-by-step instructions for preparing the recipe..."
                ></v-textarea>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>

        <v-card-actions class="pt-0">
          <v-spacer></v-spacer>
          <v-btn
            variant="tonal"
            color="error"
            @click="closeEditModal"
            class="mr-3"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            @click="updateRecipe"
            variant="elevated"
            :loading="isUpdating"
          >
            Update Recipe
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>
  
  <script setup>
import { ref, onMounted, reactive } from "vue";
import axios from "axios";

const recipes = ref([]);
const editModalOpen = ref(false);
const editedRecipe = ref({});
const isUpdating = ref(false);
const editForm = ref(null);

const categories = [
  "Breakfast",
  "Lunch",
  "Dinner",
  "Dessert",
  "Snack",
  "Appetizer",
];
const difficulties = ["Easy", "Medium", "Hard"];

const getImageUrl = (image) => image || "/placeholder-image.jpg";

const getDifficultyColor = (difficulty) => {
  return (
    {
      Easy: "green-darken-2",
      Medium: "orange-darken-2",
      Hard: "red-darken-2",
    }[difficulty] || "grey-darken-1"
  );
};

const getNutritionColor = (type, value) => {
  const thresholds = {
    calories: [200, 500],
    protein: [15],
    fats: [10, 20],
    carbs: [30, 60],
  };
  const colors = ["green-lighten-3", "orange-lighten-3", "red-lighten-3"];
  return colors[thresholds[type]?.findIndex((t) => value < t) ?? 2];
};

const fetchRecipes = async () => {
  try {
    const response = await axios.get("/api/recipes/");

    recipes.value = response.data.map((recipe) => ({
      ...recipe,
      isHovering: false,
    }));
  } catch (error) {
    console.error("Error fetching recipes:", error);
  }
};

const openEditModal = (recipe) => {
  editedRecipe.value = JSON.parse(JSON.stringify(recipe));
  editModalOpen.value = true;
};

const closeEditModal = () => {
  editModalOpen.value = false;

  setTimeout(() => {
    editedRecipe.value = {};
  }, 300);
};

const handleImageUpload = (event) => {
  const file = event?.target?.files?.[0];
  if (!file) return;

  editedRecipe.value.image = file;
};

const updateRecipe = async () => {
  if (!editedRecipe.value.id) return;

  isUpdating.value = true;

  try {
    const formData = new FormData();

    const numericFields = ["calories", "protein", "fats", "carbs"];
    numericFields.forEach((field) => {
      formData.append(field, Number(editedRecipe.value[field]));
    });

    formData.append("name", editedRecipe.value.name);
    formData.append("category", editedRecipe.value.category);
    formData.append("difficulty", editedRecipe.value.difficulty);

    formData.append("ingredients", editedRecipe.value.ingredients || "");
    formData.append("instructions", editedRecipe.value.instructions || "");

    if (editedRecipe.value.image instanceof File) {
      formData.append("image", editedRecipe.value.image);
    }

    await axios.put(`/api/recipes/${editedRecipe.value.id}/`, formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    const index = recipes.value.findIndex(
      (r) => r.id === editedRecipe.value.id
    );
    if (index !== -1) {
      const isHovering = recipes.value[index].isHovering;
      recipes.value[index] = { ...editedRecipe.value, isHovering };
    }

    closeEditModal();
  } catch (error) {
    console.error("Error updating recipe:", error);
  } finally {
    isUpdating.value = false;
  }
};

const deleteRecipe = async (id) => {
  if (!confirm("Are you sure you want to delete this recipe?")) return;
  try {
    await axios.delete(`/api/recipes/${id}/`);
    recipes.value = recipes.value.filter((recipe) => recipe.id !== id);
  } catch (error) {
    console.error("Error deleting recipe:", error);
  }
};

onMounted(fetchRecipes);
</script>
  
  <style scoped>
.image-container {
  position: relative;
}

.hover-actions {
  position: absolute;
  top: 10px;
  right: 10px;
  display: flex;
  gap: 8px;
  z-index: 10;
}

.hover-actions .v-btn {
  background-color: rgba(110, 108, 108, 0.8);
  transition: background-color 0.2s;
}

.hover-actions .v-btn:hover {
  background-color: rgba(255, 255, 255, 1);
}

.v-dialog {
  transition: opacity 0.3s, transform 0.3s;
}

.v-card {
  transition: all 0.3s;
}
</style>