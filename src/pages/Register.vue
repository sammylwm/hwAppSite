<script setup>
import {ref} from 'vue'
import {postRequest} from '../api/api.vue'
import {useCookies} from "@vueuse/integrations/useCookies";
import { useRouter } from 'vue-router'

const router = useRouter()
const cookies = useCookies()
const loading = ref(false)
const error = ref(null)
const result = ref(null)
const email = ref('')
const emailError = ref('')
const class_name = ref('')
const class_nameError = ref('')
const password = ref('')
const passwordError = ref('')
const login_dn = ref('')
const login_dnError = ref('')
const password_dn = ref('')
const password_dnError = ref('')

async function userCreate() {
  try {
    loading.value = true
    error.value = null
    if (!email.value || !password.value || !login_dn.value || !password_dn.value || !class_name.value) {
      emailError.value = !email.value ? "Это поле обязательно" : ""
      passwordError.value = !password.value ? "Это поле обязательно" : ""
      passwordError.value = !password.value ? "Это поле обязательно" : ""
      class_nameError.value = !class_name.value ? "Это поле обязательно" : ""
      password_dnError.value = !password_dn.value ? "Это поле обязательно" : ""
      login_dnError.value = !login_dn.value ? "Это поле обязательно" : ""
      return
    } else {
      emailError.value = null
      passwordError.value = null
      passwordError.value = null
      class_nameError.value = null
      password_dnError.value = null
      login_dnError.value = null
    }
    if (!email.value) {
      emailError.value = "Это поле обязательно"
    } else {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!emailRegex.test(email.value)) {
        emailError.value = "Введите корректный email"
        return
      } else {
        emailError.value = ""
      }
    }
    if (password.value.length < 6) {
      passwordError.value = "Пароль слишком простой"
      return
    }
    result.value = await postRequest("/mark/check/", {
      login: login_dn.value, password: password_dn.value
    })
    if (!(result.value === 1)) {
      login_dnError.value = "Не верный логин или пароль от дневника"
      password_dnError.value = "Не верный логин или пароль от дневника"
      return
    }


    try {
      result.value = await postRequest('/user/create/', {
        email: email.value, class_name: class_name.value,
        password: password.value, login_dn: login_dn.value, password_dn: password_dn.value
      })

      if (result.value) {
        const datas = await postRequest('/user/web_get_datas/', {email: email.value})
        cookies.set('email', datas[0], '7d')
        cookies.set('class', datas[1], '7d')
        cookies.set('login_dn', datas[2], '7d')
        cookies.set('password_dn', datas[3], '7d')
        error.value = null
        await router.push("/main/")
      } else {
        error.value = "Не удалось создать аккаунт."
      }
    } catch (e) {
      error.value = e
    }
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
        Регистрация аккаунта
      </h2>

      <div class="flex flex-col gap-4">
        <input
            v-model="email"
            type="email"
            placeholder="Email"
            class="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none
            focus:ring-2 focus:ring-green-400 transition"
        />
        <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
        <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>
        <select
            v-model="class_name"
            class="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none
         focus:ring-2 focus:ring-green-400 transition"
        >
          <option disabled value="">Выберите класс</option>
          <option>10А</option>
          <option>10Б</option>
          <option>10В</option>
          <option>11А</option>
          <option>11Б</option>
          <option>11В</option>
        </select>
        <p v-if="class_nameError" class="text-red-500 text-sm mt-1">{{ class_nameError }}</p>


        <input
            v-model="password"
            type="password"
            placeholder="Пароль"
            class="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none
            focus:ring-2 focus:ring-green-400 transition"
        />
        <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>

        <input
            v-model="login_dn"
            type="text"
            placeholder="Логин от дневника"
            class="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none
            focus:ring-2 focus:ring-green-400 transition"
        />
        <p v-if="login_dnError" class="text-red-500 text-sm mt-1">{{ login_dnError }}</p>

        <input
            v-model="password_dn"
            type="password"
            placeholder="Пароль от дневника"
            class="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none
            focus:ring-2 focus:ring-green-400 transition"
        />
        <p v-if="password_dnError" class="text-red-500 text-sm mt-1">{{ password_dnError }}</p>

        <button
            @click="userCreate(email, password)"
            :disabled="loading"
            class="bg-green-500 hover:bg-green-600 text-white font-semibold
             py-3 rounded-lg transition disabled:opacity-50
             disabled:cursor-not-allowed"
        >
          {{ loading ? 'Загрузка...' : 'Проверить' }}
        </button>
      </div>
      <router-link to="/">
        <p class="text-center text-gray-400 mt-4 text-sm">
          Есть аккаунт? <a href="#" class="text-green-500 hover:underline">
          Войти</a>
        </p>
      </router-link>

    </div>
  </div>
</template>