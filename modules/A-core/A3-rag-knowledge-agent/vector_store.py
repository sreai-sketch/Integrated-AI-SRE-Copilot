class LocalStore:
    def __init__(self): self.docs=[]
    def add(self,text,metadata=None): self.docs.append({"text":text,"metadata":metadata or {}})
