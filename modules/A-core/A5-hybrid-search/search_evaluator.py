def reciprocal_rank(relevant,results):
    return 1/(results.index(relevant)+1) if relevant in results else 0.0
