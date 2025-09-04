<script>
// services/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'https://lednevs.ru/hw_api',
})

export async function postRequest(url, payload) {
  try {
    const response = await api.post(url, payload)
    return response.data
  } catch (error) {
    throw error
  }
}

export default api

</script>