<template>
    <div class="py-10">
        <h1 class="text-center">What Our Users Say</h1>
        <v-row class="pt-10" justify="center">
            <v-col v-for="(userFeedback, index) in feedbacks" :key="index" cols="12" sm="8" md="6" lg="4">
                <v-card height="200" class="bg-grey-lighten-3 px-4 py-5 rounded-lg" elevation="5">
                    <v-row no-gutters align="center">
                        <v-avatar size="50" class="mr-3">
                            <v-img :src="userFeedback.profileImage" />
                        </v-avatar>
                        <div>
                            <v-card-title class="py-0 text-subtitle-1">{{ userFeedback.userName }}</v-card-title>
                            <v-card-subtitle class="text-subtitle-2">{{ userFeedback.userRole }}</v-card-subtitle>
                        </div>
                    </v-row>

                    <v-card-text class="text-grey-darken-4 text-subtitle-1 px-0 text-wrap mt-3">
                        ‟ {{ userFeedback.feedback }} ”
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script setup>
import { ref } from "vue";

const feedbacks = ref([
    {
        profileImage: '/download.webp',
        userName: "Maria DB",
        userRole: "Home Cook",
        feedback: 'RecipeMaker has transformed how I cook. I never waste ingredients anymore!'
    },
    {
        profileImage: '/pfp.png',
        userName: "Java Doe",
        userRole: "Professional Chef",
        feedback: 'The AI suggestions are incredibly creative and help me develop new dishes.'
    },
    {
        profileImage: '/baek.webp',
        userName: "Baek Hyun Min",
        userRole: "Actress/ Model/ Health Enthusiast",
        feedback: 'As someone conscious about health and nutrition, RecipeMaker helps me discover delicious yet healthy meal options tailored to my lifestyle.'
    },
    {
        profileImage: '/jani.webp',
        userName: "Jhonny Seens",
        userRole: "Chef Wannabe",
        feedback: 'RecipeMaker has been a game-changer in my culinary journey! It gives me confidence in the kitchen and helps me practice new techniques.'
    },
    {
        profileImage: '/nigga.webp',
        userName: "Green Nigga",
        userRole: "Sous Chef",
        feedback: 'The AI-generated recipes are surprisingly innovative! They inspire me to experiment with new flavors and improve my plating techniques.'
    }
]);
</script>
