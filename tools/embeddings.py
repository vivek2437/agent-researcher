from sentence_transformers import SentenceTransformer
from typing import List

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def embed_text(text: str) -> List[float]:
    """
    Embed a single text string.
    """
    return model.encode(text).tolist()


def embed_batch(texts: List[str]) -> List[List[float]]:
    """
    Embed multiple texts.
    """
    return model.encode(texts).tolist()
