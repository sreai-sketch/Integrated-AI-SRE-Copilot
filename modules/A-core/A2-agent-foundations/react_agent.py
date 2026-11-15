from agent_state import AgentState
from reflex_rules import classify
def investigate(task,reason,exit_code=None):
    state=AgentState(task)
    state.observations.append(f"Observed reason={reason}, exit_code={exit_code}")
    state.diagnosis=f"Initial hypothesis: {classify(reason,exit_code)}. Verify with logs and metrics."
    return state
