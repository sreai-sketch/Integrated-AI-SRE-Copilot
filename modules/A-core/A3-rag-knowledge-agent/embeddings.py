"""Deterministic demo vector only; not a semantic embedding model."""
import hashlib
def embed_text(text, dimensions=16):
    d=hashlib.sha256(text.lower().encode()).digest()
    return [d[i]/255 for i in range(dimensions)]
