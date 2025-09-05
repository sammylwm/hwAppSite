<template>
  <div
      v-if="open"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-40 z-50"
  >
    <div class="bg-white rounded-2xl shadow-lg p-6 w-full max-w-md">
      <!-- Заголовок -->
      <h2 class="text-lg font-bold mb-4">Добавить дз</h2>

      <!-- Предмет -->
      <div class="mb-4">
        <label class="block text-sm font-medium mb-1">Предмет</label>
        <div class="relative">
          <button
              class="w-full border rounded-lg px-3 py-2 text-left flex justify-between items-center"
              @click="expanded = !expanded"
          >
            <span>{{ selectedSubject }}</span>
            <svg
                class="w-4 h-4 transform"
                :class="expanded ? 'rotate-180' : ''"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
            >
              <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
              />
            </svg>
          </button>
          <ul
              v-show="expanded"
              class="absolute z-10 mt-1 w-full bg-white border rounded-lg shadow max-h-60 overflow-y-auto"
          >
            <li
                v-for="subject in subjects"
                :key="subject"
                @click.stop="selectSubject(subject)"
                class="px-3 py-2 hover:bg-gray-100 cursor-pointer"
            >
              {{ subject }}
            </li>
          </ul>
        </div>
      </div>

      <!-- Домашнее задание -->
      <div class="mb-4">
        <label class="block text-sm font-medium mb-1">Домашнее задание</label>
        <textarea
            v-model="homeworkText"
            rows="3"
            class="w-full border rounded-lg px-3 py-2"
            placeholder="Введите задание"
        ></textarea>
      </div>

      <!-- Дата -->
      <div class="mb-4 relative">
        <label class="block text-sm font-medium mb-1">Дата</label>

        <!-- Календарь сразу -->
        <input
            type="date"
            class="w-full border rounded-lg px-3 py-2"
            @input="onDateChange"
        />

        <!-- Отображение выбранной даты -->
        <p class="mt-2 text-sm text-gray-600">Выбрано: {{ selectedDate }}</p>
      </div>


      <!-- Кнопки -->
      <div class="flex justify-end gap-2">
        <button
            class="px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300"
            @click="$emit('dismiss')"
        >
          Отмена
        </button>
        <button
            class="px-4 py-2 rounded-lg bg-blue-500 text-white hover:bg-blue-600"
            @click="submit()"
        >
          Отправить
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from "vue"
import {postRequest} from '../api/api.vue'
import {useCookies} from "@vueuse/integrations/useCookies";

const props = defineProps({
  open: Boolean,
})
const cookies = useCookies()
const emit = defineEmits(["dismiss", "date-click"])

const subjects = [
  "Алгебра",
  "Геометрия",
  "Русский язык",
  "Литература",
  "Обществознание",
  "История",
  "Физика",
  "Английский",
  "ИП",
  "Химия",
  "ДРЯ",
  "ЦСЯ/Литургика",
  "Биология",
  "История Церкви",
  "ОБЖ",
  "География",
  "Физкультура",
  "Информатика",
  "ОПВ",
]

const selectedSubject = ref(subjects[0])
const expanded = ref(false)
const homeworkText = ref("")
const result = ref("")

function formatDate(date) {
  const d = date.getDate().toString().padStart(2, "0")
  const m = (date.getMonth() + 1).toString().padStart(2, "0")
  const y = date.getFullYear()
  return `${d}.${m}.${y}`
}

const selectedDate = ref(formatDate(new Date()))
const showCalendar = ref(false)



function onDateChange(e) {
  const date = new Date(e.target.value)
  selectedDate.value = formatDate(date)
  showCalendar.value = false
}

function selectSubject(subject) {
  selectedSubject.value = subject
  expanded.value = false
}

async function submit() {
  if (!homeworkText.value || !selectedDate.value) {
    alert("Заполните все поля")
    return
  }

  try {
    result.value = await postRequest("/class/add_hw/", {
      subject: selectedSubject.value,
      hw: homeworkText.value,
      date: selectedDate.value,
      class_name: cookies.get("class")
    })
    if (result.value === 1) {
      alert("Домашка добавлена!")
    } else alert("Ошибка при добавлении домашки")
    emit("dismiss")
  } catch (e) {
    console.error(e)
  }
}
</script>
