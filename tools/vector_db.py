from pinecone import Pinecone, ServerlessSpec
from core.config import PINECONE_API_KEY, PINECONE_INDEX_NAME

pc = Pinecone(api_key=PINECONE_API_KEY)


def create_index_if_not_exists(dimension: int):
    existing = [i["name"] for i in pc.list_indexes()]

    if PINECONE_INDEX_NAME not in existing:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )


def get_index():
    return pc.Index(PINECONE_INDEX_NAME)


def upsert_vectors(vectors: list):
    index = get_index()
    index.upsert(vectors=vectors)


def query_vector(vector: list, top_k=5):
    index = get_index()
    return index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True
    )
