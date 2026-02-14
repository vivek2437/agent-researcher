import uuid
from tools.pdf_loader import load_pdfs_from_folder, chunk_text
from core.embeddings import embed_text
from tools.vector_db import (
    create_index_if_not_exists,
    upsert_vectors,
    get_index
)

EMBEDDING_DIMENSION = 384
DATA_FOLDER = "data/raw_papers"


def ingest_pdfs():
    print("🚀 Starting PDF ingestion...\n")

    # 1️⃣ Ensure index exists
    create_index_if_not_exists(EMBEDDING_DIMENSION)

    documents = load_pdfs_from_folder(DATA_FOLDER)

    if not documents:
        print("❌ No PDFs found in data/raw_papers/")
        return

    all_vectors = []
    total_chunks = 0

    for doc in documents:
        print(f"📄 Processing: {doc['filename']}")

        chunks = chunk_text(doc["text"])
        print(f"   → {len(chunks)} chunks created")

        for chunk in chunks:
            embedding = embed_text(chunk)

            vector = {
                "id": str(uuid.uuid4()),
                "values": embedding,
                "metadata": {
                    "source": doc["filename"],
                    "text": chunk
                }
            }

            all_vectors.append(vector)
            total_chunks += 1

    if not all_vectors:
        print("❌ No chunks generated. Check PDF extraction.")
        return

    print("\n📦 Uploading vectors to Pinecone...")
    upsert_vectors(all_vectors)

    # Verify count
    index = get_index()
    stats = index.describe_index_stats()

    print("\n✅ Ingestion completed successfully.")
    print(f"📊 Total chunks uploaded: {total_chunks}")
    print(f"📊 Pinecone total vectors: {stats['total_vector_count']}")


if __name__ == "__main__":
    ingest_pdfs()
