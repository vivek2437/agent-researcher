from pipelines.rag_pipeline import rag_query


def test_rag():
    question = "What is machine learning?"
    answer = rag_query(question)

    print("\nRAG Answer:\n")
    print(answer)


if __name__ == "__main__":
    test_rag()
