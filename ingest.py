from src.services import data_service
from src.services import chunking_service
from src.services import embedding_service
from src.services import vector_service


def ingest():
    documents = data_service.load_documents()
    print("Documents:", len(documents))
    chunks = chunking_service.chunk_documents(documents)
    print("Chunks:", len(chunks))
    vectors = embedding_service.embed_documents(chunks)
    print("Vectors:", len(vectors))
    print("Vector dimension:", len(vectors[0]))
    vector_service.recreate_collection()
    vector_service.store_chunks(
        chunks,
        vectors,
    )
    print("Ingestion completed.")


if __name__ == "__main__":
    ingest()