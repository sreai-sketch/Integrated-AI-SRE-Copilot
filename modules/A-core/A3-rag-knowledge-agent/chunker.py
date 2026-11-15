def chunk_text(text, size=80):
    if size<=0: raise ValueError("size must be positive")
    words=text.split()
    return [" ".join(words[i:i+size]) for i in range(0,len(words),size)]
