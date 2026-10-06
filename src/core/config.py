import os 
from dotenv import load_dotenv
from pathlib import Path

from sentence_transformers import SentenceTransformer

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "openai/gpt-oss-120b"
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path("data")

SENTENCE_TRANSFORMER_MODEL = SentenceTransformer(
    "all-MiniLM-L6-v2"
)