from models import IncidentRequest
from incident_manager import create_incident
from approval_manager import decide
def test_incident(): assert create_incident(IncidentRequest(service="survey",pod="p1",reason="OOMKilled"))["status"]=="investigation_requested"
def test_approval_gate(): assert decide("HOLD")["may_continue"] is False
