from pydantic import BaseModel
class IncidentRequest(BaseModel):
    service:str
    pod:str
    reason:str
    exit_code:int|None=None
class ApprovalRequest(BaseModel):
    decision:str
