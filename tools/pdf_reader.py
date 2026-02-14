import os
from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def load_pdfs_from_folder(folder_path: str):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            full_path = os.path.join(folder_path, file)
            text = read_pdf(full_path)

            documents.append({
                "filename": file,
                "text": text
            })

    return documents


def chunk_text(text: str, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks
