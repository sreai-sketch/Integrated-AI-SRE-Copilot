from models import Incident
from api_client import diagnose
def test_offline_diagnosis():
    result=diagnose(Incident(service="survey",pod="p1",reason="OOMKilled"),offline=True)
    assert result.recommended_checks
