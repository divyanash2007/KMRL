from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    vector_store = Chroma(
        collection_name="cvc_documents",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_store


def get_retriever():
    vector_store = get_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5},
    )

    return retriever