"""Document ingestion: load -> chunk -> embed -> store in FAISS.

This module owns the FAISS vector store lifecycle (load, add, list, clear).
The store is persisted to disk so the index survives restarts, and a small
JSON manifest tracks which documents have been indexed (for the UI list).
"""
import json
import shutil
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from . import config

_embeddings = None
_vectorstore = None

MANIFEST_PATH = config.VECTORSTORE_DIR / "manifest.json"
SUPPORTED_SUFFIXES = {".pdf", ".txt", ".md"}


def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = GoogleGenerativeAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            google_api_key=config.GOOGLE_API_KEY,
        )
    return _embeddings


def _load_manifest():
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return []


def _save_manifest(manifest):
    config.VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))


def load_vectorstore():
    """Return the in-memory store, loading it from disk on first use."""
    global _vectorstore
    if _vectorstore is not None:
        return _vectorstore
    if (config.VECTORSTORE_DIR / "index.faiss").exists():
        _vectorstore = FAISS.load_local(
            str(config.VECTORSTORE_DIR),
            get_embeddings(),
            allow_dangerous_deserialization=True,
        )
    return _vectorstore


def _load_file(path, filename):
    suffix = Path(filename).suffix.lower()
    if suffix == ".pdf":
        loader = PyPDFLoader(str(path))
    else:  # .txt / .md
        loader = TextLoader(str(path), encoding="utf-8")
    return loader.load()


def ingest_file(path, filename):
    """Index one file and persist the store. Returns the chunk count."""
    docs = _load_file(path, filename)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(docs)

    # Normalise the source to the display filename (loaders store a temp path).
    for chunk in chunks:
        chunk.metadata["source"] = filename

    global _vectorstore
    store = load_vectorstore()
    if store is None:
        _vectorstore = FAISS.from_documents(chunks, get_embeddings())
    else:
        store.add_documents(chunks)
        _vectorstore = store

    config.VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)
    _vectorstore.save_local(str(config.VECTORSTORE_DIR))

    manifest = _load_manifest()
    manifest.append({"filename": filename, "chunks": len(chunks)})
    _save_manifest(manifest)

    return len(chunks)


def list_documents():
    return _load_manifest()


def clear_index():
    """Drop the entire index and manifest from memory and disk."""
    global _vectorstore
    _vectorstore = None
    if config.VECTORSTORE_DIR.exists():
        shutil.rmtree(config.VECTORSTORE_DIR)
