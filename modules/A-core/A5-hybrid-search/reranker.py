def rerank(query,docs):
    terms=set(query.lower().split())
    return sorted(docs,key=lambda d:len(terms & set(d.lower().split())),reverse=True)
