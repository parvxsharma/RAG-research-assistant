# AI-Powered Research Assistant (RAG + LangChain)

A document question-answering assistant. Upload PDFs / text files, ask questions in
natural language, and get answers grounded in your documents with cited sources —
powered by **Retrieval-Augmented Generation (RAG)**.

> Built for the "AI-powered business workflow automation" assignment — Use Case D:
> AI Research Assistant.

---

## What it does

1. You upload a document (PDF / TXT / MD).
2. It is split into chunks, embedded with Gemini, and stored in a **FAISS** vector index.
3. You ask a question.
4. **LangChain** retrieves the most relevant chunks and **Gemini** writes an answer
   using only those chunks — with expandable source references.

## Architecture

```
            React + Vite UI  (upload + chat)
                    │  HTTP (axios)
                    ▼
              FastAPI backend
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
  LangChain RAG          Gemini Embeddings
  (retrieve top-k)       (gemini-embedding-001)
        │                       │
        ▼                       ▼
   FAISS vector DB  ◄───────────┘   (local, free)
        │
        ▼
   Gemini → grounded answer + sources
```

## Tech stack

| Layer        | Tools                                                        |
|--------------|-------------------------------------------------------------|
| Frontend     | React 18, Vite, TailwindCSS, axios, react-dropzone, react-markdown |
| Backend      | FastAPI, Uvicorn                                            |
| RAG / LLM    | LangChain, Gemini 2.5 Flash, gemini-embedding-001           |
| Vector store | FAISS (local)                                              |

---

## Setup

### 1. Backend

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
cp backend/.env.example backend/.env   # then paste your Google AI key into backend/.env
python -m uvicorn app.main:app --app-dir backend --reload --port 9000
```

API docs: http://localhost:9000/docs

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:5173

Or start both servers together after installing dependencies:

```bash
./start.sh
```

---

## API

| Method | Endpoint      | Purpose                              |
|--------|---------------|--------------------------------------|
| GET    | `/health`     | Status + configured model            |
| POST   | `/ingest`     | Upload & index a document (multipart)|
| POST   | `/ask`        | `{ "question": "..." }` → answer + sources |
| GET    | `/documents`  | List indexed documents               |
| DELETE | `/documents`  | Clear the index                      |

Example:

```bash
curl -F "file=@backend/data/sample_docs/rag_overview.txt" http://localhost:9000/ingest
curl -X POST http://localhost:9000/ask \
     -H "Content-Type: application/json" \
     -d '{"question":"What is RAG and why does it matter?"}'
```

## Sample documents

`backend/data/sample_docs/` contains two ready-to-index files
(`rag_overview.txt`, `tooling_notes.txt`) so you can demo immediately.

## Cost (rough)

| Service                   | Monthly (light use) |
|---------------------------|---------------------|
| Gemini API (~100 q/day)   | Low usage-based cost |
| Gemini embeddings         | Low one-time ingest cost |
| FAISS + FastAPI (local)   | $0                  |

## Notes / limitations

- Requires a valid `GOOGLE_API_KEY` for `/ingest` and `/ask`.
- FAISS index is local and persisted to `backend/vectorstore/`.
- For production, swap FAISS for a managed vector DB (Pinecone/Weaviate) and run
  multiple backend instances behind a load balancer.
