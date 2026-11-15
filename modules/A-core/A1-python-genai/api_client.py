from config import OPENAI_API_KEY, OPENAI_MODEL
from models import Diagnosis
def diagnose(incident, offline=False):
    if offline:
        return Diagnosis(summary=f"{incident.service} reported {incident.reason}",
          possible_cause="Investigate logs and resource metrics; cause is not confirmed.",
          recommended_checks=["Check previous logs", "Review Pod events", "Check memory metrics"])
    if not OPENAI_API_KEY:
        raise RuntimeError("Set OPENAI_API_KEY or use offline=True")
    from openai import OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = ("Analyze this incident using only supplied evidence. Return JSON with "
      "summary, possible_cause, recommended_checks. Incident: " + incident.model_dump_json())
    response = client.responses.create(model=OPENAI_MODEL, input=prompt)
    import json
    return Diagnosis.model_validate(json.loads(response.output_text))
