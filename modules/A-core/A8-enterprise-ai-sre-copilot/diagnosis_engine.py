def diagnose(evidence):
    oom=str(evidence.get("reason","")).lower()=="oomkilled"
    return {"summary":f"Incident reported for {evidence.get('service','unknown')}",
      "possible_cause":"Possible memory limit issue; verify with metrics and logs." if oom else "Cause not established; collect more evidence.",
      "supporting_evidence":evidence,"recommended_checks":["Review logs","Review Pod events","Check resource metrics"],
      "requires_human_review":True}
