from types import SimpleNamespace
import pytest
from pydantic import ValidationError
from contracts import Ticket, Prediction
from triage import classify_rule, classify_live


def test_error_wins_over_login():
    result = classify_rule(Ticket(id="1", text="login gives an error"))
    assert result.category == "technical"


def test_missing_text_rejected():
    with pytest.raises(ValidationError):
        Ticket.model_validate({"id": "1"})


def test_unknown_category_rejected():
    with pytest.raises(ValidationError):
        Prediction(category="urgent", reason="bad category")


def test_refusal_has_no_success_record():
    fake = SimpleNamespace(
        responses=SimpleNamespace(
            parse=lambda **kwargs: SimpleNamespace(output_parsed=None)
        )
    )
    with pytest.raises(RuntimeError, match="No parsed"):
        classify_live(Ticket(id="1", text="hello"), fake)


def test_network_error_is_not_silently_a_mock():
    def fail(**kwargs):
        raise TimeoutError("simulated timeout")

    fake = SimpleNamespace(responses=SimpleNamespace(parse=fail))
    with pytest.raises(TimeoutError):
        classify_live(Ticket(id="1", text="hello"), fake)
