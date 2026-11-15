def investigate(state):
    incident=state.get("incident",{})
    return {"evidence":[f"reason={incident.get('reason','unknown')}"],"status":"investigated"}
def diagnose(state):
    evidence=state.get("evidence",[])
    cause="Possible memory issue" if any("OOMKilled" in x for x in evidence) else "Cause unknown"
    return {"diagnosis":cause,"status":"diagnosed"}
def approval(state):
    return {"status":"approval_"+state.get("decision","HOLD").lower()}
