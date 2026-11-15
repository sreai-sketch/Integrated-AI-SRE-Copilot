from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_compose_has_exactly_two_application_services():
    compose = (ROOT / "infra" / "compose.yaml").read_text()
    assert "auth-service:" in compose
    assert "survey-service:" in compose
    assert compose.count("    build:") == 2


def test_all_nineteen_modules_are_mapped():
    mapping = (ROOT / "docs" / "MODULE-MAP.md").read_text()
    for number in range(1, 20):
        assert f"{number}." in mapping


def test_human_approval_is_explicit():
    architecture = (ROOT / "docs" / "ARCHITECTURE.md").read_text()
    for decision in ("Approve", "Reject", "Hold"):
        assert decision in architecture
