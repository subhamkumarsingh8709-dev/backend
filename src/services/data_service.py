from langchain_community.document_loaders import DirectoryLoader, TextLoader #type: ignore

from src.core import config


def load_documents():
    loader = DirectoryLoader(
        str(config.DATA_DIR),
        glob="*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    documents = loader.load()
    for index, document in enumerate(documents):
        document.id = f"doc-{index + 1}"

    return documents