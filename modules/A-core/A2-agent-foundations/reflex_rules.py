def classify(reason, exit_code=None):
    if reason.lower()=="oomkilled" or exit_code==137: return "possible_memory_issue"
    if reason.lower() in {"error","crashloopbackoff"}: return "application_startup_issue"
    return "needs_investigation"
