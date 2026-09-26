import argparse
import json
from pathlib import Path
from contracts import Ticket
from triage import run


def evaluate(split="dev", mode="mock"):
    cases = json.loads(Path("data/cases.json").read_text())
    rows = []
    for case in cases:
        if case["split"] != split:
            continue
        record = run(Ticket(id=case["id"], text=case["text"]), mode)
        actual = record["prediction"]["category"]
        rows.append(
            {
                "id": case["id"],
                "expected": case["expected"],
                "actual": actual,
                "correct": actual == case["expected"],
            }
        )
    correct = sum(row["correct"] for row in rows)
    return {
        "split": split,
        "mode": mode,
        "correct": correct,
        "count": len(rows),
        "accuracy": correct / len(rows),
        "rows": rows,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=["dev", "holdout"], default="dev")
    parser.add_argument("--mode", choices=["mock", "live"], default="mock")
    args = parser.parse_args()
    report = evaluate(args.split, args.mode)
    Path("output").mkdir(exist_ok=True)
    Path(f"output/eval-{args.split}-{args.mode}.json").write_text(
        json.dumps(report, indent=2)
    )
    print(json.dumps(report, indent=2))
