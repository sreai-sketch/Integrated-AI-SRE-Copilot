def decide(value):
    d=value.upper()
    if d not in {"APPROVE","REJECT","HOLD"}: raise ValueError("Use APPROVE, REJECT or HOLD")
    return {"decision":d,"may_continue":d=="APPROVE"}
