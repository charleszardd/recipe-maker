<template>
    <v-container class="main-font text-black">
        <h1 class="text-center">Why Choose Recipe Maker</h1>
        <v-row class="my-10" justify="center">
            <v-col v-for="(detailsCards, index) in cards" :key="index" cols="12" sm="6" md="4">
                <v-card height="auto" class="bg-grey-lighten-2 rounded-lg" elevation="5">
                    <v-card-title class="pb-0">
                        <v-icon class="mr-2">{{ detailsCards.icon }}</v-icon>
                    </v-card-title>
                    <v-card-title class="d-flex align-center mb-5 py-0">
                        {{ detailsCards.title }}
                    </v-card-title>
                    <v-card-text class="text-grey-darken-3">{{ detailsCards.description }}</v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <feedback />
        <user-engagement-section />
    </v-container>
</template>

<script setup>
import { ref } from "vue";

const cards = ref([
    {
        icon: "mdi-auto-fix",
        title: "AI-Powered Suggestions",
        description: "Get personalized recipe recommendations based on your ingredients and preferences."
    },
    {
        icon: "mdi-clock-outline",
        title: "Save Time",
        description: "Generate complete recipes with instructions in seconds, not hours."
    },
    {
        icon: "mdi-file-plus",
        title: "Recipe Creator",
        description: "You can create your own recipes and share them with the world."
    },
]);
</script>
