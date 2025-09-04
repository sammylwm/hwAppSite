<script setup>
import {ref} from 'vue'
import {postRequest} from '../api/api.vue'
import {useCookies} from "@vueuse/integrations/useCookies";

const cookies = useCookies()
const loading = ref(false)
const error = ref(null)
const result = ref(null)
const email = ref('')
const password = ref('')
const data = ref(null)
const emailError = ref('')
const passwordError = ref('')

async function userExists(emailValue, passwordValue) {
  loading.value = true
  error.value = null
  try {
    result.value = await postRequest('/user/', {email: emailValue, password: passwordValue})
    if (result.value === 2) {
      const datas = await postRequest('/user/web_get_datas/', {email: emailValue})
      cookies.set('email', datas[0], '7d')
      cookies.set('class', datas[1], '7d')
      cookies.set('login_dn', datas[2], '7d')
      cookies.set('password_dn', datas[3], '7d')
      emailError.value = null
      passwordError.value = null
    } else if (result.value === 1) {
      passwordError.value = "Не верный пароль"
      emailError.value = null
      data.value = null
    } else if (result.value === 0) {
      emailError.value = "Такого аккаунта нет"
      data.value = null
    }
  } catch (e) {
    error.value = e
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class=" flex items-center justify-center">
    <div class="bg-white rounded-2xl p-10 w-full max-w-sm
             shadow-xl hover:shadow-2xl
              border-2 border-green-400
      ">
      <h2 class="text-2xl font-bold text-center text-green-700 mb-6">
        Вход в аккаунт
      </h2>

      <div class="flex flex-col gap-4">
        <input
            v-model="email"
            type="email"
            placeholder="Email"
            class="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none
            focus:ring-2 focus:ring-green-400 transition"
        />
        <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>

        <input
            v-model="password"
            type="password"
            placeholder="Пароль"
            class="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none
            focus:ring-2 focus:ring-green-400 transition"
        />
        <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>

        <button
            @click="userExists(email, password)"
            :disabled="loading"
            class="bg-green-500 hover:bg-green-600 text-white font-semibold
             py-3 rounded-lg transition disabled:opacity-50
             disabled:cursor-not-allowed"
        >
          {{ loading ? 'Загрузка...' : 'Проверить' }}
        </button>
      </div>
      <router-link to="/register">
        <p class="text-center text-gray-400 mt-4 text-sm">
          Нет аккаунта? <a href="#" class="text-green-500 hover:underline">
          Регистрация</a>
        </p>
      </router-link>

    </div>
  </div>
</template>
