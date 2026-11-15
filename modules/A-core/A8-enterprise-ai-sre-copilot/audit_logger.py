from datetime import datetime,timezone
def record(event,details):
    return {"timestamp":datetime.now(timezone.utc).isoformat(),"event":event,"details":details}
