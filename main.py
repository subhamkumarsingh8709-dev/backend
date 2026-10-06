from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from src.services import data_service, chunking_service, embedding_service, vector_service, llm_service
from src.core import config

app = FastAPI(title="Support Copilot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

@app.post("/ticket")
def create_ticket(query: str):
    results = vector_service.search(query)

    context = "\n\n".join(
        result.payload.get("text", "")
        for result in results
        if result.payload
    )

    answer = llm_service.generate_response(
        query=query,
        context=context,
    )

    return {
        "query": query,
        "answer": answer,
    }