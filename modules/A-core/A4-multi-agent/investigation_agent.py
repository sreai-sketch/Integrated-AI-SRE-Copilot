from agent_messages import message
def run(incident):
    return message("investigation",f"reason={incident.get('reason')}; exit_code={incident.get('exit_code')}")
