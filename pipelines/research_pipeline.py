# pipelines/research_pipeline.py

from pipelines.rag_pipeline import rag_query


def run_research(topic: str):
    """
    Main research execution function.
    """

    print("\n🔎 Researching topic:", topic)
    print("-" * 50)

    answer = rag_query(topic, top_k=5)

    print("\n📚 Research Summary:\n")
    print(answer)

    return answer
