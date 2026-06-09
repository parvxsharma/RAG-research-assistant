import { useCallback } from 'react'
import { useDropzone } from 'react-dropzone'
import { UploadCloud, FileText, CheckCircle2, Trash2, Loader2 } from 'lucide-react'

export default function UploadPanel({
  documents,
  uploading,
  onUpload,
  onClear,
  error,
}) {
  const onDrop = useCallback(
    (accepted) => {
      if (accepted.length > 0) onUpload(accepted[0])
    },
    [onUpload],
  )

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    multiple: false,
    accept: {
      'application/pdf': ['.pdf'],
      'text/plain': ['.txt'],
      'text/markdown': ['.md'],
    },
  })

  const totalChunks = documents.reduce((sum, d) => sum + (d.chunks || 0), 0)

  return (
    <aside className="flex h-full w-80 flex-col gap-4 border-r border-slate-200 bg-white p-5">
      <div>
        <h2 className="text-sm font-semibold text-slate-700">Knowledge Base</h2>
        <p className="mt-0.5 text-xs text-slate-400">
          Upload PDF, TXT, or MD files to search.
        </p>
      </div>

      <div
        {...getRootProps()}
        className={`flex cursor-pointer flex-col items-center justify-center gap-2 rounded-xl border-2 border-dashed px-4 py-8 text-center transition ${
          isDragActive
            ? 'border-blue-400 bg-blue-50'
            : 'border-slate-200 hover:border-blue-300 hover:bg-slate-50'
        }`}
      >
        <input {...getInputProps()} />
        {uploading ? (
          <Loader2 size={26} className="animate-spin text-blue-500" />
        ) : (
          <UploadCloud size={26} className="text-slate-400" />
        )}
        <span className="text-xs font-medium text-slate-500">
          {uploading
            ? 'Indexing…'
            : isDragActive
              ? 'Drop to upload'
              : 'Drag a file or click to browse'}
        </span>
      </div>

      {error && (
        <p className="rounded-lg bg-red-50 px-3 py-2 text-xs text-red-600">
          {error}
        </p>
      )}

      <div className="flex items-center justify-between text-xs text-slate-400">
        <span>
          {documents.length} doc{documents.length === 1 ? '' : 's'} · {totalChunks} chunks
        </span>
        {documents.length > 0 && (
          <button
            onClick={onClear}
            className="inline-flex items-center gap-1 text-red-400 transition hover:text-red-600"
          >
            <Trash2 size={13} /> Clear
          </button>
        )}
      </div>

      <div className="flex-1 space-y-2 overflow-y-auto">
        {documents.length === 0 ? (
          <p className="mt-4 text-center text-xs text-slate-300">
            No documents indexed yet.
          </p>
        ) : (
          documents.map((doc, i) => (
            <div
              key={`${doc.filename}-${i}`}
              className="flex items-center gap-2 rounded-lg border border-slate-100 bg-slate-50 px-3 py-2"
            >
              <FileText size={16} className="shrink-0 text-slate-400" />
              <span className="flex-1 truncate text-xs text-slate-600" title={doc.filename}>
                {doc.filename}
              </span>
              <CheckCircle2 size={15} className="shrink-0 text-emerald-500" />
            </div>
          ))
        )}
      </div>
    </aside>
  )
}
