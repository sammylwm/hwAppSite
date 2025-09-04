<script setup lang="ts">

</script>

<template>
  <div class="fixed bottom-0 left-0 w-full bg-[#3b2a1a] flex justify-around py-2">
    <router-link
        to="/main"
        class="flex flex-col items-center text-[#e6d3b3]"
        :class="{ 'text-white font-bold': $route.name === 'main' }"
    >
      <span class="w-8 h-8 flex items-center justify-center rounded-full"
            :class="$route.name === 'homework' ? 'bg-[#a0794a]' : ''">
        📖
      </span>
      <span>Дз</span>
    </router-link>

    <router-link
        to="/grades"
        class="flex flex-col items-center text-[#e6d3b3]"
        :class="{ 'text-white font-bold': $route.name === 'grades' }"
    >
      ⭐
      <span>Оценки</span>
    </router-link>

    <router-link
        to="/allgrades"
        class="flex flex-col items-center text-[#e6d3b3]"
        :class="{ 'text-white font-bold': $route.name === 'allgrades' }"
    >
      ⭐
      <span>Всё</span>
    </router-link>
  </div>
</template>

<style scoped>

</style>