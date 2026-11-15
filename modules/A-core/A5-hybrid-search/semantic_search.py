"""Simple word-overlap similarity placeholder; real embeddings are a later enhancement."""
def score(query,text):
    q=set(query.lower().split()); t=set(text.lower().split())
    return len(q&t)/max(1,len(q|t))
