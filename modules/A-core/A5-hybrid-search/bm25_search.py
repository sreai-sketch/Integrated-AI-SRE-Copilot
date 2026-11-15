"""Teaching example using term frequency; not a full BM25 implementation."""
from collections import Counter
def score(query,text):
    c=Counter(text.lower().split())
    return sum(c[w] for w in query.lower().split())
