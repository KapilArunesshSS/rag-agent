from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_DIR = BASE_DIR / "data" / "documents"
VECTORSTORE_DIR = BASE_DIR / "data" / "vectorstore"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "Qwen/Qwen3-0.6B"

TOP_K = 4