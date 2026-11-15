from typing import TypedDict
class WorkflowState(TypedDict,total=False):
    incident:dict
    evidence:list[str]
    diagnosis:str
    decision:str
    status:str
