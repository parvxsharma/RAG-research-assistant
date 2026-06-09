import { useState } from 'react'
import { ChevronDown, ChevronRight, FileText } from 'lucide-react'

export default function SourceCard({ sources }) {
  const [open, setOpen] = useState(false)

  if (!sources || sources.length === 0) return null

  return (
    <div className="mt-2 rounded-lg border border-slate-200 bg-white">
      <button
        onClick={() => setOpen((v) => !v)}
        className="flex w-full items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-500 transition hover:text-slate-700"
      >
        {open ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
        Sources ({sources.length})
      </button>

      {open && (
        <div className="space-y-2 px-3 pb-3">
          {sources.map((s) => (
            <div
              key={s.index}
              className="rounded-md bg-slate-50 p-2 text-xs text-slate-600"
            >
              <div className="mb-1 flex items-center gap-1.5 font-medium text-slate-700">
                <FileText size={12} className="text-slate-400" />
                [{s.index}] {s.filename}
                {s.page != null && (
                  <span className="text-slate-400">· p.{s.page}</span>
                )}
              </div>
              <p className="leading-relaxed text-slate-500">{s.excerpt}…</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
