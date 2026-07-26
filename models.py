from pydantic import BaseModel, Field
from datetime import date as Date


class Expense(BaseModel):
    name: str = Field(min_length = 1)
    amount: float = Field(gt=0)
    category: str = Field(min_length = 1) 
    date: Date

class Expense_Update(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    amount: float | None = Field(default=None, gt=0)
    category: str | None = Field(default=None, min_length=1)
    date: Date | None = None
    