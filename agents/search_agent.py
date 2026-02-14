from pipelines.rag_pipeline import rag_query


def search_topic(topic: str):
    """
    Retrieves relevant information using RAG.
    """

    return rag_query(topic)
