def incident_message(d):
    return f"INCIDENT REVIEW REQUIRED\n{d.get('summary')}\nPossible cause: {d.get('possible_cause')}\nAPPROVE / REJECT / HOLD"
