from keyword_search import score as keyword_score
from semantic_search import score as semantic_score
def search(query,docs,top_k=3):
    ranked=[(keyword_score(query,d)+semantic_score(query,d),d) for d in docs]
    return [d for s,d in sorted(ranked,reverse=True)[:top_k] if s>0]
