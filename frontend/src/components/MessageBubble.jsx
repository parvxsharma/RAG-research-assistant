import ReactMarkdown from 'react-markdown'
import { Bot, User } from 'lucide-react'
import SourceCard from './SourceCard'

export default function MessageBubble({ message }) {
  const isUser = message.role === 'user'

  if (isUser) {
    return (
      <div className="flex justify-end gap-2">
        <div className="max-w-[80%] rounded-2xl rounded-tr-sm bg-blue-600 px-4 py-2 text-sm text-white">
          {message.content}
        </div>
        <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-blue-100 text-blue-600">
          <User size={16} />
        </div>
      </div>
    )
  }

  return (
    <div className="flex justify-start gap-2">
      <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-200 text-slate-600">
        <Bot size={16} />
      </div>
      <div className="max-w-[80%]">
        <div className="rounded-2xl rounded-tl-sm bg-slate-100 px-4 py-2 text-sm text-slate-800">
          <div className="prose prose-sm max-w-none prose-p:my-1 prose-ul:my-1 prose-li:my-0">
            <ReactMarkdown>{message.content}</ReactMarkdown>
          </div>
        </div>
        <SourceCard sources={message.sources} />
      </div>
    </div>
  )
}
