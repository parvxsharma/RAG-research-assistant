"""FastAPI entry point for the AI Research Assistant RAG service."""
import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from . import config, ingest, rag_chain

app = FastAPI(title="AI Research Assistant", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "chat_model": config.CHAT_MODEL,
        "embedding_model": config.EMBEDDING_MODEL,
        "api_key_configured": bool(config.GOOGLE_API_KEY),
    }


@app.post("/ingest")
async def ingest_endpoint(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix.lower()
    if suffix not in ingest.SUPPORTED_SUFFIXES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{suffix}'. Use PDF, TXT, or MD.",
        )

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        chunks = ingest.ingest_file(tmp_path, file.filename)
    except Exception as exc:  # surface model / parsing errors to the UI
        raise HTTPException(status_code=500, detail=str(exc))
    finally:
        os.unlink(tmp_path)

    return {"filename": file.filename, "chunks_indexed": chunks}


@app.post("/ask")
def ask_endpoint(req: AskRequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    try:
        return rag_chain.answer_question(req.question)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/documents")
def documents_endpoint():
    return {"documents": ingest.list_documents()}


@app.delete("/documents")
def clear_endpoint():
    ingest.clear_index()
    return {"status": "cleared"}
