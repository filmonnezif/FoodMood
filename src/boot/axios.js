import { boot } from 'quasar/wrappers'
import axios from 'axios'

const api = axios.create({ baseURL: 'https://newfastapifoodmood-6c31621f4c5f.herokuapp.com/' })
//const api = axios.create({ baseURL: 'http://localhost:8000/' })

export default boot(({ app }) => {
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = api
})

export { api }
