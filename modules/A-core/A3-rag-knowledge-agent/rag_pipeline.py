from ingestion import ingest
from retriever import retrieve
from context_builder import build_context
def search_knowledge(query,folder="knowledge_base"):
    store=ingest(folder)
    return build_context(retrieve(query,store.docs))
