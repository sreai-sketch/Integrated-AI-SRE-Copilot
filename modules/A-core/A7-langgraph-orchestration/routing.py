def route(state):
    d=state.get("decision","HOLD").upper()
    return "approved" if d=="APPROVE" else "rejected" if d=="REJECT" else "hold"
