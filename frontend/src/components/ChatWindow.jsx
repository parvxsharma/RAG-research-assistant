import { useEffect, useRef, useState } from 'react'
import { Send, Loader2, MessagesSquare } from 'lucide-react'
import MessageBubble from './MessageBubble'

export default function ChatWindow({ messages, loading, onAsk, disabled }) {
  const [input, setInput] = useState('')
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  const submit = (e) => {
    e.preventDefault()
    const q = input.trim()
    if (!q || loading) return
    onAsk(q)
    setInput('')
  }

  return (
    <main className="flex h-full flex-1 flex-col bg-slate-50">
      <div className="flex-1 space-y-4 overflow-y-auto p-6">
        {messages.length === 0 ? (
          <div className="flex h-full flex-col items-center justify-center text-center text-slate-300">
            <MessagesSquare size={40} strokeWidth={1.5} />
            <p className="mt-3 text-sm font-medium text-slate-400">
              Ask a question about your documents
            </p>
            <p className="mt-1 text-xs text-slate-300">
              Upload a file on the left, then ask anything about it.
            </p>
          </div>
        ) : (
          messages.map((m, i) => <MessageBubble key={i} message={m} />)
        )}

        {loading && (
          <div className="flex justify-start gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded-full bg-slate-200 text-slate-500">
              <Loader2 size={16} className="animate-spin" />
            </div>
            <div className="rounded-2xl rounded-tl-sm bg-slate-100 px-4 py-2 text-sm text-slate-400">
              Searching documents…
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <form
        onSubmit={submit}
        className="border-t border-slate-200 bg-white p-4"
      >
        <div className="flex items-center gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={
              disabled ? 'Upload a document first…' : 'Ask a question…'
            }
            disabled={disabled || loading}
            className="flex-1 rounded-xl border border-slate-200 px-4 py-2.5 text-sm outline-none transition focus:border-blue-400 focus:ring-2 focus:ring-blue-100 disabled:bg-slate-50 disabled:text-slate-400"
          />
          <button
            type="submit"
            disabled={disabled || loading || !input.trim()}
            className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-600 text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-slate-200"
          >
            {loading ? (
              <Loader2 size={18} className="animate-spin" />
            ) : (
              <Send size={18} />
            )}
          </button>
        </div>
      </form>
    </main>
  )
}
