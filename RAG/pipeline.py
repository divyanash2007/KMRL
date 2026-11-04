
from llm_provider import get_llm
from prompt import rag_prompt
from retriever import get_retriever


def format_documents(documents):
    """
    Convert retrieved LangChain documents into
    context that Gemini can understand.
    """

    formatted_chunks = []

    for index, document in enumerate(documents, start=1):

        metadata = document.metadata

        file_name = metadata.get("file_name", "Unknown document")
        page_number = metadata.get("page_number", "Unknown page")

        chunk = f"""
                Source {index}
                Document: {file_name}
                Page: {page_number}

                Content:
                {document.page_content}
            """

        formatted_chunks.append(chunk)

    return "\n\n".join(formatted_chunks)


def ask_rag(question: str):

    # 1. Retrieve relevant document chunks
    retriever = get_retriever()
    documents = retriever.invoke(question)

    if not documents:
        return {
            "answer": (
                "I could not find relevant information "
                "in the available documents."
            ),
            "sources": [],
        }

    # 2. Format retrieved documents
    context = format_documents(documents)

    # 3. Initialize Gemini
    llm = get_llm()

    # 4. Create prompt
    messages = rag_prompt.format_messages(
        question=question,
        context=context,
    )

    # 5. Generate answer
    response = llm.invoke(messages)

    # 6. Extract source information
    sources = []

    for document in documents:

        source = {
            "file_name": document.metadata.get("title"),
            "page_number": document.metadata.get("page"),
        }

        if source not in sources:
            sources.append(source)

    return {
        "answer": response.content,
        "sources": sources,
    }
