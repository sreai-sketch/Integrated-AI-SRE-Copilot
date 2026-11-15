import json
from pathlib import Path
from models import Incident
def load_incident(path):
    return Incident.model_validate(json.loads(Path(path).read_text()))
