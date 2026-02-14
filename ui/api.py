from fastapi import FastAPI
from pipelines.rag_pipeline import rag_query

app = FastAPI(title="AI Research Agent API")


@app.get("/")
def home():
    return {"message": "AI Research Agent API running"}


@app.post("/research")
def research(query: str):
    answer = rag_query(query)
    return {"query": query, "answer": answer}
