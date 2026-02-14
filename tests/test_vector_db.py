import uuid
from tools.embeddings import embed_text
from tools.vector_db import create_index_if_not_exists, upsert_vectors


def test_vector_db():
    text = "This is a test vector."
    vector = embed_text(text)

    create_index_if_not_exists(len(vector))

    vector_data = [{
        "id": str(uuid.uuid4()),
        "values": vector,
        "metadata": {"text": text}
    }]

    upsert_vectors(vector_data)

    print("\nVector uploaded successfully.")


if __name__ == "__main__":
    test_vector_db()
