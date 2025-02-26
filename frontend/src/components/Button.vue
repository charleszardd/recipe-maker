<template>
    <v-btn color="#212121" class=" normal-text" v-bind="$attrs" @click="emit('click')">
      <v-icon v-if="icon" :class="iconClass">{{ icon }}</v-icon>
      <slot></slot>
    </v-btn>
  </template>
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    icon: String, 
    noSpacing: {
        type: Boolean,
        default: true
    } 
  })
  
  const emit = defineEmits(['click'])
  
  const iconClass = computed(() => (props.noSpacing ? '' : 'mr-2'))
  </script>