from contracts import Ticket

ticket = Ticket.model_validate({"id": "T-001", "text": "Hello"})
print(ticket.text)
print(ticket.model_dump())
