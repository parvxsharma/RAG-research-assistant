import { useEffect, useState } from 'react'
import { BrainCircuit } from 'lucide-react'
import UploadPanel from './components/UploadPanel'
import ChatWindow from './components/ChatWindow'
import StatusBadge from './components/StatusBadge'
import {
  uploadDocument,
  askQuestion,
  listDocuments,
  clearIndex,
  getHealth,
} from './api/client'

export default function App() {
  const [documents, setDocuments] = useState([])
  const [messages, setMessages] = useState([])
  const [uploading, setUploading] = useState(false)
  const [asking, setAsking] = useState(false)
  const [uploadError, setUploadError] = useState('')
  const [health, setHealth] = useState({ state: 'checking', model: '' })

  useEffect(() => {
    getHealth()
      .then((h) => setHealth({ state: 'ok', model: h.chat_model }))
      .catch(() => setHealth({ state: 'down', model: '' }))
    listDocuments().then(setDocuments).catch(() => {})
  }, [])

  const handleUpload = async (file) => {
    setUploading(true)
    setUploadError('')
    try {
      await uploadDocument(file)
      setDocuments(await listDocuments())
    } catch (e) {
      setUploadError(
        e.response?.data?.detail || 'Upload failed. Is the backend running?',
      )
    } finally {
      setUploading(false)
    }
  }

  const handleClear = async () => {
    try {
      await clearIndex()
      setDocuments([])
      setMessages([])
    } catch (e) {
      setUploadError('Failed to clear index.')
    }
  }

  const handleAsk = async (question) => {
    setMessages((m) => [...m, { role: 'user', content: question }])
    setAsking(true)
    try {
      const res = await askQuestion(question)
      setMessages((m) => [
        ...m,
        { role: 'assistant', content: res.answer, sources: res.sources },
      ])
    } catch (e) {
      const detail =
        e.response?.data?.detail || 'Request failed. Is the backend running?'
      setMessages((m) => [
        ...m,
        { role: 'assistant', content: `⚠️ ${detail}`, sources: [] },
      ])
    } finally {
      setAsking(false)
    }
  }

  return (
    <div className="flex h-full flex-col">
      <header className="flex items-center justify-between border-b border-slate-200 bg-white px-6 py-3">
        <div className="flex items-center gap-2.5">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-blue-600 text-white">
            <BrainCircuit size={20} />
          </div>
          <div>
            <h1 className="text-sm font-semibold text-slate-800">
              AI Research Assistant
            </h1>
            <p className="text-xs text-slate-400">
              RAG · LangChain · Gemini · FAISS
            </p>
          </div>
        </div>
        <StatusBadge state={health.state} model={health.model} />
      </header>

      <div className="flex flex-1 overflow-hidden">
        <UploadPanel
          documents={documents}
          uploading={uploading}
          onUpload={handleUpload}
          onClear={handleClear}
          error={uploadError}
        />
        <ChatWindow
          messages={messages}
          loading={asking}
          onAsk={handleAsk}
          disabled={documents.length === 0}
        />
      </div>
    </div>
  )
}
