from rag_pipeline import search_knowledge
def test_oom_runbook_retrieval():
    assert "memory" in search_knowledge("OOMKilled memory").lower()
