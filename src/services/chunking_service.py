from langchain_text_splitters import RecursiveCharacterTextSplitter #type: ignore


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documents)

    for index, chunk in enumerate(chunks):
        chunk.id = f"chunk-{index + 1}"

    return chunks