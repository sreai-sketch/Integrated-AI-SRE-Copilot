from dataclasses import dataclass,field
@dataclass
class SharedState:
    evidence:list[str]=field(default_factory=list)
    diagnosis:str=""
