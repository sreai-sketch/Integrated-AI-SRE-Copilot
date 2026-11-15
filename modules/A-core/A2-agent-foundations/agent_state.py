from dataclasses import dataclass, field
@dataclass
class AgentState:
    task: str
    observations: list[str]=field(default_factory=list)
    diagnosis: str=""
