import pytest
from guardrails import require_approval,require_evidence
def test_approval_gate():
    with pytest.raises(PermissionError): require_approval(False)
def test_evidence_gate():
    with pytest.raises(ValueError): require_evidence([])
