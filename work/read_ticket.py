import json
from pathlib import Path

raw_text = Path("data/ticket.json").read_text()
ticket = json.loads(raw_text)

print(type(raw_text).__name__)
print(type(ticket).__name__)
print(ticket["id"])
print(ticket["text"])

print(ticket["text"].lower())

result = {"id": ticket["id"], "category": "billing"}
print(json.dumps(result, indent=2))
