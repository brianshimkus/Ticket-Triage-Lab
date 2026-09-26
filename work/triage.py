import argparse
import json
import os
import time
from pathlib import Path

from contracts import Prediction, Ticket
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]
from openai import OpenAI  # noqa: F401

load_dotenv()


def classify_rule(ticket):
    text = ticket.text.lower()
    for category, words in [
        ("billing", ["invoice", "refund", "charged"]),
        ("technical", ["error", "api", "timeout"]),
        ("account", ["login", "password", "locked out"]),
    ]:
        if any(word in text for word in words):
            return Prediction(category=category, reason="Keyword rule matched.")
    return Prediction(category="other", reason="No keyword rule matched.")


def classify_live(ticket, client=None):
    raise NotImplementedError("Complete classify_live in the tutorial")


def run(ticket, mode="mock"):
    start = time.perf_counter()
    if mode == "mock":
        result, usage = classify_rule(ticket), {}
    elif mode == "live":
        result, usage = classify_live(ticket)
    else:
        raise ValueError("mode must be mock or live")
    return {
        "ticket_id": ticket.id,
        "mode": mode,
        "model": os.getenv("OPENAI_MODEL", "gpt-4.1-mini") if mode == "live" else None,
        "prediction": result.model_dump(),
        "usage": usage,
        "latency_ms": round((time.perf_counter() - start) * 1000, 2),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="data/ticket.json")
    parser.add_argument("--mode", choices=["mock", "live"], default="mock")
    args = parser.parse_args()
    ticket = Ticket.model_validate_json(Path(args.path).read_text())
    record = run(ticket, args.mode)
    Path("output").mkdir(exist_ok=True)
    Path("output/result.json").write_text(json.dumps(record, indent=2))
    print(json.dumps(record, indent=2))
