import { CheckCircle2, XCircle, Loader2 } from 'lucide-react'

// state: 'ok' | 'down' | 'checking'
export default function StatusBadge({ state, model }) {
  if (state === 'checking') {
    return (
      <span className="inline-flex items-center gap-1.5 rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-500">
        <Loader2 size={14} className="animate-spin" />
        Connecting…
      </span>
    )
  }
  if (state === 'down') {
    return (
      <span className="inline-flex items-center gap-1.5 rounded-full bg-red-50 px-3 py-1 text-xs font-medium text-red-600">
        <XCircle size={14} />
        API offline
      </span>
    )
  }
  return (
    <span className="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-3 py-1 text-xs font-medium text-emerald-600">
      <CheckCircle2 size={14} />
      Online{model ? ` · ${model}` : ''}
    </span>
  )
}
