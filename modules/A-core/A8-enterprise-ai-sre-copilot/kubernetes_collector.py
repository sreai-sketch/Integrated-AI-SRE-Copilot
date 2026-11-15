"""Safe demo collector; real cluster connection will be added with read-only RBAC."""
def collect_pod_evidence(pod,observed=None):
    return {"pod":pod,"observed":observed or {"phase":"Unknown"},"mode":"demo_read_only"}
