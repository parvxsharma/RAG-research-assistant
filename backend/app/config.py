"""Central configuration. All values come from environment / .env."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "models/gemini-embedding-001")
CHAT_MODEL = os.getenv("CHAT_MODEL", "models/gemini-2.5-flash")

# Folder that holds the FAISS index files and the document manifest.
VECTORSTORE_DIR = Path(os.getenv("VECTORSTORE_DIR", "./vectorstore"))

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))
TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", "4"))

# Frontend origins allowed to call this API (Vite dev server).
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
