from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import get_all_expenses, get_expense_cat, create_table, get_expense, create_expense, modify_expense, replace_expense, delete_expense
from datetime import date as Date


app = FastAPI()

create_table()

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
    


@app.get("/")
def home():
    return {"message": "the tracker is up and running"}

@app.get("/expenses")
def get_expenses(category: str | None = None):
    if category is None:
        return get_all_expenses()
    else:
        return get_expense_cat(category)

@app.get("/expenses/{expense_id}")
def grab_expense(expense_id: int):
    expense = get_expense(expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="expense not found")
    return expense


@app.post("/expenses", status_code=201)
def new_expense(expense: Expense):

    new_id = create_expense(expense.name, expense.amount, expense.category, expense.date)

    return {"message": "expense saved successfully", "expense": get_expense(new_id)}

    
@app.patch("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense_Update):

    if expense.name is None and expense.amount is None and expense.category is None and expense.date is None:
        raise HTTPException(status_code=400, detail="no update fields provided")
    
    update = modify_expense(expense_id, name=expense.name, amount=expense.amount, category=expense.category, date_entered=expense.date)

    if update is False:
        raise HTTPException(status_code=404, detail="expense not found")
    
    return {"message": "expense updated successfully", "expense": get_expense(expense_id)}   
    

@app.put("/expenses/{expense_id}")
def swap_expense(expense_id: int, expense: Expense):
    
    replace = replace_expense(expense_id, name=expense.name, amount=expense.amount, category=expense.category, date_entered=expense.date)

    if replace is False:
        raise HTTPException(status_code=404, detail="expense not found")
        
    return  {"message": "expense updated successfully", "expense": get_expense(expense_id)}


@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int):

    expense_deleted = get_expense(expense_id)

    remove = delete_expense(expense_id)

    if remove is False:
        raise HTTPException(status_code=404, detail="expense not found")
    
    return {"message": "expense deleted successfully", "expense": expense_deleted}