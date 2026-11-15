class AgentMemory:
    def __init__(self): self.items=[]
    def remember(self,item): self.items.append(item)
    def recall(self): return list(self.items)
