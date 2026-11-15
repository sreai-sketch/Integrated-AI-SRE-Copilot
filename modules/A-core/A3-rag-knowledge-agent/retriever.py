def retrieve(query,docs,top_k=3):
    terms=set(query.lower().split())
    ranked=sorted(((len(terms & set(d["text"].lower().split())),d) for d in docs),key=lambda x:x[0],reverse=True)
    return [d for score,d in ranked[:top_k] if score>0]
