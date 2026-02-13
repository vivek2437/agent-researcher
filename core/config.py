import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "upstage/solar-pro-3:free"

# Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = "research-agent-index"
PINECONE_CLOUD = "aws"
PINECONE_REGION = "us-east-1"

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"