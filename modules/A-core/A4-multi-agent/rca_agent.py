from agent_messages import message
def run(evidence,guidance):
    cause="Possible memory limit issue" if "oom" in evidence.lower() else "Cause not established"
    return message("rca",cause+"; "+guidance)
