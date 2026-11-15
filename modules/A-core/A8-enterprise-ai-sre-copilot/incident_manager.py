from models import IncidentRequest
def create_incident(data:IncidentRequest):
    return {"service":data.service,"pod":data.pod,"reason":data.reason,"status":"investigation_requested"}
