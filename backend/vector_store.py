import uuid
import chromadb # type: ignore

from sentence_transformers import SentenceTransformer # type: ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter # type: ignore

embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    "study_material"
)

def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_text(text)

def store_document(text):

    chunks = chunk_text(text)

    for chunk in chunks:

        embedding = embedding_model.encode(
            chunk
        ).tolist()

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[chunk],
            embeddings=[embedding]
        )

def retrieve_context(question):

    query_embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return "\n\n".join(
        results["documents"][0]
    )