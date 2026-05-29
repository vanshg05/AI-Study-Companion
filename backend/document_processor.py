from backend.pdf_processor import extract_text_from_pdf
from backend.text_chunker import chunk_text
from backend.vector_store import store_chunks

def process_pdf(pdf_path):

    text = extract_text_from_pdf(
        pdf_path
    )

    chunks = chunk_text(text)

    store_chunks(chunks)

    return len(chunks)