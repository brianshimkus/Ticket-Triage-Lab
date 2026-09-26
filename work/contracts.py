from typing import Literal
from pydantic import BaseModel, Field


class Ticket(BaseModel):
    id: str = Field(min_length=1)
    text: str = Field(min_length=1, max_length=4000)


class Prediction(BaseModel):
    category: Literal["billing", "account", "technical", "other"]
    reason: str
