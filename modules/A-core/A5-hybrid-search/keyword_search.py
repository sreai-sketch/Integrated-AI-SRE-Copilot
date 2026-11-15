def score(query,text): return sum(1 for w in set(query.lower().split()) if w in text.lower())
