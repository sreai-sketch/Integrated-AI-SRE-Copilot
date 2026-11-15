from pathlib import Path
from document_parser import read_document
from chunker import chunk_text
from vector_store import LocalStore
def ingest(folder="knowledge_base"):
    store=LocalStore()
    for p in Path(folder).glob("*.md"):
        for chunk in chunk_text(read_document(p)): store.add(chunk,{"source":p.name})
    return store
