from agent_messages import message
def run(incident):
    advice="Review logs, events and metrics."
    if incident.get("reason","").lower()=="oomkilled": advice="Review memory usage, limits, previous logs and node capacity."
    return message("knowledge",advice)
