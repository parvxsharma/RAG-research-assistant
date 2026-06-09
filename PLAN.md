# AI-Powered Research Assistant — Assignment Plan

**Deadline:** Wednesday, 10 June 2026  
**Time Left:** ~2 days  
**Use Case:** AI Research Assistant (Option D)  
**Stack:** OpenAI GPT-4o · LangChain · FAISS · FastAPI · Python · React · Vite · TailwindCSS

---

## What This Assignment Is Actually Asking

Act as an AI Solutions Consultant. Three deliverables:

1. **Research Report** — compare 3+ AI tools, justify choices
2. **Working Prototype** — RAG system that answers questions from documents
3. **Recommendation Report** — architecture, costs, risks, scaling

All packed into a GitHub repo + PDF report + demo video.

---

## Part 1 — AI Research & Evaluation

### Tools to Compare (pick these 5, write about 3 minimum)

| Tool | Role in This Project | Why Include It |
|---|---|---|
| **OpenAI GPT-4o** | LLM for answer generation | Gold standard, easy API |
| **LangChain** | Orchestration framework | Core of the RAG pipeline |
| **FAISS** | Vector database (local) | Free, no setup, bonus points |
| **Pinecone** | Vector database (cloud) | Compare vs FAISS — cost/scale |
| **Ollama** | Local LLM alternative | Shows you know cost optimization |

### Comparison Dimensions (required by assignment)
- Capabilities
- Pricing
- Scalability
- Ease of integration
- Limitations
- Best use cases

### Where to Get This Info
- OpenAI: platform.openai.com/docs/pricing
- LangChain: python.langchain.com
- FAISS: github.com/facebookresearch/faiss
- Pinecone: pinecone.io/pricing
- Ollama: ollama.com

---

## Part 2 — Prototype (Most Important Part)

### What We're Building

A FastAPI web app where:
1. User uploads PDF/text documents
2. Documents get chunked + embedded + stored in FAISS
3. User asks a question via API or simple UI
4. LangChain retrieves relevant chunks from FAISS
5. OpenAI GPT-4o generates an answer grounded in those chunks
6. Response returned with source references

### Architecture

```
User Query (HTTP POST /ask)
        ↓
    FastAPI
        ↓
   LangChain RAG Chain
        ↓              ↓
  FAISS Vector DB   OpenAI Embeddings
  (similarity search)   (text-embedding-3-small)
        ↓
  Retrieved Chunks
        ↓
  OpenAI GPT-4o
  (answer generation)
        ↓
  Final Answer + Sources
```

### File Structure

```
rag-research-assistant/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point + CORS
│   │   ├── rag_chain.py         # LangChain RAG pipeline
│   │   ├── ingest.py            # Document loading + FAISS indexing
│   │   └── config.py            # API keys, model names, settings
│   ├── data/
│   │   └── sample_docs/         # Sample PDFs/text files to demo
│   ├── vectorstore/             # FAISS index (auto-generated, gitignored)
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadPanel.jsx      # Drag-and-drop document uploader
│   │   │   ├── ChatWindow.jsx       # Q&A conversation thread
│   │   │   ├── MessageBubble.jsx    # Single message (user or AI)
│   │   │   ├── SourceCard.jsx       # Collapsible source reference
│   │   │   └── StatusBadge.jsx      # Indexing status indicator
│   │   ├── api/
│   │   │   └── client.js            # Axios calls to FastAPI
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css                # Tailwind directives
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── screenshots/
├── architecture.png
├── .gitignore
└── README.md
```

### Backend Modules

#### `ingest.py` — Load and index documents
```
- Load PDFs using PyPDFLoader / DirectoryLoader
- Split with RecursiveCharacterTextSplitter (chunk_size=1000, overlap=200)
- Embed with OpenAIEmbeddings (text-embedding-3-small)
- Save to FAISS vectorstore
```

#### `rag_chain.py` — The RAG pipeline
```
- Load FAISS vectorstore
- Create retriever (top-k=4 similar chunks)
- Build RetrievalQA chain with GPT-4o
- Return answer + source documents
```

#### `main.py` — FastAPI app
```
POST /ingest       — upload and index a document (multipart/form-data)
POST /ask          — ask a question, get answer + sources
GET  /documents    — list indexed documents
DELETE /documents  — clear the index
GET  /health       — health check

CORS enabled for http://localhost:5173 (Vite dev server)
```

---

### Frontend Components

#### Layout — Two-panel design
```
┌─────────────────────────────────────────────────────┐
│  AI Research Assistant                    [status]   │
├──────────────────┬──────────────────────────────────┤
│                  │                                   │
│  UPLOAD PANEL    │      CHAT WINDOW                  │
│                  │                                   │
│  Drag & drop     │  [User]: What is RAG?             │
│  or click to     │                                   │
│  upload PDF/TXT  │  [AI]: RAG stands for...          │
│                  │       ┌──────────────────┐        │
│  Indexed docs:   │       │ Sources (2)    ▼ │        │
│  • doc1.pdf ✓    │       │ doc1.pdf, p.3    │        │
│  • doc2.txt ✓    │       └──────────────────┘        │
│                  │                                   │
│  [Clear Index]   │  ┌─────────────────────────────┐  │
│                  │  │ Ask a question...      [Ask] │  │
└──────────────────┴──┴─────────────────────────────┴─┘
```

#### `UploadPanel.jsx`
```
- Drag-and-drop zone (react-dropzone)
- Shows list of indexed documents with green checkmarks
- Upload progress indicator
- Clear index button
- Handles PDF and .txt files
```

#### `ChatWindow.jsx`
```
- Scrollable message thread
- Loading spinner while waiting for answer
- Auto-scroll to latest message
- Empty state: "Upload a document and ask a question"
```

#### `MessageBubble.jsx`
```
- User messages: right-aligned, blue
- AI messages: left-aligned, gray, with avatar
- Markdown rendering for AI answers (react-markdown)
- Collapsible SourceCard below each AI message
```

#### `SourceCard.jsx`
```
- Shows: filename, page number, excerpt snippet
- Collapsible (hidden by default, click to expand)
- One card per retrieved chunk
```

#### `api/client.js`
```
- axios instance pointed at http://localhost:8000
- uploadDocument(file) → POST /ingest
- askQuestion(query) → POST /ask
- listDocuments() → GET /documents
- clearIndex() → DELETE /documents
```

### Sample Documents to Include (for demo)
Use free, publicly available documents:
- A few pages from Wikipedia (AI, RAG, LangChain topics) saved as .txt
- A sample research paper PDF (arXiv)
- A company FAQ text file (make one up)

This lets you demo the system answering real questions.

---

## Part 3 — Recommendation Report

### Report Structure (write as PDF or DOCX)

#### 1. Problem Statement
> Researchers and knowledge workers spend excessive time manually searching through documents to find relevant information. An AI-powered RAG system reduces this to seconds by semantically searching documents and generating grounded answers.

#### 2. Recommended Architecture
- Diagram (same as above, polished in draw.io or Excalidraw)
- Describe each component and why it was chosen

#### 3. Tool Selection Justification
- OpenAI: best generation quality, reliable API, extensive docs
- LangChain: reduces boilerplate for RAG chains, active ecosystem
- FAISS: zero cost, runs locally, sufficient for prototype; Pinecone for production
- FastAPI: async Python, automatic docs, lightweight

#### 4. Estimated Infrastructure Cost

| Service | Usage | Monthly Cost |
|---|---|---|
| OpenAI GPT-4o | ~100 queries/day @ ~1K tokens | ~$15–25 |
| OpenAI Embeddings | text-embedding-3-small, one-time ingest | ~$0.50 |
| FAISS | Local, self-hosted | $0 |
| FastAPI (Render/Railway free tier) | Hosting | $0 |
| **Total** | | **~$15–25/month** |

#### 5. Risks & Limitations
- **Hallucination:** GPT-4o may fabricate when context is insufficient — mitigate with strict prompts + source citation
- **Context window limits:** Very large documents need smart chunking
- **API cost at scale:** Token costs grow linearly with usage
- **Data privacy:** Sending documents to OpenAI API — use Azure OpenAI or local Ollama for sensitive data
- **FAISS limitations:** No persistence by default, not distributed — use Pinecone/Weaviate in production

#### 6. Production Scaling Strategy
```
Load Balancer (nginx)
        ↓
Multiple FastAPI instances (Docker + Kubernetes)
        ↓
Pinecone (managed vector DB, horizontally scalable)
        ↓
OpenAI API (auto-scales)
```

---

## Deliverables Checklist

### GitHub Repository
- [ ] All code committed, clean history
- [ ] `.env.example` with variable names (never commit real `.env`)
- [ ] `requirements.txt` with pinned versions
- [ ] `README.md` with setup instructions + demo GIF/screenshot
- [ ] `architecture.png` in repo root
- [ ] `screenshots/` folder with at least 3 screenshots

### README.md Must Include
- Project title + one-line description
- Architecture diagram
- Setup instructions (pip install, set env vars, run)
- Example query + output
- Tool comparison table
- Cost estimate

### Report (PDF)
- [ ] Problem statement
- [ ] Tool comparison table (3+ tools)
- [ ] Architecture diagram with explanation
- [ ] Why these tools
- [ ] Cost analysis table
- [ ] Risks section
- [ ] Scaling strategy
- [ ] Future improvements

### Demo Video (2–5 min)
Script:
1. Show the GitHub repo structure (30s)
2. Run `uvicorn app.main:app` — show it starts (20s)
3. POST /ingest — upload a sample doc (30s)
4. POST /ask — ask 2–3 questions, show answers with sources (2–3 min)
5. Briefly explain the RAG flow while showing output (1 min)

Use Loom (free) or OBS to record.

### Screenshots Needed
1. FastAPI running (`/docs` Swagger UI)
2. Ingest endpoint — document uploaded successfully
3. Ask endpoint — question + answer + sources in JSON
4. Terminal showing the app running
5. Architecture diagram (high quality)

---

## Build Order (Day-by-Day)

### Day 1 (Today, June 8) — Build Everything

**Backend (2–3 hrs)**
- [ ] Create project structure (`backend/` + `frontend/`)
- [ ] `pip install langchain langchain-openai faiss-cpu fastapi uvicorn python-dotenv pypdf python-multipart`
- [ ] Write `config.py` — load env vars
- [ ] Write `ingest.py` — load docs, chunk, embed, save FAISS
- [ ] Write `rag_chain.py` — retriever + GPT-4o chain
- [ ] Write `main.py` — all endpoints + CORS for localhost:5173
- [ ] Test backend with curl/Postman

**Frontend (2–3 hrs)**
- [ ] `npm create vite@latest frontend -- --template react`
- [ ] Install deps: tailwind, axios, react-dropzone, react-markdown, lucide-react
- [ ] Write `api/client.js`
- [ ] Build `UploadPanel.jsx` — drag-drop + indexed docs list
- [ ] Build `ChatWindow.jsx` + `MessageBubble.jsx` + `SourceCard.jsx`
- [ ] Wire up `App.jsx` with two-panel layout
- [ ] Test full flow: upload → ask → see answer with sources

**Evening — Polish**
- [ ] Error states (no docs indexed, API down)
- [ ] Loading spinners, disable Ask button while loading
- [ ] Prepare 2–3 sample docs for demo
- [ ] Take screenshots

### Day 2 (June 9) — Report + Demo + Submit

**Morning — Report (2–3 hrs)**
- [ ] Write full recommendation report using structure above
- [ ] Create architecture diagram (draw.io / Excalidraw) → export as PNG
- [ ] Real pricing data from each tool's website
- [ ] Export as PDF

**Afternoon — Demo Video + Final Polish (2 hrs)**
- [ ] Record 2–5 min demo with Loom
  - Show repo structure
  - Run backend + frontend
  - Upload a doc
  - Ask 3 questions, show sources
  - Briefly explain the RAG flow
- [ ] Add architecture.png to repo root
- [ ] Final README with setup instructions + screenshot
- [ ] Push to GitHub

**Evening — Buffer**
- [ ] Recheck deliverables checklist
- [ ] Submit

---

## Bonus Points Strategy

The assignment explicitly awards bonus points for:

| Bonus | How We Get It |
|---|---|
| RAG systems | Core feature — FAISS + LangChain retrieval |
| Real API integrations | OpenAI API with real key |
| Cost optimization analysis | FAISS (free) vs Pinecone (paid) comparison in report |
| Production deployment thinking | Scaling section in report |
| AI agents | Optional: add a simple LangChain agent that can choose between "search documents" and "general knowledge" as tools |

The agent bonus is easy to add — LangChain's `create_react_agent` with two tools takes ~20 lines.

---

## Tech Stack Summary

```
Backend
  Language:     Python 3.11+
  API:          FastAPI + Uvicorn
  LLM:          OpenAI GPT-4o (gpt-4o)
  Embeddings:   OpenAI text-embedding-3-small
  Vector DB:    FAISS (local, free)
  RAG:          LangChain RetrievalQA
  Env:          python-dotenv
  Doc Loading:  LangChain PyPDFLoader, TextLoader

Frontend
  Framework:    React 18 + Vite
  Styling:      TailwindCSS
  HTTP:         Axios
  Markdown:     react-markdown
  File Upload:  react-dropzone
  Icons:        lucide-react
```

## Frontend Dependencies

```json
{
  "dependencies": {
    "axios": "^1.7.0",
    "react": "^18.3.0",
    "react-dom": "^18.3.0",
    "react-dropzone": "^14.2.0",
    "react-markdown": "^9.0.0",
    "lucide-react": "^0.400.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.0",
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.0",
    "tailwindcss": "^3.4.0",
    "vite": "^5.3.0"
  }
}
```

## Key Environment Variables

```bash
OPENAI_API_KEY=sk-...
EMBEDDING_MODEL=text-embedding-3-small
CHAT_MODEL=gpt-4o
FAISS_INDEX_PATH=./vectorstore/index
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_RESULTS=4
```
