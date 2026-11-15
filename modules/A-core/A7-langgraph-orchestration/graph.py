from langgraph.graph import StateGraph,END
from state import WorkflowState
from nodes import investigate,diagnose,approval
from routing import route
def build_graph():
    g=StateGraph(WorkflowState)
    g.add_node("investigate",investigate); g.add_node("diagnose",diagnose); g.add_node("approval",approval)
    g.set_entry_point("investigate"); g.add_edge("investigate","diagnose"); g.add_edge("diagnose","approval")
    g.add_conditional_edges("approval",route,{"approved":END,"rejected":END,"hold":END})
    return g.compile()
if __name__=="__main__":
    print(build_graph().invoke({"incident":{"reason":"OOMKilled"},"decision":"HOLD"}))
