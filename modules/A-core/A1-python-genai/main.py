import argparse
from json_handler import load_incident
from api_client import diagnose
p=argparse.ArgumentParser()
p.add_argument("--incident", default="examples/sample_incident.json")
p.add_argument("--offline", action="store_true")
a=p.parse_args()
print(diagnose(load_incident(a.incident), offline=a.offline).model_dump_json(indent=2))
