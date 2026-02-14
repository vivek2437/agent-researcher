from tools.embeddings import embed_text


def test_embeddings():
    text = "Artificial Intelligence is transforming research."
    vector = embed_text(text)

    print("\nEmbedding dimension:", len(vector))


if __name__ == "__main__":
    test_embeddings()
