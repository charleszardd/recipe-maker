<template>
    <div class="main-font engagement-section">
        <v-row>
            <v-col>
                <v-card class="pa-5 bg-black rounded-lg">
                    <v-col>
                    <v-card-title class="text-center">
                        {{ engagement.title }}
                    </v-card-title>
                    <v-card-subtitle class="text-center">{{ engagement.subtitle }}</v-card-subtitle>

                    <div class="d-flex justify-center">
                    <Button height="40" elevation="5" class="bg-white mt-10 rounded-lg">Get Started Free</Button>
                </div>
                </v-col>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
<script setup>
import { ref } from "vue";

const engagement = ref({
    title: 'Ready to Transform Your Cooking?',
    subtitle: 'Join thousands of happy cooks using RecipeMaker every day.',
});
</script>
<style scoped>
.engagement-section{
    padding-top: 10rem;
    padding-bottom: 5rem;
}
</style>