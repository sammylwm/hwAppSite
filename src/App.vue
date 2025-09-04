<template>
  <div class="bg-white min-h-screen flex flex-col">
    <Header />

    <!-- Контент с отступом снизу под Bottom -->
    <div class="flex-1 p-10 pb-20">
      <router-view></router-view>
    </div>

    <Bottom v-if="['grades', 'allgrades', 'main'].includes(route.path.replace(/^\/|\/$/g, ''))"/>
  </div>
</template>

<script setup>
import Header from "./components/Header.vue";
import Bottom from "./components/Bottom.vue";
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
