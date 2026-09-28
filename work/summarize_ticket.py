import json
from pathlib import Path

raw_text = Path("data/ticket.json").read_text()
ticket = json.loads(raw_text)
print(ticket["id"])
print(len(ticket["text"]))
