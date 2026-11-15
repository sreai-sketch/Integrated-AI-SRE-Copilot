def fuse(rankings,k=60):
    scores={}
    for ranking in rankings:
        for rank,item in enumerate(ranking,1): scores[item]=scores.get(item,0)+1/(k+rank)
    return sorted(scores.items(),key=lambda x:x[1],reverse=True)
