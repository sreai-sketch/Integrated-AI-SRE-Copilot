def require_evidence(evidence):
    if not evidence: raise ValueError("Evidence is required")
def require_approval(approved):
    if not approved: raise PermissionError("Human approval is required")
