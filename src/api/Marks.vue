<script setup lang="ts">
import { ref, onMounted } from 'vue'
import {postRequest} from "src/api/api.vue"
import { useCookies } from "@vueuse/integrations/useCookies"
interface GradeEntry {
  date: string
  subject: string
  grade: string
}

const grades = ref<GradeEntry[]>([])
const isLoaded = ref(false)
const cookies = useCookies()

async function fetchMarks(login: string, password: string) {
  const response = await postRequest('/class/get_marks/', { login, password })
  if (Array.isArray(response)) {
    const cleanedMarks = response.map((item: any[]) => ({
      date: item[0],
      subject: item[1],
      grade: String(item[2])
    }))

    cookies.set('userMarks', JSON.stringify(cleanedMarks), { path: '/', maxAge: 60*60*24*30 }) // месяц

    grades.value = cleanedMarks
    isLoaded.value = true
  }
}
</script>
