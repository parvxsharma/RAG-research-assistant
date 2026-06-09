"""RAG pipeline: retrieve relevant chunks from FAISS, then answer with the LLM.

Built with LangChain Expression Language (prompt | llm) rather than the
deprecated RetrievalQA chain, so it stays compatible with langchain 1.x.
The chat model is configured through environment variables.
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from . import config, ingest

_llm = None

SYSTEM_PROMPT = (
    "You are a precise research assistant. Answer the user's question using ONLY "
    "the context below, which was retrieved from their uploaded documents. "
    "If the context does not contain enough information to answer, say so plainly "
    "instead of guessing. Cite the bracketed source numbers (e.g. [1], [2]) you used.\n\n"
    "Context:\n{context}"
)

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{question}"),
    ]
)


def get_llm():
    global _llm
    if _llm is None:
        _llm = ChatGoogleGenerativeAI(
            model=config.CHAT_MODEL,
            google_api_key=config.GOOGLE_API_KEY,
            temperature=0,
        )
    return _llm


def _format_context(docs):
    return "\n\n".join(
        f"[{i + 1}] {doc.page_content}" for i, doc in enumerate(docs)
    )


def _format_sources(docs):
    sources = []
    for i, doc in enumerate(docs):
        page = doc.metadata.get("page")
        sources.append(
            {
                "index": i + 1,
                "filename": doc.metadata.get("source", "unknown"),
                # PyPDF pages are 0-indexed; show a human page number.
                "page": page + 1 if isinstance(page, int) else None,
                "excerpt": doc.page_content[:300].strip(),
            }
        )
    return sources


def answer_question(question):
    store = ingest.load_vectorstore()
    if store is None:
        return {
            "answer": "No documents have been indexed yet. Upload a document first.",
            "sources": [],
        }

    retriever = store.as_retriever(search_kwargs={"k": config.TOP_K_RESULTS})
    docs = retriever.invoke(question)

    chain = PROMPT | get_llm()
    response = chain.invoke(
        {"context": _format_context(docs), "question": question}
    )

    return {"answer": response.content, "sources": _format_sources(docs)}
