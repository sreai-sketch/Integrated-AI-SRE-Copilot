from fastapi import APIRouter
from models import IncidentRequest
from incident_manager import create_incident
router=APIRouter()
@router.post("/incidents")
def submit(request:IncidentRequest): return create_incident(request)
