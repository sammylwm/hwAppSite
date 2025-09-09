<template>
  <div class="flex flex-col items-center w-full">
    <!-- Поп-ап -->
    <AddHwDialog
        :open="dialogOpen"
        @dismiss="dialogOpen = false"
    />

    <!-- Кнопка открыть -->
    <button v-if="ifAdmin" @click="dialogOpen = true" class="px-4 py-2 rounded-lg bg-blue-500 text-white">
      Добавить домашку
    </button>

    <!-- Дата -->
    <div class="my-4 flex flex-col items-center">
      <label class="text-slate-700 font-medium mb-1">Дата:</label>
      <input
          type="date"
          :value="dateForInput"
          @change="onDateChange($event)"
          class="border border-slate-300 rounded-lg px-3 py-2 text-center"
      />
    </div>

    <!-- Карточки уроков -->
    <div
        v-for="(lesson, index) in lessons"
        :key="index"
        class="relative flex flex-col my-4 bg-white shadow-sm border border-slate-200 rounded-lg w-full max-w-md"
    >
      <div class="flex justify-between items-center mx-3 mb-0 border-b border-slate-200 pt-3 pb-2 px-1">
        <span class="text-sm font-medium text-slate-600">{{ lesson.subject }}</span>
        <span class="text-sm font-medium text-slate-600">{{ lesson.time }}</span>
      </div>
      <div class="p-4">
        <p class="text-slate-600 leading-normal font-light">{{ lesson.homework }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {ref, onMounted, computed} from 'vue'
import {useCookies} from "@vueuse/integrations/useCookies"
import {postRequest} from '../api/api.vue'
import AddHwDialog from "../components/AddHwDialog.vue";

const time = [
  "08:10 - 08:55",
  "08:10 - 09:55",
  "10:05 - 10:45",
  "10:00 - 11:45",
  "11:55 - 12:40",
  "13:00 - 13:40",
  "14:00 - 14:40",
  "14:45 - 15:25"
]

const cookies = useCookies()
const lessons = ref<any[]>([])
const dialogOpen = ref(false)

const ifAdmin = ref(false)
// реактивная дата
const today = ref(new Date())

// формат для отображения "dd.MM.yyyy"
const displayDate = computed(() => {
  const day = String(today.value.getDate()).padStart(2, '0')
  const month = String(today.value.getMonth() + 1).padStart(2, '0')
  const year = today.value.getFullYear()
  return `${day}.${month}.${year}`
})

const dateForInput = computed(() => {
  const day = String(today.value.getDate()).padStart(2, '0')
  const month = String(today.value.getMonth() + 1).padStart(2, '0')
  const year = today.value.getFullYear()
  return `${year}-${month}-${day}`
})

async function fetchHomework() {
  const rawClass = cookies.get("class") || ""
  const className = rawClass.replace("А", "A").replace("Б", "B").replace("В", "V")
  ifAdmin.value = await postRequest("/class/check_admin/", {
    class_name: cookies.get("class"),
    email: cookies.get("email")
  })

  const response = await postRequest('/class/get_hw/', {
    date: displayDate.value,
    class_name: className
  })

  if (Array.isArray(response) && response.length === 3) {
    const [subjectsList, homeworksList, timesList] = response;

    lessons.value = subjectsList.map((subject: string, index: number) => {
      const homework = (homeworksList[index] || "Нет домашнего задания")
          .replace(/[\[\]']/g, '')    // на случай лишних скобок/кавычек
          .split(', ')
          .filter(Boolean)
          .join('\n');

      const time = timesList[index] || "—";

      return { subject, homework, time };
    });
  }
}

// при выборе новой даты
function onDateChange(event: Event) {
  const input = event.target as HTMLInputElement
  today.value = new Date(input.value)
  fetchHomework()
}


onMounted(() => {
  fetchHomework()
})
</script>
