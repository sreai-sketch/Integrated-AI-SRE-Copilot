from hybrid_retriever import search
def test_hybrid_search():
    assert search("OOMKilled memory",["OOMKilled pod memory limit","blue website theme"])[0].startswith("OOMKilled")
