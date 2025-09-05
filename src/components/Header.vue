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
        <button @click="exit()" class="inline-flex items-center gap-2">
          <LogOut class="w-5 h-5" />
          Выйти
        </button>
      </li>
    </ul>
  </header>

</template>

<script setup lang="ts">
import { LogOut, X } from "lucide-vue-next"
import {useRouter} from 'vue-router'

const router = useRouter()
async function exit() {
  const cookies = document.cookie.split(";");

  for (let cookie of cookies) {
    const eqPos = cookie.indexOf("=");
    const name = eqPos > -1 ? cookie.substring(0, eqPos) : cookie;

    document.cookie = name.trim() +
        "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
    document.cookie = name.trim() +
        "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain=" + window.location.hostname;
  }
  await router.push("/login")

}

</script>