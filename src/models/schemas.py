# Shapes of the data going in and out of the API.
from typing import Literal, Optional

from pydantic import BaseModel

class SuggestRequest(BaseModel):
    ticket: str
    category: Optional[str] = None  # optional filter, e.g. "shipping"

class Source(BaseModel):
    source: str
    type: str  # "ticket" or "faq"
    category: str
    text: str
    score: float                         # Qdrant similarity
    rerank_score: Optional[float] = None  # cross-encoder score

class SuggestResponse(BaseModel):
    reply: str
    sources: list[Source]

class IngestResponse(BaseModel):
    tickets_loaded: int
    faq_sections_loaded: int
    chunks_stored: int

class FeedbackRequest(BaseModel):
    ticket: str
    reply: str
    rating: Literal["up", "down"]
    edited_reply: Optional[str] = None

class FeedbackResponse(BaseModel):
    status: str