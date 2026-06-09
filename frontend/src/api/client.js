import axios from 'axios'

const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:9000'

const api = axios.create({ baseURL })

export async function uploadDocument(file) {
  const form = new FormData()
  form.append('file', file)
  const { data } = await api.post('/ingest', form, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return data
}

export async function askQuestion(question) {
  const { data } = await api.post('/ask', { question })
  return data
}

export async function listDocuments() {
  const { data } = await api.get('/documents')
  return data.documents
}

export async function clearIndex() {
  const { data } = await api.delete('/documents')
  return data
}

export async function getHealth() {
  const { data } = await api.get('/health')
  return data
}
