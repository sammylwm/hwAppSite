<script setup>
import Header from "./components/Header.vue";
</script>

<template>
  <div class="bg-white ">
    <Header/>
    <div class="p-10">
      <router-view></router-view>
    </div>
  </div>
</template>
