from pydantic import BaseModel, Field
class Incident(BaseModel):
    service: str
    pod: str
    reason: str
    exit_code: int | None = None
    restart_count: int = Field(default=0, ge=0)
class Diagnosis(BaseModel):
    summary: str
    possible_cause: str
    recommended_checks: list[str]
