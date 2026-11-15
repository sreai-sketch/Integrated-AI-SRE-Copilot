from routing import route
from approval import validate_decision
def test_routes():
    assert route({"decision":"APPROVE"})=="approved"
    assert route({"decision":"HOLD"})=="hold"
def test_decision():
    assert validate_decision("reject")=="REJECT"
