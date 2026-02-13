# pipelines/rag_pipeline.py

from tools.embeddings import embed_text
from tools.vector_db import query_vector
from core.openrouter_client import chat_openrouter


def build_context(matches):
    """
    Convert Pinecone matches into readable context
    """
    context = ""

    for match in matches.get("matches", []):
        metadata = match.get("metadata", {})
        text = metadata.get("text", "")
        context += text + "\n\n"

    return context


def rag_query(user_query: str, top_k: int = 5):
    """
    Full RAG Flow:
    1. Embed user query
    2. Query Pinecone
    3. Build context
    4. Ask OpenRouter
    """

    # Step 1: Embed user query
    query_vector = embed_text(user_query)

    # Step 2: Retrieve similar chunks
    results = query_vector_from_db(query_vector, top_k)

    # Step 3: Build context
    context = build_context(results)

    # Step 4: Ask LLM with context
    messages = [
        {
            "role": "system",
            "content": "You are an AI research assistant. Answer using the provided context only."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {user_query}"
        }
    ]

    response = chat_openrouter(messages)

    return response["choices"][0]["message"]["content"]


def query_vector_from_db(vector, top_k):
    return query_vector(vector=vector, top_k=top_k)
