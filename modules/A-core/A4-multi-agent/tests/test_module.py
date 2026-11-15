from orchestrator import run_team
def test_team():
    assert [x["agent"] for x in run_team({"reason":"OOMKilled"})]==["investigation","knowledge","rca","remediation"]
