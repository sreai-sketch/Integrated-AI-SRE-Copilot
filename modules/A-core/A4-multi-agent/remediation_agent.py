from agent_messages import message
def run(diagnosis):
    return message("remediation","Proposal only: gather supporting metrics and prepare a minimal reviewed YAML change. "+diagnosis)
