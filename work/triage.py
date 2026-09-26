import argparse
import json
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from contracts import Ticket, Prediction

load_dotenv()


def classify_rule(ticket):
    # Implement this function in the matching tutorial lesson.
    raise NotImplementedError("Complete classify_rule in the tutorial")


def classify_live(ticket, client=None):
    # Implement this function in the matching tutorial lesson.
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
