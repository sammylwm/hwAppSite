<template>
  <header class="px-2 py-5 flex items-center justify-between">
    <!-- Лого + название -->
    <div class="flex items-center gap-2 flex-shrink-0">
      <router-link to="/">
        <img src="/logo.webp" alt="Logo" class="w-8 md:w-16 rounded-4xl"/>
      </router-link>
      <h1 class="text-base md:text-2xl font-bold truncate">
        HWAPP
      </h1>
    </div>

    <!-- Иконки -->
    <ul class="flex items-center gap-2">
      <li>
        <a href="https://github.com/sammylwm" target="_blank"
           class="flex items-center gap-2 text-gray-500 hover:text-blue-600">
<!--          <img src="/github.svg" alt="GitHub" class="w-8"/>-->
        </a>
      </li>
      <li>
        <a href="https://t.me/sammylwm" target="_blank"
           class="flex items-center gap-2 text-gray-500 hover:text-blue-600">
<!--          <img src="/telegram.svg" alt="Telegram" class="w-8"/>-->
        </a>
      </li>
    </ul>
  </header>

</template>

<script setup lang="ts"></script>