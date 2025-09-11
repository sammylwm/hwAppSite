<script setup>
import { ref, onMounted } from 'vue'
import { postRequest } from '../api/api.vue'
import { useCookies } from "@vueuse/integrations/useCookies";
import { useRouter } from 'vue-router'

const router = useRouter()
const result = ref(null)
const loading = ref(true)
const cookies = useCookies()

onMounted(async () => {
  const allCookies = cookies.getAll()

  if ("email" in allCookies && "password" in allCookies) {
    console.log("email:", cookies.get("email"))
    console.log("password:", cookies.get("password"))

    result.value = await postRequest('/user/', {
      email: cookies.get("email"),
      password: cookies.get("password")
    })
    if (result.value === 2) {
      await router.push("/main/")
    } else {
      await router.push("/login/")
    }
  } else {
    await router.push("/login/")
  }
})
</script>

<template>
  <div v-if="loading" class="flex items-center justify-center h-screen">
    <div class="w-12 h-12 border-4 border-blue-500 border-dashed rounded-full animate-spin"></div>
  </div>
</template>
