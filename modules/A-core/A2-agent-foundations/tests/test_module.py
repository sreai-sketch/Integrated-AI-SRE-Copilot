from react_agent import investigate
def test_agent_hypothesis():
    assert "possible_memory_issue" in investigate("test","OOMKilled",137).diagnosis
