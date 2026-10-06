from sentence_transformers import SentenceTransformer
from src.core import config

model = config.SENTENCE_TRANSFORMER_MODEL

def embed_documents(documents):
    texts = [document.page_content for document in documents]

    return model.encode(
        texts,
        convert_to_numpy=True
    ).tolist()


def embed_query(query: str):
    return model.encode(
        query,
        convert_to_numpy=True
    ).tolist()