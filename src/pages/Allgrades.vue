<template>
  <div class="flex flex-col items-center w-full p-4">
    <!-- Состояние загрузки -->
    <div v-if="loading" class="text-slate-500 text-sm mb-4">Загрузка оценок...</div>

    <!-- Карточки предметов -->
    <div
        v-for="(subject, index) in subjects"
        :key="subject"
        class="relative flex flex-col my-4 bg-white shadow-md border border-slate-200 rounded-lg w-full max-w-md transition-shadow duration-200 hover:shadow-lg"
    >
      <!-- Верхняя часть карточки: предмет и итоговая оценка -->
      <div
          class="flex justify-between items-center mx-3 mb-0 border-b border-slate-200 pt-3 pb-2 px-1 cursor-pointer"
          @click="expandedIndex === index ? expandedIndex = null : expandedIndex = index"
      >
        <span class="text-sm font-medium text-slate-600">{{ subject }}</span>
        <span class="text-sm font-medium text-slate-600">{{ grades[index] || '-' }}</span>
      </div>

      <!-- Разворачиваемая часть: список оценок -->
      <div v-if="expandedIndex === index" class="p-4 border-t border-slate-200">
        <p v-if="marks[index]?.length" class="text-slate-600 leading-normal font-light">
          <span v-for="(mark, mIndex) in marks[index]" :key="mIndex">
            {{ mark }}<span v-if="mIndex < marks[index].length - 1">, </span>
          </span>
        </p>
        <p v-else class="text-slate-400 text-sm">Оценки отсутствуют</p>
      </div>
    </div>

    <!-- Сообщение если нет предметов -->
    <div v-if="!loading && subjects.length === 0" class="text-slate-400 text-sm mt-4">
      Предметы пока отсутствуют
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useCookies } from "@vueuse/integrations/useCookies"
import { postRequest } from '../api/api.vue'

const cookies = useCookies()
const loading = ref(false)
const expandedIndex = ref<number | null>(null) // индекс развернутой карточки

// Структура UI
const subjects = ref<string[]>([])
const grades = ref<string[]>([])
const marks = ref<string[][]>([])

// Получение данных
async function fetchGrades() {
  loading.value = true
  try {
    const response = await postRequest('/mark/all/', {
      login: cookies.get("login_dn"),
      password: cookies.get("password_dn")
    })

    if (Array.isArray(response)) {
      subjects.value = response.map((item: any[]) => item[0]) // название предмета
      grades.value = response.map((item: any[]) => item[1])   // итоговая оценка
      marks.value = response.map((item: any[]) => item[2] || []) // список оценок
    }
  } catch (err) {
    console.error('Failed to fetch grades', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchGrades()
})
</script>
