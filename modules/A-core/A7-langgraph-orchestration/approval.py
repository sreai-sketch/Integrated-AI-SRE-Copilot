def validate_decision(decision):
    d=decision.upper()
    if d not in {"APPROVE","REJECT","HOLD"}: raise ValueError("Use APPROVE, REJECT or HOLD")
    return d
