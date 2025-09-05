<template>
  <div class="flex flex-col items-center w-full p-4">
    <div v-if="loading" class="text-slate-500 text-sm mb-4">Загрузка оценок...</div>

    <div
        v-for="lesson in grades"
        :key="lesson.date + lesson.subject"
        class="relative flex flex-col my-4 bg-white shadow-md border border-slate-200 rounded-lg w-full max-w-md hover:shadow-lg transition-shadow duration-200"
    >
      <div class="flex justify-between items-center mx-3 mb-0 border-b border-slate-200 pt-3 pb-2 px-1">
        <div class="flex flex-col">
          <span class="text-sm font-medium text-slate-600">{{ lesson.subject }}</span>
          <span class="text-xs text-slate-400">{{ lesson.date }}</span>
        </div>
        <span class="text-sm font-medium text-slate-600">{{ lesson.grade }}</span>
      </div>

    </div>

    <!-- Сообщение если оценок нет -->
    <div v-if="!loading && grades.length === 0" class="text-slate-400 text-sm mt-4">
      Оценки пока отсутствуют
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useCookies } from "@vueuse/integrations/useCookies"
import { postRequest } from '../api/api.vue'

interface GradeEntry {
  date: string
  subject: string
  grade: string
}

type ApiGradeResponse = [string, string, string];

const cookies = useCookies()
const grades = ref<GradeEntry[]>([])
const loading = ref(false);

async function fetchGrades() {
  loading.value = true;
  try {
    const response = await postRequest('/mark/', {
      login: cookies.get("login_dn"),
      password: cookies.get("password_dn")
    });

    if (Array.isArray(response)) {
      grades.value = response.map((item: ApiGradeResponse) => ({
        date: item[0],
        subject: item[1],
        grade: item[2],
      }));
    }
  } catch (err) {
    console.error('Failed to fetch grades', err);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchGrades()
})
</script>
